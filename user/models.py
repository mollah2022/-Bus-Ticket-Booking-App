from django.db import models
from django.contrib.auth.models import AbstractUser

USER_OPTIONS = (
    ('user','user'),
    ('admin','admin'),
    ('super-admin','super-admin')
)

class SiteUser(AbstractUser):
    phone_number = models.CharField(max_length=20,blank=True)
    special_user = models.CharField(max_length=100,default='user',choices=USER_OPTIONS)

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ('email','username')
