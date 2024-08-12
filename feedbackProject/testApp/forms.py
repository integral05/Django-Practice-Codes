from django import forms 
from django.core import validators

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(label="Password",validators=[validators.MinLengthValidator(8)])
    verify_pwd = forms.CharField(label="Re-Enter Password")
    feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)
    


    def clean(self):
        print("Total Form Validation")
        cleaned_data = super().clean()
        
        pwd = cleaned_data['password']
        rpwd = cleaned_data['verify_pwd']
        if pwd!=rpwd:
            raise forms.ValidationError("Password Do Not Matched")
        
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("Hello Bot You Are Not Welcome")




