from django.shortcuts import render, redirect
from .models import uploadImage

# Create your views here.
def index(request):
    context = {

    }

    return render(request, 'deepagency/index.html', context=context)

def start(request):
    context = {

    }

    return render(request, 'deepagency/start.html', context=context)

def upload_image(request):
    upload = uploadImage()
    upload.image = request.FILES['image']
    upload.save()

    context = {
        'upload' : upload,
        'upload.image' : upload.image,
    }

    return render(request, 'deepagency/detail.html', context=context)
    # return redirect('deepagency/start/' + str())