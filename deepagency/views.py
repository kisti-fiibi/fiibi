from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }

    return render(request, 'deepagency/index.html', context=context)

def start(request):
    context = {

    }

    return render(request, 'deepagency/start.html', context=context)