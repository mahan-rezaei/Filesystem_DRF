from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, password, email):
        if not phone_number:
            raise ValueError('must have phone_number')

        norm_email = self.normalize_email(email)
        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            email=norm_email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            password=password
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user
