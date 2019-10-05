from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from babelconverter import utils
import requests
from PIL import Image
import numpy as np
@csrf_exempt
def compositeByName(request):
  loaded = json.loads(request.body)
  
  r = requests.request('GET','https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+ loaded["compound-name"] +'/JSON')

  if(r.status_code == 200):
    return HttpResponse(r, content_type='application/json')
  return HttpResponse('Not working')

@csrf_exempt
def compositeImageByName(request):
  loaded = json.loads(request.body)
  compound_name = loaded['compound-name']
  print(compound_name)
  r = requests.request('GET','https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+ compound_name +'/JSON')
  
  smiles = r.json()['PC_Compounds'][0]['props'][18]['value']['sval']
  
  print(smiles)
  file_path = "../temp/"
  command = utils.convert_to_command(smiles, file_path, compound_name)
  os.system(command)
  if(r.status_code == 200):
    return HttpResponse(file_path + compound_name +".svg", content_type="image/svg+xml")
  return HttpResponse('Not working')

@csrf_exempt
def convert(request):
  smiles = request.GET.get('smiles', '')
  size = request.GET.get('size', '300')
  background = request.GET.get('background', '000000')
  composite_name = datetime.datetime.now().__str__() + "-composite"
  file_path = "../temp/"
  file_name = "composite"

  rgb = tuple(int(background[i:i+2], 16) for i in (0, 2, 4))




  
  command = utils.convert_to_command(smiles, file_path, file_name)
  command = command + " -xp " + size
  print(command)
  os.system(command)
  
  im = Image.open(file_path + file_name +".png")
  data = np.array(im)
  red, green, blue = data.T 

  white_areas = (red == 255) & (blue == 255) & (green == 255)
  print(data)
  data[0:][white_areas.T] = (rgb[0], rgb[1], rgb[2])
  print(data)
  im2 = Image.fromarray(data)
  im2.save(file_path + file_name + '.png', "PNG")

  image_data = open(file_path + file_name +".png", "rb").read()
  return HttpResponse(image_data, content_type="image/png")
    
