

from django import forms
from .validators import validate_dot_com, validate_url
# clean methods work by specific fields in this case 'url'
class SubmitUrlForm(forms.Form):
    url = forms.CharField(
       label='',
        validators=[validate_url],
        widget = forms.TextInput(
            attrs= {
                "placeholder": "Long URL",
                "class": "form-control",
            }
        )
    
    
    )

    """def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        url = cleaned_data.get('url')
        print(url)
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("Invalid URL")
        return url

    """
    """
        The clean url is still needed, because the views get_or_create does not get the
        http  + url into the function, it only gets the url without the http. So the function
        will never find the url and thus it creates again the object.
    """
    def clean_url(self):
        url = self.cleaned_data["url"]
        #print(url)
        if "http" in url:
            return url

        return "http://" + url
