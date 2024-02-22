from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def portao(request):
    return HttpResponse("Você cegou ao portão da casa")

def sala (request):
    return HttpResponse("Você chegou na sala")

def quarto (request):
    return HttpResponse("Você chegou no quarto")

def post_list(request):
    return render(request, 'blog/post_list.html', {})