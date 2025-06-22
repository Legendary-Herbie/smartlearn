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

subjectslist = [
    'Accounting',
    'Biology',
    'Business Management',
    'Chemistry',
    'Christian Religious Studies (CRS)',
    'Core ICT',
    'Core Mathematics',
    'Costing',
    'Economics',
    'Elective Mathematics',
    'English',
    'French',
    'Geography',
    'Government',
    'History',
    'Integrated Science',
    'Literature',
    'Physics',
    'Social Studies'
    ]

def home(request):
    return render(request,'HomePage.html')

def subjects(request):
    return render(request, 'Subjects.html',
    {
        'core_subjects': CORE_SUBJECTS,
        'general_science_electives' : GENERAL_SCIENCE_ELECTIVES,
        'business_electives' : BUSINESS_ELECTIVES,
        'general_arts_electives' : GENERAL_ARTS_ELECTIVES
    })

def resources(request):
    return render(request,'Resources.html')
    
def userprofile(request):
    return render(request,'Profile.html')

def news(request):
    return render(request,'News.html')

def progress(request):
    return render(request,'Progress.html')

def createplan(request):
    return render(request,'CreatePlan.html', {'subjects': subjectslist} )

def about(request):
    return render(request,'About.html')

def accounting(request):
    return render(request,'BusinessElectives/Accounting.html')

def business_management(request):
    return render(request,'BusinessElectives/BusinessManagement.html')

def costing(request):
    return render(request,'BusinessElectives/Costing.html')

def economics(request):
    return render(request,'BusinessElectives/Economics.html')

def core_mathematics(request):
    return render(request,'CoreSubjects/CoreMathematics.html')

def core_ict(request):
    return render(request,'CoreSubjects/Core_ICT.html')

def english(request):
    return render(request,'CoreSubjects/English.html')

def interscience(request):
    return render(request,'CoreSubjects/IntegratedScience.html')

def social_studies(request):
    return render(request,'CoreSubjects/SocialStudies.html')

def crs(request):
    return render(request,'GeneralArtsElectives/CRS.html')

def french(request):
    return render(request,'GeneralArtsElectives/French.html')

def geography(request):
    return render(request,'GeneralArtsElectives/Geography.html')

def government(request):
    return render(request,'GeneralArtsElectives/Government.html')

def history(request):
    return render(request,'GeneralArtsElectives/History.html')

def literature(request):
    return render(request,'GeneralArtsElectives/Literature.html')

def biology(request):
    return render(request,'GeneralScienceElectives/Biology.html')

def chemistry(request):
    return render(request,'GeneralScienceElectives/Chemistry.html')

def elective_mathematics(request):
    return render(request,'GeneralScienceElectives/ElectiveMathematics.html')

def physics(request):
    return render(request,'GeneralScienceElectives/Physics.html')
