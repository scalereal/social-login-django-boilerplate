from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        now = timezone.now()
        user = self.model(email=email.lower(), last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and saves a superuser with the given email and password.
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, **extra_fields)

    def get_user(self, *args, **kwargs):
        try:
            return super(UserManager, self).get(**kwargs)
        except Exception as e:
            print(e)
