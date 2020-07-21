import re
import random  
import string  
global List_All
List_All=[]
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth,User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import  UserSignUpForm,Email_Verification
from .models import Customer
from Queries.models import Electrical,Plumber,Trainer,Salon,Massage,HouseKeeping

def Get_OTP(size):
	generate_pass = ''.join([random.choice( string.ascii_uppercase +string.ascii_lowercase +string.digits) for n in range(size)])
	return generate_pass
# Create your views here.

def Email_Verify(request):
	global OTP_sent
	if request.user.is_authenticated:
		return render(request,'Houses/HomePage.html',{'title': 'HouseHelpers-Home'})
	else:
		if request.method == 'POST':
			form = Email_Verification(request.POST)
			if form.is_valid():
				PINUsers = form.cleaned_data['Enter_OTP']
				if (PINUsers == OTP_sent):
					global List_All
					user = User.objects.create_user(username=List_All[0],password=List_All[1],first_name=List_All[2],last_name=List_All[3],email=List_All[4])
					user.save()
					PPP=List_All[1]
					PWRD_OG=make_password(PPP)
					Cust=Customer(username=List_All[0],password=PWRD_OG,First_Name=List_All[2],Last_Name=List_All[3],Email=List_All[4],City=List_All[5],Address_Line_1=List_All[6],Address_Line_2=List_All[7],Contact=List_All[8],Gender=List_All[9],PinCode=List_All[10])
					Cust.save()
					messages.info(request,"User Saved!!")
					return redirect('SignIn-User')
				else:
					messages.info(request,"Please Enter the correct OTP!\nWait till we send you another")
					return redirect('Email-Verify')
		else:
			OTP_sent = Get_OTP(5)
			subject="House Helpers"
			message = render_to_string('Houses/Email_Format.html', {
                'user1': List_All[0],
                'otp':OTP_sent,
            })
			from_email=settings.EMAIL_HOST_USER
			to_list=[List_All[4]]
			email_to_send=EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
			email_to_send.content_subtype = "html"
			email_to_send.send(fail_silently=False)
			form = Email_Verification()
			return render(request,'Houses/OTP.html',{'title': 'Email_Verify','form':form})

def Homes(request):
	return render(request,'Houses/HomePage.html',{'title': 'HouseHelpers-Home'})

def ContactUs(request):
	return render(request,'Houses/ContactUs.html',{'title': 'HouseHelpers-ContactUs'})

def SignUp(request):
	if request.user.is_authenticated:
		return render(request,'Houses/HomePage.html',{'title': 'HouseHelpers-Home'})
	else:
		if request.method == 'POST':
			form = UserSignUpForm(request.POST)
			if form.is_valid():
				Contacts=form.cleaned_data['Contact']
				if(len(Contacts))!=10:
					messages.info(request,"Please Enter Valid Contact Number")
					return redirect('SignUp-User')
				Number=['0','1','2','3','4','5','6','7','8','9']
				for i in Contacts:
					if i not in Number:
						messages.info(request,"Please Enter Valid Contact Number")
						return redirect('SignUp-User')
					else:
						continue
				PHN=Contacts
				MATCH=re.match(r"^[789]\d{9}$",PHN)
				if not MATCH:
					messages.info(request,"Please Enter Valid Contact Number (Mobile Numbers start with 7/8/9)")
					return redirect('SignUp-User')
				PC=form.cleaned_data['PinCode']
				LEN1=len(PC)
				if (form.cleaned_data['password']==form.cleaned_data['Confirm_Password'] and LEN1==6):
					A1=form.cleaned_data['username']
					A2=form.cleaned_data['password']
					A3=form.cleaned_data['First_Name']
					A4=form.cleaned_data['Last_Name']
					A5=form.cleaned_data['Email']
					A6=form.cleaned_data['City']
					A7=form.cleaned_data['Address_Line_1']
					A8=form.cleaned_data['Address_Line_2']
					A9=form.cleaned_data['Contact']
					A10=form.cleaned_data['Gender']
					A11=form.cleaned_data['PinCode']
					List1=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]
					global List_All
					List_All=List1
					messages.info(request,"Hello {} You May have recieved an OTP from Us on the registered Email.\n Pls Verify it to proceed!!".format(List1[0]))
					return redirect('Email-Verify')
				else:
					messages.info(request,"Both Passwords don't match")
					return redirect('SignUp-User')
			else:
				messages.info(request,'User / Email already Registered!')
				return redirect('SignUp-User')
		else:
			form = UserSignUpForm()
			return render(request,'Houses/SignUp.html',{'title': 'HouseHelpers-SignUp','form':form})


