from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin
import uuid


from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
import uuid

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You must provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True, default='')

    # Set unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change this to something unique
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change this to something unique
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    
class Book(models.Model):
    ID = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    ISBN = models.BigAutoField
    publication_date = models.DateField(null=True, blank=True)
    copies_availabel = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    memeber_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True, default='')
    phone = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name
    
class Librarian(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name}"
    
class Borrow(models.Model):
    borrow_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)

    def __str__(self):
        return f"Borrow ID: {self.borrow_id}, Member: {self.member.full_name}"

class Manager(models.Model):
    manager_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Author(models.Model):
    author_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', related_name='authors')

    def __str__(self):
        return self.full_name

