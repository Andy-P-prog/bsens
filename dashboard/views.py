from django.shortcuts import render
from django.http import HttpResponse
from .get_query import download
# Create your views here.
def dash(request):
    return render(request,'dashboard/index.html')

def home(request):
    return render(request,'home/home.html')

def download_file(request):
    if request.method=='POST':
        title=request.POST['title']       
        upload1=request.FILES['upload']
        object=upload.objects.create(title=title,upload=upload1)
        object.save()  
    context=upload.objects.all()
    return render(request,'index1.html',{'context':context})