def SignIn(request):
	if request.user.is_authenticated:
		return render(request,'Houses/HomePage.html',{'title': 'HouseHelpers-Home'})
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)			
			if user is not None:
				login(request,user)
				return redirect("Web-Home")
			else:
				messages.info(request,'Invalid credentials')
				return redirect('SignIn-User')
		else:
			return render(request,'Houses/SignIn.html',{'title': 'HouseHelpers-SignIn'})


@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def Payments(request):
	return render(request,'Houses/Payments.html',{'title': 'HouseHelpers-Payments'})



@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def MyAccount(request):
	if request.method=='POST':
		usernames_req = request.user.username
		u = User.objects.get(username=usernames_req)
		ADD1=request.POST['live1']
		ADD2=request.POST['live2']
		ADD3=request.POST['live3']
		if(ADD1!=None and ADD2!=None and ADD3!=None):
			if (u.check_password(ADD1)):
				if(ADD2==ADD3):
					u = User.objects.get(username=usernames_req)
					u.set_password(ADD2)
					u.save()
					ADD2_real=make_password(ADD2)
					OBJ1=Customer.objects.get(username=usernames_req)
					Custs1=Customer(username=OBJ1.username,password=ADD2_real,First_Name=OBJ1.First_Name,Last_Name=OBJ1.Last_Name,Email=OBJ1.Email,City=OBJ1.City,Address_Line_1=OBJ1.Address_Line_1,Address_Line_2=OBJ1.Address_Line_2,Contact=OBJ1.Contact,Gender=OBJ1.Gender,PinCode=OBJ1.PinCode)
					Custs1.save()
					messages.info(request,"Password Updated!!")
					return redirect('MyAccount_User')
				else:
					messages.info(request,"Note: New passwords don't match")
					return redirect('MyAccount_User')
			else:
				messages.info(request,"Old Password doesn't match")
				return redirect('MyAccount_User')			
		else:
			messages.info(request,"Please Enter Valid Password")
			return redirect('MyAccount_User')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Houses/Profile.html',{'title': 'HouseHelpers-MyAccount','users' : OBJ1})



@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def MyAccsAdd(request):
	if request.method=='POST':
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		ADD1=request.POST['live1']
		ADD2=request.POST['live2']
		ADD3=request.POST['CT2']
		ADD4=request.POST['PC']
		LEN1=len(ADD4)
		if(ADD1!=None and ADD2!=None and LEN1==6):
			NUMBS=['1','2','3','4','5','6','7','8','9','0']	
			for i in ADD4:
				if i not in NUMBS:
					messages.info(request,"Please Enter Valid PinCode ")
					return redirect('Address_User')
				else:
					continue
			Cust=Customer(username=OBJ1.username,password=OBJ1.password,First_Name=OBJ1.First_Name,Last_Name=OBJ1.Last_Name,Email=OBJ1.Email,City=ADD3,Address_Line_1=ADD1,Address_Line_2=ADD2,Contact=OBJ1.Contact,Gender=OBJ1.Gender,PinCode=ADD4)
			Cust.save()
			messages.info(request,"Address Updated!!")
			return redirect('Address_User')
		else:
			messages.info(request,"Please Enter Valid Address")
			return redirect('Address_User')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Houses/Address.html',{'title': 'HouseHelpers-MyAddress','users': OBJ1})


