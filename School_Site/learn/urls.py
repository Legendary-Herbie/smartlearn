from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'learn'

urlpatterns =  [
    path('', views.home, name = 'Home'),
    path('Subjects/', views.subjects, name = 'Subjects'),
    path('accounts/register/', views.register, name = 'Register'),
    path('accounts/login/', LoginView.as_view(template_name='Authentication/Login.html'), name = 'Login'),
    path('Resources/', views.resources, name = 'Resources'),
    path('News/', views.news, name = 'News'),
    path('Progress/', views.progress, name = 'Progress'),
    path('CreatePlan/', views.createplan, name = 'CreatePlan'),
    path('about/', views.about, name='About'),
    path('logout/', views.logout_view, name='Logout'),
    path('Profile/',views.UserProfileView.as_view(), name ='Profile' ),

    path('BusinessElectives/Accounting/', views.accounting, name='Accounting'),
    path('BusinessElectives/BusinessManagement/', views.business_management, name='BusinessManagement'),
    path('BusinessElectives/Costing/', views.costing, name='Costing'),
    path('BusinessElectives/Economics/', views.economics, name='Economics'),

    path('CoreSubjects/CoreMathematics/', views.core_mathematics, name='CoreMathematics'),
    path('CoreSubjects/Core_ICT/', views.core_ict, name='Core_ICT'),
    path('CoreSubjects/English/', views.english, name='English'),
    path('CoreSubjects/IntegratedScience/', views.interscience, name='IntegratedScience'),
    path('CoreSubjects/SocialStudies/', views.social_studies, name='SocialStudies'),

    path('GeneralArtsElectives/CRS/', views.crs, name='CRS'),
    path('GeneralArtsElectives/French/', views.french, name='French'),
    path('GeneralArtsElectives/Geography/', views.geography, name='Geography'),
    path('GeneralArtsElectives/Government/', views.government, name='Government'),
    path('GeneralArtsElectives/History/', views.history, name='History'),
    path('GeneralArtsElectives/Literature/', views.literature, name='Literature'),

    path('GeneralScienceElectives/Biology/', views.biology, name='Biology'),
    path('GeneralScienceElectives/Chemistry/', views.chemistry, name='Chemistry'),
    path('GeneralScienceElectives/ElectiveMathematics/', views.elective_mathematics, name='ElectiveMathematics'),
    path('GeneralScienceElectives/Physics/', views.physics, name='Physics'),
]