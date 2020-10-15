from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'home/index.html')

def register(request):
    # template = loader.get_template('home/register.html')
    # return HttpResponse(template.render(request=request))
    return render(request, 'home/register.html')

# def about(request):
#     context = {}
#     return render(request, 'home/about.html')