@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def logout(request):
	auth.logout(request)
	return redirect("Web-Home")


def Pass_Reset_UsrAcc(request):
	if request.user.is_authenticated:
		return render(request,'Houses/HomePage.html',{'title': 'HouseHelpers-Home'})
	else:
		if request.method=="POST":
			users1=request.POST['USRNAME_Forget']
			if User.objects.filter(username=users1).exists():
				global FORGOT_USER_NAME
				FORGOT_USER_NAME=users1
				subject="House Helpers"
				messaging = render_to_string('Houses/Email_Format_Password.html',{'USER1': users1,})
				from_email=settings.EMAIL_HOST_USER
				OBJS1=User.objects.get(username=users1)
				TOEMAILS=OBJS1.email
				to_list=[TOEMAILS]
				email_to_send=EmailMessage(subject=subject, body=messaging, from_email=from_email, to=to_list)
				email_to_send.content_subtype = "html"
				email_to_send.send(fail_silently=False)
				return render(request,'Houses/Forgot_Password.html',{'title':'Reset_Password','USER1':users1})
			else:
				messages.info(request,"Username does not exist")
				return redirect('Password_Reset_User')
		else:
			return render(request,'Houses/Username_Password_Reset.html',{'title': 'Reset_Password_User_Details'})



def Pass_Reset(request):
	global FORGOT_USER_NAME
	NAMES_FORGET=FORGOT_USER_NAME
	if request.user.is_authenticated:
		return render(request,'Houses/HomePage.html',{'title': 'HouseHelpers-Home'})
	else:
		if request.method == 'POST':
			P1=request.POST['PASS1']
			P2=request.POST['PASS2']
			if(P1==P2 and Customer.objects.filter(username=FORGOT_USER_NAME).exists()):
				u = User.objects.get(username=NAMES_FORGET)
				u.set_password(P1)
				u.save()
				P1_Real=make_password(P1)
				OBJ1=Customer.objects.get(username=NAMES_FORGET)
				Customs1=Customer(username=OBJ1.username,password=P1_Real,First_Name=OBJ1.First_Name,Last_Name=OBJ1.Last_Name,Email=OBJ1.Email,City=OBJ1.City,Address_Line_1=OBJ1.Address_Line_1,Address_Line_2=OBJ1.Address_Line_2,Contact=OBJ1.Contact,Gender=OBJ1.Gender,PinCode=OBJ1.PinCode)
				Customs1.save()
				messages.info(request,"Password Saved Successfully")
				return redirect('SignIn-User')
			else:
				messages.info(request,"Both Passwords don't match.")
				return redirect('Password_Reset')
		else:
			return render(request,'Houses/Password_Reset.html',{'title':'Reset_Password'})



@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def USR_Problems1(request):
	if request.method=='POST':
		user_req_del=request.user.username
		Activ=request.POST['Act']
		Date_Req=request.POST['Pref_Dt']
		Time_Req=request.POST['Pref_Tm']
		Addr_Req=request.POST['Pref_Addr']
		Pcd_req=request.POST['PCD']
		Desc_req=request.POST['Desc']
		qur_objs=HouseKeeping.objects.get(customer=user_req_del,PinCode=str(Pcd_req),Preferred_Time=Time_Req,Preferred_Date=Date_Req)
		qur_objs.delete()
		return redirect('My-Problems-HK')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		HK = HouseKeeping.objects.filter(customer=username)
		return render(request,'Houses/Problems_Registered.html',{'title':'My Problems','users': OBJ1,'HKS':HK})

