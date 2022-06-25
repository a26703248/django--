from django.shortcuts import HttpResponse, render

# Create your views here.
def hello(request):
    return HttpResponse("Hello")

def html_tag(request):
    return HttpResponse("<h1>html_tag</h1>")

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
