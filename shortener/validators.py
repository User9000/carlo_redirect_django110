from django.core.validators import URLValidator, ValidationError
from django import forms

def validate_url(value):
    url_validator = URLValidator()
    if not "https" or not "http" in value:
        value = "https://" + value

    try:
        url_validator(value)
    except:
        raise ValidationError("Wrong URL")
    print(value)
    return value
def validate_dot_com(value):
    
        if not "com" in value:
            raise forms.ValidationError("This is not valid because of not .com")
        return value

