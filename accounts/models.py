from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
GenderChoices=(
    ('Male','Male'),
    ('Female','Female'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=GenderChoices, default='')
    contact_details = models.CharField(max_length=15, default='')
    profile_photo = models.FileField(null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.pk})
