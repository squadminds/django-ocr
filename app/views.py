from django.shortcuts import render
from PIL import Image
import requests
from matplotlib import pyplot as plt
import easyocr
import numpy as np

def text_extraction(request):
    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image = Image.open(image_file)
                reader = easyocr.Reader(['en'])
                result = reader.readtext(image)
                text = ''
                for r in result:
                    text += r[1] + ' '
                return render(request,"home.html", {"text" : text})
        
            if 'imageurl' in request.POST:
                image_url = request.POST['imageurl']
                response = requests.get(image_url)
                image = response.content
                reader = easyocr.Reader(['en'])
                result = reader.readtext(image)
                text = ''
                for r in result:
                    text += r[1] + ' '
                return render(request,"home.html", {"text" : text})
        except:
            pass
    return render(request,"home.html")