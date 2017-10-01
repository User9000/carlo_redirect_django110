

from django import forms

# clean methods work by specific fields in this case 'url'
class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit url')

    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        url = cleaned_data["url"]
        print(url)


    def clean_url(self):
        url = self.cleaned_data['url']
        print(url)
        return url