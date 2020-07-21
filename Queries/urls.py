from django.urls import path
from . import views

urlpatterns = [
	path('Electricals/',views.Electrical_Fault,name='Electrical-Fault'),
	path('Trainers/',views.Trainer_Request,name='Trainer-Request'),
	path('Salons/',views.Salon_Request,name='Salon-Request'),
	path('Plumbing/',views.Plumbing_Fault,name='Plumbing-Fault'),
	path('Housekeepings/',views.Housekeeping_Request,name='Housekeeping-Request'),
	path('Massages/',views.Massage_Request,name='Massage-Request'),
	path('Submittion/',views.Form_Submitted,name='Form-Completion-Request'),
]