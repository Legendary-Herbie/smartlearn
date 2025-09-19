from django.db import models

# Create your models here.

class Flashcard(models.Model):
    name = models.CharField(null=True)
    subject = models.TextField(max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cards' ,null=True, blank=True)
    question = models.TextField()
    answer = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__():
        return
