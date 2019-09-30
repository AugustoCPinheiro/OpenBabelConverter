from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from babelconverter import utils
import requests

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
  composite_name = datetime.datetime.now().__str__() + "-composite"
  file_path = "../temp/"
  file_name = "composite"
  command = utils.convert_to_command(smiles, file_path, file_name)
  command = command + " -xp " + size
  print(command)
  os.system(command)
  image_data = open(file_path + file_name +".png", "rb").read()
  return HttpResponse(image_data, content_type="image/png")
    
