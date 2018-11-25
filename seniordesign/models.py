
from django import forms
from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager )



import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Definition needs checking ^


'''
#We don't use trash basic models, Licas FapO'Urksi
class User(models.Model):
	uname = models.CharField(max_length = 128)
	hashed_pass = models.CharField(max_length = 128)
'''



# we're going to need tables for rooms, courses, professors, and...?




#UserManager defines creating user
class UserManager(BaseUserManager):
    def create_user(self, email, password = None, is_active = True, is_staff = False, is_admin = False):
        if not email: raise ValueError("Users must have an email address! ")
        if not password: raise ValueError("Users must have a password! ")
       # print("yerrrr")
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff  = is_staff
        user_obj.admin  = is_admin
        user_obj.save(using=self.db)
        return user_obj

    def create_staffuser(self, email, password = None):
        user_obj = self.create_user(email, password=password, is_staff =True)
        return user_obj

    def create_superuser(self, email, password = None):
        user_obj = self.create_user(email, password=password, is_staff =True, is_admin = True)
        return user_obj



#customUser not standard django User class
class User(AbstractBaseUser):
    email           = models.EmailField(max_length= 255, unique =True, default = "example@nyu.edu")
    active          = models.BooleanField(default= True)
    staff           = models.BooleanField(default = False)
    admin           = models.BooleanField(default = False)
    memberSince     = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def _str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        #"Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        #"Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        #"Is the user active?"
        return self.active

#Custom User basic profile
class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE,)
    firstName       = models.CharField(max_length = 30)
    lastName        = models.CharField(max_length = 30)
    username        = models.CharField(max_length = 30)
    university      = models.CharField(max_length = 30)
	#need path to be specified for next line
    profilePic      = models.ImageField(default = os.path.join(BASE_DIR, "NeedPath") )
    
    YEAR_IN_SCHOOL_CHOICES = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    )
    year_in_school = models.CharField(max_length=15, choices=YEAR_IN_SCHOOL_CHOICES, default='Freshman',)
    
