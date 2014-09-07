# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator
from django.db import models


class User(AbstractUser):
    """Model for SatNOGS users."""

    bio = models.TextField(default='', validators=[MaxLengthValidator(1000)])

    def __unicode__(self):
        return self.username
