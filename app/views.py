from django.shortcuts import render
from PIL import Image
import requests
from matplotlib import pyplot as plt
import easyocr
import numpy as np
from easyocr import Reader 
from io import BytesIO 

def text_extraction(request):
    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image = Image.open(image_file)
                reader = Reader(['en'])
                result = reader.readtext(np.array(image))  # Convert PIL Image to numpy array
                text = ''
                for r in result:
                    text += r[1] + ' '
                return render(request, "home.html", {"text": text})
        
            if 'imageurl' in request.POST:
                image_url = request.POST['imageurl']
                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))  # Import BytesIO for handling image content
                reader = Reader(['en'])
                result = reader.readtext(np.array(image))  # Convert PIL Image to numpy array
                text = ''
                for r in result:
                    text += r[1] + ' '
                return render(request, "home.html", {"text": text})
        except Exception as e:
            error = "Something Went Wrong."
            return render(request, "home.html", {"error": error})
    return render(request, "home.html")