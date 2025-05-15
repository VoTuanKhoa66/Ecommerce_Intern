from django.contrib.auth.base_user import BaseUserManager
from roles.models import Role

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, username, email, password=None, phone=None, role=None, is_superuser=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("Email is required")

        if role is None:
            role, created = Role.objects.get_or_create(
                name='customer',
                defaults={'scope': 'customer:basic_access'}
            )
        else:
            role = Role.objects.filter(name=role).first()
            
        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)
        user.role = role
        user.phone = phone
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.is_active = is_active
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        role, _ = Role.objects.get_or_create(
            name='admin',
            defaults={'scope': 'admin:all_manage'}
        )
        return self.create_user(username, email, password, role=role, **extra_fields)