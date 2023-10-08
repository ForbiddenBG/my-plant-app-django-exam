from django.core.validators import MinLengthValidator
from django.db import models

from core.validators import only_letters_validation


# Create your models here.
class Plant(models.Model):
    OUTDOOR_PLANTS = "Outdoor Plants"
    INDOOR_PLANTS = "Indoor Plants"

    PLANT_TYPES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    plant_type = models.CharField(
        max_length=14,
        choices=PLANT_TYPES,
    )

    name = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
            only_letters_validation,
        ),
    )

    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()
