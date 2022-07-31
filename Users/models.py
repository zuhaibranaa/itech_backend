from django.db import models
from RouterOS.models import PPPOE, Profile
from django.core.validators import RegexValidator
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
# Create your models here.

# Custom User Manager
class CustomerManager(BaseUserManager):
    def create_user(self, name, location, cnic, phone, email, image, pppoe=None, profile=None, manager=None, password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name = name,
            image = image,
            location = location,
            cnic = cnic,
            phone = phone,
            pppoe = pppoe,
            profile = profile,
            manager = manager,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class ManagerManager(BaseUserManager):
    def create_user(self, name, location, cnic, phone, email, image, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            image = image,
            location = location,
            cnic = cnic,
            phone = phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, location, cnic, phone, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email = email,
            name = name,
            location = location,
            cnic = cnic,
            phone = phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
# Manager User
class Manager(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='my_picture',blank=True)
    location = models.CharField(max_length=255)
    cnic = models.CharField(max_length=20)
    phone = models.CharField(max_length=500, validators=[phone_regex], unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ManagerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','cnic','phone','location']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
# Customer User
class Customer(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='my_picture',blank=True)
    location = models.CharField(max_length=255)
    cnic = models.CharField(max_length=20)
    phone = models.CharField(max_length=500, validators=[phone_regex], unique=True)
    pppoe = models.ForeignKey(PPPOE,models.CASCADE,null=True)
    profile = models.ForeignKey(Profile,models.CASCADE,null=True)
    manager = models.ForeignKey(Manager,on_delete=models.SET_NULL,null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','cnic','phone','location','profile']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
    
