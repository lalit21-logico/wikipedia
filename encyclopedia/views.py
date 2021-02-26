from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from encyclopedia.models import Entry
import random

# Create your views here.
def home(request):
    data = Entry.objects.all()
    dataTopics =Entry.objects.all()
    return render(request,"home.html",{'data':data, 'dataTopics':dataTopics})

def create(request):
    dataTopics =Entry.objects.all()
    return render(request, 'create.html',{'dataTopics':dataTopics})

def send(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        subheading = request.POST['subheading']
        discription = request.POST['discription']
        Entry(heading = heading, subheading = subheading, discription = discription).save()
        msg = "Data Save Sucessfully"
        dataTopics =Entry.objects.all()
        return render(request, "home.html",{'msg':msg, 'dataTopics':dataTopics})
    else:
        return HttpResponse("<h1>404 -- Not Found </h1>")

def show(request):
    ID = request.GET['id']
    data = Entry.objects.filter(ID = ID)  
    dataTopics =Entry.objects.all()  
    return render(request, "show.html",{'data':data, 'dataTopics':dataTopics})

def edit(request):
    ID = request.GET['id']
    for data in Entry.objects.filter(ID = ID):
        heading = data.heading
        subheading = data.subheading
        discription = data.discription
        dataTopics =Entry.objects.all() 
    return render(request, "edit.html",{'ID':ID, 'heading':heading, 'subheading':subheading, 'discription':discription, 'dataTopics':dataTopics})

def editRecord(request):
    if request.method == "POST":
        ID = request.POST['ID']
        heading = request.POST['heading']
        subheading = request.POST['subheading']
        discription = request.POST['discription']
        Entry.objects.filter(ID = ID).update(heading = heading, subheading = subheading, discription = discription )
        return HttpResponseRedirect("/")
    else:
        return HttpResponse("<h1>404 -- Not Found </h1>")

        
def randompage(request):
    count = Entry.objects.count()
    ID = random.randint(7, count+7)
    data = Entry.objects.filter(ID = ID)   
    dataTopics =Entry.objects.all()  
    return render(request, "randompage.html",{'data':data, 'dataTopics':dataTopics})

def aboutDevloper(request):
    dataTopics =Entry.objects.all()  
    return render(request, 'about_devloper.html', {'dataTopics':dataTopics})

def aboutWebapp(request):
    dataTopics =Entry.objects.all()  
    return render(request, 'about_webapp.html', {'dataTopics':dataTopics})

def search(request):
    if request.method == "POST":
        heading = request.POST['heading']
        data = Entry.objects.filter(heading = heading)  
        dataTopics =Entry.objects.all()  
        return render(request, "show.html",{'data':data, 'dataTopics':dataTopics})
    else:
        return HttpResponse("<h1>404 -- Not Found </h1>")
   
        

