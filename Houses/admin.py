from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_fields=['username','First_Name','Last_Name','Email','Contact','Gender','City','Address_Line_1','Address_Line_2','PinCode']
	search_fields=['username','First_Name','Email','Address_Line_1','PinCode']
	readonly_fields=['username','First_Name','Last_Name','Email','Contact','Gender','City','Address_Line_1','Address_Line_2','PinCode','password']

	filter_horizontal=()
	list_filter=()
	fieldsets=()

admin.site.register(Customer,CustomerAdmin)