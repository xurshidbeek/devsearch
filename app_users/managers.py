from django.contrib.auth.models import UserManager

from app_users.models import User
from django.core.exceptions import ValidationError

class MyUsermanager(UserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str = None) -> User:
        if not first_name:
            raise ValidationError('First Name cannot be empty.')
        if not last_name:
            raise ValidationError('Last Name cannot be empty.')
        if not email:
            raise ValidationError('Email Address cannot be empty.')
        if not password:
            raise ValidationError('Password cannot be empty.')

        email = self.normalize_email(email=email)
        username = email[:email.index('@')]

        user = self.model(first_name=first_name,
                          last_name=last_name,
                          email=email,
                          username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name: str,
                         last_name: str ,
                         email: str,
                         password: str) -> User:
        superuser = self.create_user(first_name, last_name, email, password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)

        return superuser