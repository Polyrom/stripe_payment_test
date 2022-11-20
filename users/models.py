from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):

    def __str__(self):
        return self.username
