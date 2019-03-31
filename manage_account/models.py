from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator


class User(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    user_id = models.CharField(max_length=20, validators=[MinLengthValidator(6), alphanumeric])
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8), alphanumeric])
    nickname = models.CharField(max_length=30, blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
