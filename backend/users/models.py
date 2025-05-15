from django.db import models
import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers.user_manager import UserManager
from django.utils import timezone
from roles.models import Role

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    username = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20,null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username'] 

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "oauth_users"
