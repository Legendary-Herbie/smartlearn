from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'HomePage.html')

def subjects(request):
    return render(request, 'Subjects.html')

def resources(request):
    return render(request,'Resources.html')
    
def userprofile(request):
    return render(request,'Profile.html')

def news(request):
    return render(request,'News.html')

def progress(request):
    return render(request,'Progress.html')

def createplan(request):
    return render(request,'CreatePlan.html')

def r(request):
    return render(request,'')
