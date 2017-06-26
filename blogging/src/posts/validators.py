from django.core.exceptions import ValidationError

def content_validation(value):
    content = value 
    if content == "ñelda":
        raise ValidationError("Cannot be 'ñelda'")
    return content
