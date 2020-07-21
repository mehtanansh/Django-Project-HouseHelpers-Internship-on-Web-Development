from django.contrib import admin
from .models import Electrical,HouseKeeping,Massage,Plumber,Trainer,Salon


class ElectricalAdmin(admin.ModelAdmin):
	list_fields=['customer','Needed_For','Device','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description','Completed']
	search_fields=['PinCode','Needed_For','Device']
	readonly_fields=['customer','Needed_For','Device','Preferred_Date','Preferred_Time','Address_of_Service','Date_of_Complaint','PinCode','Description']

	filter_horizontal=()
	list_filter=()
	fieldsets=()

class PlumberAdmin(admin.ModelAdmin):
	list_fields=['customer','Problem_Type','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description','Completed']
	search_fields=['PinCode','Problem_Type','Device']
	readonly_fields=['customer','Problem_Type','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description']

	filter_horizontal=()
	list_filter=()
	fieldsets=()

class TrainerAdmin(admin.ModelAdmin):
	list_fields=['customer','Needed_For','Activity','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description','Completed']
	search_fields=['PinCode','Needed_For','Activity']
	readonly_fields=['customer','Needed_For','Activity','Preferred_Date','Preferred_Time','Address_of_Service','Date_of_Complaint','PinCode','Description']

	filter_horizontal=()
	list_filter=()
	fieldsets=()

class SalonAdmin(admin.ModelAdmin):
	list_fields=['customer','Needed_For','Activity','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description','Completed']
	search_fields=['PinCode','Needed_For','Activity']
	readonly_fields=['customer','Needed_For','Activity','Preferred_Date','Preferred_Time','Address_of_Service','Date_of_Complaint','PinCode','Description']

	filter_horizontal=()
	list_filter=()
	fieldsets=()

class MassageAdmin(admin.ModelAdmin):
	list_fields=['customer','Needed_For','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description','Completed']
	search_fields=['PinCode','Needed_For']
	readonly_fields=['customer','Needed_For','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description']

	filter_horizontal=()
	list_filter=()
	fieldsets=()

class HouseKeepingAdmin(admin.ModelAdmin):
	list_fields=['customer','Activity','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description','Completed']
	search_fields=['PinCode','Needed_For']
	readonly_fields=['customer','Activity','Date_of_Complaint','Preferred_Date','Preferred_Time','Address_of_Service','PinCode','Description']

	filter_horizontal=()
	list_filter=()
	fieldsets=()

# Register your models here.
admin.site.register(Electrical,ElectricalAdmin)
admin.site.register(Plumber,PlumberAdmin)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Salon,SalonAdmin)
admin.site.register(Massage,MassageAdmin)
admin.site.register(HouseKeeping,HouseKeepingAdmin)