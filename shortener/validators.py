from django.core.validators import URLValidator, ValidationError
from django import forms

def validate_url(value):
    url_validator = URLValidator()

    reg_value = value
    if "http" in reg_value:
        new_value = reg_value
    else:
        new_value = "http://" + reg_value

    try:
        url_validator(new_value)
    except:
        raise ValidationError("Wrong URL")
    #print(new_value)
    return new_value
def validate_dot_com(value):
    
        if not "com" in value:
            raise forms.ValidationError("This is not valid because of not .com")
        return value

