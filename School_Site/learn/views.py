from django.shortcuts import render

# Create your views here.
# Subject name to URL mapping for each course
CORE_SUBJECTS = {
    'Core Mathematics': 'CoreMathematics',
    'English': 'English',
    'Integrated Science': 'IntegratedScience',
    'Social Studies': 'SocialStudies',
    'Core ICT': 'Core_ICT',
}

GENERAL_SCIENCE_ELECTIVES = {
    'Biology': 'Biology',
    'Chemistry': 'Chemistry',
    'Physics': 'Physics',
    'Elective Mathematics': 'ElectiveMathematics',
}

BUSINESS_ELECTIVES = {
    'Accounting': 'Accounting',
    'Business Management': 'BusinessManagement',
    'Costing': 'Costing',
    'Economics': 'Economics',
}

GENERAL_ARTS_ELECTIVES = {
    'Christian Religious Studies': 'CRS',
    'Literature': 'Literature',
    'French': 'French',
    'Geography': 'Geography',
    'Government': 'Government',
    'History': 'History',
}

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

def about(request):
    return render(request,'About.html')

def accounting(request):
    return render(request,'Accounting.html')

def business_management(request):
    return render(request,'BusinessManagement.html')

def costing(request):
    return render(request,'Costing.html')

def economics(request):
    return render(request,'Economics.html')

def core_mathematics(request):
    return render(request,'CoreMathematics.html')

def core_ict(request):
    return render(request,'Core_ICT.html')

def english(request):
    return render(request,'English.html')

def interscience(request):
    return render(request,'IntegratedScience.html')

def social_studies(request):
    return render(request,'SocialStudies.html')

def crs(request):
    return render(request,'CRS.html')

def french(request):
    return render(request,'French.html')

def geography(request):
    return render(request,'Geography.html')

def government(request):
    return render(request,'Government.html')

def history(request):
    return render(request,'History.html')

def literature(request):
    return render(request,'Literature.html')

def biology(request):
    return render(request,'Biology.html')

def chemistry(request):
    return render(request,'Chemistry.html')

def elective_mathematics(request):
    return render(request,'ElectiveMathematics.html')

def physics(request):
    return render(request,'Physics.html')
