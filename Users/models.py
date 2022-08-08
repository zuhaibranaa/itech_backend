from django.db import models
from RouterOS.models import PPPOE, Profile
from django.core.validators import RegexValidator
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, name, location, phone, email,roles_id, image=None,password=None,cnic=None):
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
            roles_id = roles_id,
            phone = phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, location, phone,email,roles_id, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email = email,
            # image = image,
            name = name,
            location = location,
            # cnic = cnic,
            phone = phone,
            password=password,
            roles_id=roles_id,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
# Customer User
class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    USER_TYPE = (
        (0,'Customer'),
        (1, 'Manager'),
        (2, 'Admin')
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='my_picture',blank=True,default=None)
    location = models.CharField(max_length=255)
    cnic = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=500, validators=[phone_regex], unique=True)
    pppoe = models.ForeignKey(PPPOE,models.CASCADE,null=True)
    profile = models.ForeignKey(Profile,models.CASCADE,null=True,default=None)
    manager = models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    roles_id = models.IntegerField(default=0,choices=USER_TYPE)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','location','roles_id']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Messages(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    from_user = models.ForeignKey(User,models.CASCADE,verbose_name='Sender',related_name='Sender')
    to_user = models.ForeignKey(User,models.CASCADE,verbose_name='Reciever',related_name='Reciever')
    
    def __str__(self):
        return self.title
    
class Complains(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User,models.CASCADE,verbose_name='User',related_name='Complainer')
    manager = models.ForeignKey(User,models.CASCADE,verbose_name='Manager',related_name='Complainsofficer')
    
    def __str__(self):
        return self.title
    
