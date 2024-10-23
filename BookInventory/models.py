from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin


class CustomeUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have entred ana invalid email!!🙂‍↔️")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save (using=self._db)

        return user 
    
    def create_user (self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_supper_user', False)

        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        # return super().create_superuser(username, email, password, **extra_fields)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=100, blank=True, default='')


    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    employee_profile = models.OneToOneField('Employee', blank=True, null=True, on_delete=models.SET_NULL)
    manager_profile = models.OneToOneField('Manager', blank=True, null=True, on_delete=models.SET_NULL)
    author_profile =models.OneToOneField('Author', null=True, blank=True, on_delete=models.SET_NULL)


    date_joined = models.DateTimeField(auto_now_add=True)  #default=timezone.now (optional)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomeUserManager()

    USER_NAMEFIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS =[]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name 
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]


class Department(models.Model):
    department_name = models.CharField(max_length=250)

    def __str__(self):
        return self.department_name
    
class Book(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    id = models.BigAutoField
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name}, {self.department}"

class Manager(models.Model):
    pass

class Author(models.Model):
    id = models.BigAutoField
    full_name = models.CharField(max_length=100)
    