@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def USR_Problems2(request):
	if request.method=='POST':
		user_req_del=request.user.username
		Activ=request.POST['Act']
		Date_Req=request.POST['Pref_Dt']
		Time_Req=request.POST['Pref_Tm']
		Addr_Req=request.POST['Pref_Addr']
		Pcd_req=request.POST['PCD']
		Desc_req=request.POST['Desc']
		qur_objs=Salon.objects.get(customer=user_req_del,PinCode=str(Pcd_req),Preferred_Time=Time_Req,Preferred_Date=Date_Req)
		qur_objs.delete()
		return redirect('My-Problems-SL')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		Sals = Salon.objects.filter(customer=username)
		return render(request,'Houses/Problems_Registered.html',{'title':'My Problems','users': OBJ1,'SalsS':Sals})

@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def USR_Problems3(request):
	if request.method=='POST':
		user_req_del=request.user.username
		Activ=request.POST['Act']
		Date_Req=request.POST['Pref_Dt']
		Time_Req=request.POST['Pref_Tm']
		Addr_Req=request.POST['Pref_Addr']
		Pcd_req=request.POST['PCD']
		Desc_req=request.POST['Desc']
		qur_objs=Plumber.objects.get(customer=user_req_del,PinCode=str(Pcd_req),Preferred_Time=Time_Req,Preferred_Date=Date_Req)
		qur_objs.delete()
		return redirect('My-Problems-PL')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		Plumb= Plumber.objects.filter(customer=username)
		return render(request,'Houses/Problems_Registered.html',{'title':'My Problems','users': OBJ1,'PlumbS':Plumb})

@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def USR_Problems4(request):
	if request.method=='POST':
		user_req_del=request.user.username
		Activ=request.POST['Act']
		Date_Req=request.POST['Pref_Dt']
		Time_Req=request.POST['Pref_Tm']
		Addr_Req=request.POST['Pref_Addr'].rstrip()
		Pcd_req=request.POST['PCD']
		Desc_req=request.POST['Desc'].rstrip()
		qur_objs=Electrical.objects.get(customer=user_req_del,PinCode=str(Pcd_req),Preferred_Time=Time_Req,Preferred_Date=Date_Req)
		qur_objs.delete()
		return redirect('My-Problems-EL')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		Elect= Electrical.objects.filter(customer=username)
		return render(request,'Houses/Problems_Registered.html',{'title':'My Problems','users': OBJ1,'ElectS':Elect})


@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def USR_Problems5(request):
	if request.method=='POST':
		user_req_del=request.user.username
		Activ=request.POST['Act']
		Date_Req=request.POST['Pref_Dt']
		Time_Req=request.POST['Pref_Tm']
		Addr_Req=request.POST['Pref_Addr'].rstrip()
		Pcd_req=request.POST['PCD']
		Desc_req=request.POST['Desc'].rstrip()
		qur_objs=Massage.objects.get(customer=user_req_del,Preferred_Time=Time_Req,PinCode=str(Pcd_req),Preferred_Date=Date_Req)
		qur_objs.delete()
		return redirect('My-Problems-MA')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		Mass = Massage.objects.filter(customer=username)
		return render(request,'Houses/Problems_Registered.html',{'title':'My Problems','users': OBJ1,'MassS':Mass})

@login_required(login_url="/SignIn",redirect_field_name="/HomePage")
def USR_Problems6(request):
	if request.method=='POST':
		user_req_del=request.user.username
		Activ=request.POST['Act']
		Date_Req=request.POST['Pref_Dt']
		Time_Req=request.POST['Pref_Tm']
		Addr_Req=request.POST['Pref_Addr']
		Pcd_req=request.POST['PCD']
		Desc_req=request.POST['Desc']
		qur_objs=Trainer.objects.get(customer=user_req_del,PinCode=str(Pcd_req),Preferred_Time=Time_Req,Preferred_Date=Date_Req)
		qur_objs.delete()
		return redirect('My-Problems-TR')
	else:
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		Train = Trainer.objects.filter(customer=username)
		return render(request,'Houses/Problems_Registered.html',{'title':'My Problems','users': OBJ1,'TrainS':Train})



		# ,Description=str(Desc_req),,,,,,,


