from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models

class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, USER),
        (ADMIN, ADMIN)
    )


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    objects = UserManager()

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.USER, max_length=13)
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to='user_avatars/', null=True)
    is_active = models.BooleanField(null=True, default=True)

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app):
        return self.is_admin