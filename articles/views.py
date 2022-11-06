from django.shortcuts import render,HttpResponse

# Create your views here.

def list(request):
    return HttpResponse('list tables are created')