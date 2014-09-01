# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """Model for SatNOGS users."""

    bio = models.TextField(validators=[MaxLengthValidator(1000)])

    def __unicode__(self):
        return self.username
