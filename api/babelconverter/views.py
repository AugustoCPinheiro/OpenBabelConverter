from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
#from .forms import ConvertSmiles
#from django.shortcuts import render

   
#def test(request):
    #if request.method == 'POST':
      #  form = ConvertSmiles(request.POST)
     #   if form.is_valid():
    #        return HttpResponseRedirect('/thanks/')
   # else:
  #      form = ConvertSmiles()

 #       return render(request, 'convertsmiles.html', {'form': form})

@csrf_exempt
def convert(request):
    loaded = json.loads(request.body)
    os.system("obabel -:"+"'"+loaded['smiles']+"'"+ "-O test.svg")
    image_data = open("../test.svg", "rb").read()
    return HttpResponse(image_data, content_type="image/svg+xml")
    

#@csrf_exempt
#def current_datetime(request):
  #  now = datetime.datetime.now()
 #   print(request.body)
   # html = "<html><body>It is now %s.</body></html>" % now
  
# Create your views here.
