from django.db import models
from Houses.models import Customer
from django.utils import timezone 
# Create your models here.

class Electrical(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	choices_problems=[('Repairs_&_Fixes','Repairs & Fixes'),('House_Wiring_and_Short-Circuits','House Wiring & Short-Circuits'),('Society_Electrical_Break-Downs','Society Electrical Break-Downs'),('Device_Installation_and_Setup','Device Installation & Setup'),('Customized','Others')]
	choices_devices=[('Air_Conditioner','Air Conditioner'),('Tube_lights','Tube-lights'),('Fans','Fans'),('Washing_Machines','Washing Machines'),('Refridgerators','Refridgerators'),('Televisions','Televisions'),('Vacuum_Cleaners','Vacuum Cleaners'),('Aqua_Guards','Aqua Guards'),('Microwave','Microwave'),('Gysers','Gysers'),('Customized','Others')]
	Needed_For=models.CharField(max_length=50,choices=choices_problems)
	Device=models.CharField(max_length=50,choices=choices_devices)
	Preferred_Date=models.CharField(max_length=50,default='Null')
	Preferred_Time=models.CharField(max_length=50,default='Null')
	Address_of_Service=models.TextField(default='Null')
	Date_of_Complaint=models.DateTimeField(default=timezone.now)
	PinCode=models.CharField(max_length=6)
	Description=models.TextField()
	Completed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.customer.username} Electrical'


class Plumber(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	choices_problems=[('Taps_and_Leakages','Taps & Leakages'),('Repairs_&_Fixes','Repairs & Fixes'),('Home_Pipes_and_Taps_Fixing','Home : Pipes & Taps Fixing'),('Installation','Installation'),('Customized','Others')]
	Problem_Type=models.CharField(max_length=40,choices=choices_problems)
	Date_of_Complaint=models.DateTimeField(default=timezone.now)
	Preferred_Date=models.CharField(max_length=50,default='Null')
	Preferred_Time=models.CharField(max_length=50,default='Null')
	Address_of_Service=models.TextField(default='Null')	
	PinCode=models.CharField(max_length=6)
	Description=models.TextField()
	Completed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.customer.username} Plumbing'


class Trainer(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	choices_groups=[('Men','Men'),('Women','Women'),('Couple','Couple'),('Kids(Below_15)','Kids(Below 15)'),('Group','Group'),('Customized','Others')]
	choices_fields=[('Yoga_Trainer','Yoga Trainer'),('Fitness_Trainer','Fitness Trainer'),('Dance_Trainer','Dance Trainer'),('Karate_Trainer','Karate Trainer'),('Swimming_Trainer','Swimming Trainer'),('Customized','Others')]
	Needed_For=models.CharField(max_length=30,choices=choices_groups)
	Activity=models.CharField(max_length=30,choices=choices_fields)
	Date_of_Complaint=models.DateTimeField(default=timezone.now)
	Preferred_Date=models.CharField(max_length=50,default='Null')
	Preferred_Time=models.CharField(max_length=50,default='Null')
	Address_of_Service=models.TextField(default='Null')
	PinCode=models.CharField(max_length=6)
	Description=models.TextField()
	Completed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.customer.username} Trainers'


class Salon(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	choices_groups=[('Men','Men'),('Women','Women')]
	choices_fields=[('Hair_Styling','Hair Styling'),('Facial','Facial'),('Beautician_&_Grooming','Beautician and Grooming'),('Customized','Others')]
	Needed_For=models.CharField(max_length=5,choices=choices_groups)
	Activity=models.CharField(max_length=25,choices=choices_fields)
	Date_of_Complaint=models.DateTimeField(default=timezone.now)
	Preferred_Date=models.CharField(max_length=50,default='Null')
	Preferred_Time=models.CharField(max_length=50,default='Null')
	Address_of_Service=models.TextField(default='Null')	
	PinCode=models.CharField(max_length=6)
	Description=models.TextField()
	Completed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.customer.username} Salon'


class Massage(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	choices_groups=[('Men','Men'),('Women','Women')]
	Needed_For=models.CharField(max_length=5,choices=choices_groups)
	Date_of_Complaint=models.DateTimeField(default=timezone.now)
	Preferred_Date=models.CharField(max_length=50,default='Null')
	Preferred_Time=models.CharField(max_length=50,default='Null')
	Address_of_Service=models.TextField(default='Null')	
	PinCode=models.CharField(max_length=6)
	Description=models.TextField()
	Completed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.customer.username} Massage'


class HouseKeeping(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	choices_groups=[('Sofa_Cleaning','Sofa Cleaning'),('Full_Home_Cleaning','Full Home Cleaning'),('Bathroom_and_Toilets_Cleaning','Bathroom and Toilets Cleaning'),('Kitchen_Cleaning','Kitchen Cleaning'),('Backyard_Gardens_Terraces Cleaning','Back-yard/Gardens/Terraces Cleaning'),('Customized','Others')]
	Activity=models.CharField(max_length=50,choices=choices_groups)
	Date_of_Complaint=models.DateTimeField(default=timezone.now)
	Preferred_Date=models.CharField(max_length=50,default='Null')
	Preferred_Time=models.CharField(max_length=50,default='Null')
	Address_of_Service=models.TextField(default='Null')
	PinCode=models.CharField(max_length=6)
	Description=models.TextField()
	Completed = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.customer.username} HouseKeeping'