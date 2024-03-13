from typing import Iterable
from django.db import models

from passwordmanager.util import EncryptHelper



# Create your models here.
class PasswordsManagerModel(models.Model):
    name=models.CharField(max_length=10)
    username=models.TextField()
    url=models.URLField()
    password=models.TextField() 
    def save(self, *args, **kwargs) -> None:
        self.password=EncryptHelper.encrypt(self.password)
        self.username=EncryptHelper.encrypt(self.username)
        super(PasswordsManagerModel, self).save(*args, **kwargs)