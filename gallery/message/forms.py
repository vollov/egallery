from django import forms
from models import Message
from captcha.fields import CaptchaField

class MessageForm(forms.ModelForm):
#     name = forms.CharField(max_length=60, required=True, help_text="Please enter your name.")
#     email = forms.EmailField(max_length=60, required=True)
#     title = forms.CharField(max_length=160)
#     message = forms.Textarea(required=False)
    #captcha = CaptchaField()
    
    name = forms.CharField(max_length=60, required=True, help_text="Please enter your name.")
    title = forms.CharField(max_length=160, help_text="Please enter the title of the message.")
    captcha = CaptchaField()
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Message
        fields = ('name', 'title')