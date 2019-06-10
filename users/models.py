''' user models '''
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.


class User(AbstractBaseUser):
    
    username = models.CharField('username', unique=True, max_length=10, db_index=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # unique identifier for users model
    USERNAME_FIELD = 'username'
    
    def __unicode__(self):
        return self.username


