from django.urls import path
from . import views

urlpatterns = [
	path('',views.Homes,name='Web-Home'),
	path('SignUp/',views.SignUp,name='SignUp-User'),
	path('SignIn/',views.SignIn,name='SignIn-User'),
	path('logout/',views.logout,name='Logout'),
	# path('Email_Verify/',views.Email_Verify,name='Email-Verify'),
	path('Payments/',views.Payments,name='Payments'),
	path('ContactUs/',views.ContactUs,name='ContactUs'),
	path('Accounts/',views.MyAccount,name='MyAccount_User'),
	path('MyAccount-Address/',views.MyAccsAdd,name='Address_User'),
	path('Password_Reset/',views.Pass_Reset,name='Password_Reset'),
	path('Password_Reset_User/',views.Pass_Reset_UsrAcc,name='Password_Reset_User'),
	path('My_Problems_HK/',views.USR_Problems1,name='My-Problems-HK'),
	path('My_Problems_Salon/',views.USR_Problems2,name='My-Problems-SL'),
	path('My_Problems_Plumber/',views.USR_Problems3,name='My-Problems-PL'),
	path('My_Problems_Electric/',views.USR_Problems4,name='My-Problems-EL'),
	path('My_Problems_Massage/',views.USR_Problems5,name='My-Problems-MA'),
	path('My_Problems_Trainer/',views.USR_Problems6,name='My-Problems-TR'),
]