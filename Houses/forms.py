from django import forms
from .models import Customer

class UserSignUpForm(forms.ModelForm):
	"""docstring for ClassName"""
	Confirm_Password=forms.CharField(max_length=18,widget=forms.PasswordInput)

	class Meta:
		model=Customer

		fields=["First_Name","Last_Name","Email","Contact","Gender","username","password","Confirm_Password","City","Address_Line_1","Address_Line_2","PinCode"]
		widgets = {
            'Address_Line_1': forms.TextInput(attrs={'placeholder':'Flat,Wing,Building'}),
            'Address_Line_2': forms.TextInput(attrs={'placeholder':'Road,Suburb,City,State'}),
            'password': forms.PasswordInput,
            }

class Email_Verification(forms.Form):
	# """docstring for ClassName"""
	Enter_OTP=forms.CharField(max_length=5)

	widgets={
	'Enter_OTP': forms.TextInput(attrs={'placeholder':'OTP'})
	}