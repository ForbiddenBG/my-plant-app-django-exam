from django.core.exceptions import ValidationError


def first_letter_capitalized(value):
    if value != value.capitalize():
        raise ValidationError("Your name must start with a capital letter!")
    return value


def only_letters_validation(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Plant name should contain only letters!")
    return value
