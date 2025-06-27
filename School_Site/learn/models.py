from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    phone_no = models.CharField( max_length=15, blank=True, null=True )
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"

class Plan(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='plans' ,null=True, blank=True)
    subject = models.CharField(max_length=100)
    goal= models.CharField(max_length=255)
    days = models.IntegerField(null = 5)
    hours = models.IntegerField(null = 4)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.subject} {self.goal}"