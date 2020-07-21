from django import forms
from .models import Electrical,HouseKeeping,Massage,Plumber,Trainer,Salon

class Form1(forms.ModelForm):

	class Meta:
		model=Electrical

		fields=["Needed_For","Device","Description"]
		widgets = {
		    'Description': forms.Textarea(attrs={'placeholder':'Tell us more about the fault/problem.\nIf "Others" Option Selected in any fields, Pls specify'}),
            }



class Form2(forms.ModelForm):
	class Meta:
		model=HouseKeeping
		fields=["Activity","Description"]
		widgets = {
            'Description': forms.Textarea(attrs={'placeholder':'Tell us more about your request.\nIf "Others" Option Selected in any fields, Pls specify'}),
            }



class Form3(forms.ModelForm): 
	class Meta:
		model=Massage

		fields=["Needed_For","Description"]
		widgets = {
            'Description': forms.Textarea(attrs={'placeholder':'Tell us more about your request.\nIf "Others" Option Selected in any fields, Pls specify'}),
            }



class Form4(forms.ModelForm):
	class Meta:
		model=Plumber

		fields=["Problem_Type","Description"]
		widgets = {
            'Description': forms.Textarea(attrs={'placeholder':'Tell us more about the fault/problem.\nIf "Others" Option Selected in any fields, Pls specify'}),
            }




class Form5(forms.ModelForm):
	class Meta:
		model=Trainer
		
		fields=["Needed_For","Activity","Description"]
		widgets = {
            'Description': forms.Textarea(attrs={'placeholder':'Tell us more about your request.\nIf "Others" Option Selected in any fields, Pls specify'}),
            }



class Form6(forms.ModelForm):
	class Meta:
		model=Salon
		
		fields=["Needed_For","Activity","Description"]
		widgets = {
            'Description': forms.Textarea(attrs={'placeholder':'Tell us more about your request.\nIf "Others" Option Selected in any fields, Pls specify'}),
            }