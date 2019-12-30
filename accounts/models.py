from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, dob, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not dob:
            raise ValueError("Users must have a date of birth")
        
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            dob = dob,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, dob, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            dob = dob,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email  = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True) 
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dob = models.DateField(verbose_name="date of birth", max_length=30, null=True)
    test_completed = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "dob"]

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



