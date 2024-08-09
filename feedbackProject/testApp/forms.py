from django import forms 
from django.core import validators

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])

    def clean(self):
        print("Total Form Validation")
        cleaned_data = super().clean()
        inputName = cleaned_data['name'] 
        if len(inputName) < 10:
            raise forms.ValidationError("Minimum 10 Characters Required")




