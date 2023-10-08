from django.core.validators import MinLengthValidator
from django.db import models

from core.validators import first_letter_capitalized


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(MinLengthValidator(2),),
    )

    first_name = models.CharField(
        max_length=20,
        validators=(first_letter_capitalized,),
    )

    last_name = models.CharField(
        max_length=20,
        validators=(first_letter_capitalized,),
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
