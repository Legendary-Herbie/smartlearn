from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegisterForm
from .models import UserProfile, Plan
from django.contrib.auth import login, logout as django_logout
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Subject name to URL mapping for each course
CORE_SUBJECTS = {
    'Core Mathematics': 'CoreMathematics',
    'English': 'English',
    'Integrated Science': 'IntegratedScience',
    'Social Studies': 'SocialStudies',
    'Core ICT': 'Core_ICT',
}

GENERAL_SCIENCE_ELECTIVES = {
    'Biology': 'Biology', 'Chemistry': 'Chemistry', 'Physics': 'Physics', 'Elective Mathematics': 'ElectiveMathematics',
}

BUSINESS_ELECTIVES = {
    'Accounting': 'Accounting', 'Business Management': 'BusinessManagement', 'Costing': 'Costing', 'Economics': 'Economics',
}

GENERAL_ARTS_ELECTIVES = {
    'Christian Religious Studies': 'CRS', 'Literature': 'Literature', 'French': 'French', 'Geography': 'Geography', 'Government': 'Government', 'History': 'History',
}

subjectslist = [
    'Accounting', 'Biology', 'Business Management', 'Chemistry', 'Christian Religious Studies (CRS)', 'Core ICT', 'Core Mathematics', 'Costing', 'Economics', 'Elective Mathematics', 'English', 'French', 'Geography', 'Government', 'History', 'Integrated Science', 'Literature', 'Physics', 'Social Studies'
    ]

def home(request):
    userprofile = UserProfile.objects.filter(user=request.user).first() if request.user.is_authenticated else None
    if request.user.is_authenticated:
        message = messages.success(request, f'Welcome back, {request.user.username}')
    else:
        message = messages.info(request, 'Welcome to the School Site! Please log in or register.')
    context = {
        'message' : message,
        'userprofile': userprofile,
        'is_authenticated': request.user.is_authenticated,
        'user': request.user,
    }
    if request.method == 'POST':
        current_user = request.user
        subject = request.POST['subject']
        goal= request.POST['goal']
        days = int(request.POST['days'])
        hours = int(request.POST['hours'])
        start = request.POST['start']
        end = request.POST['end']
        new_plan = Plan(user = current_user, subject = subject , goal = goal, days = days, hours = hours, start_date = start, end_date = end)
        new_plan.save()
    return render(request, 'HomePage.html', context)

def subjects(request):
    return render(request, 'Subjects.html',
    {
        'core_subjects': CORE_SUBJECTS,
        'general_science_electives' : GENERAL_SCIENCE_ELECTIVES,
        'business_electives' : BUSINESS_ELECTIVES,
        'general_arts_electives' : GENERAL_ARTS_ELECTIVES
    })

@login_required
def resources(request):
    return render(request,'Resources.html')

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'Profile.html'
    context_object_name = 'user_data'

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)


@login_required
def news(request):
    return render(request,'News.html')

@login_required
def progress(request):
    return render(request,'Progress.html')

@login_required
def createplan(request):
    return render(request,'CreatePlan.html', {'subjects': subjectslist} )

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save the user profile with additional fields
            user_profile = UserProfile(
                user=user,
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone_no=form.cleaned_data.get('phone_no')
            )
            user_profile.save()
            login(request, user)
            return HttpResponseRedirect(reverse('Home'))
        else: 
            return render(request, 'Authentication/Login.html')
    else:
        form = UserRegisterForm()
    return render(request, 'Authentication/Register.html', {'form': form})

def logout_view(request):
    user = request.user
    django_logout(request)
    messages.success(request, f'You have been logged out, {user.username}.')
    return redirect('learn:Home')

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
