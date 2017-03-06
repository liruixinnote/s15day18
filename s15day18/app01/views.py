from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app01 import  models
# Create your views here.

def index(request):
    if request.method == "GET":
        host_list = models.HostInfo.objects.all()
        print(host_list)
        return render(request, "index.html", {"host_list":host_list})



