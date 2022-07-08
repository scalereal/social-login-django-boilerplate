from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False, max_length=254, validators=[])
    active = models.BooleanField(default=False, help_text="Active user")
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = (
        models.BooleanField(
            default=False,
            help_text="Designates whether the user can log into this admin site."
            "Unselect this instead of deleting accounts.",
        ),
    )
    date_created = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "users"
        ordering = ["-date_created", "email"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["first_name", "last_name"]),
        ]
