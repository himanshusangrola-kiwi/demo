from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)






# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username")
            
#             #create user method
#         user = self.model(
#             email = self.normalize_email(email),#normalize lowercases email
#             username = username
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class account(AbstractBaseUser):
#     email = models.EmailField(max_length=60, unique=True)
#     username = models.CharField(max_length=30,unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username

    

