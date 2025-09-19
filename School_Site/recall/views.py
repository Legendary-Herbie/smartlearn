from django.shortcuts import render
from .models import Flashcard

# Create your views here.

def create(request):
    subjectslist = [
    'Accounting', 'Biology', 'Business Management', 'Chemistry', 'Christian Religious Studies (CRS)', 'Core ICT', 'Core Mathematics', 'Costing', 'Economics', 'Elective Mathematics', 'English', 'French', 'Geography', 'Government', 'History', 'Integrated Science', 'Literature', 'Physics', 'Social Studies'
    ]


    '''if request.user.is_authenticated:
        message = messages.success(request, f'Welcome back, {request.user.username}')
    else:
        message = messages.info(request, 'Welcome to the School Site! Please log in or register.')'''
    if request.method == 'POST':
        current_user = request.user
        subject = request.POST['subject']
        question = request.POST['question']
        new_card = Flashcard(user = current_user, subject = subject)
        new_card.save()
        
    return render(request, 'index.html','subjects:subjectlist')
