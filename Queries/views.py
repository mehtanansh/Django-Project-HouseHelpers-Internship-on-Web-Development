from django.shortcuts import render, redirect
from django.contrib import messages
from Houses.models import Customer
from django.utils import timezone
from .forms import Form1,Form3,Form4,Form5,Form6,Form2
from .models import Electrical,HouseKeeping,Massage,Plumber,Trainer,Salon
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/SignIn/")
def Electrical_Fault(request):
	if request.method == 'POST':
		form = Form1(request.POST)
		if form.is_valid():
			Service_date=request.POST['Avail_date']
			Service_time=request.POST['Avail_time']
			Service_Addr=(request.POST['Addr_Service'])
			PC=str(request.POST['PinCode'])
			LEN1=len(PC)
			if(LEN1!=6):
				form = Form1()
				username = request.user.username
				OBJ1=Customer.objects.get(username=username)
				messages.info(request,"Enter a valid PinCode for the Address!!")
				return render(request,'Queries/Base_Form.html',{'title': 'Electrical_Fault','Form1':form,'Cust':OBJ1})
			now=timezone.now()
			USRNM=request.user.username
			Instant = Customer.objects.get(username=USRNM)
			Electric=Electrical(customer=Instant,Needed_For=form.cleaned_data['Needed_For'],Device=form.cleaned_data['Device'],Preferred_Date=str(Service_date),Preferred_Time=str(Service_time),Address_of_Service=Service_Addr,PinCode=PC,Date_of_Complaint=now,Description=form.cleaned_data['Description'])
			Electric.save()
			return redirect('Form-Completion-Request')
	else:
		form = Form1()
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Queries/Base_Form.html',{'title': 'Electrical_Fault','Form1':form,'Cust':OBJ1})



@login_required(login_url="/SignIn/")
def Housekeeping_Request(request):
	if request.method == 'POST':
		form = Form2(request.POST)
		if form.is_valid():
			Service_date=request.POST['Avail_date']
			Service_time=request.POST['Avail_time']
			Service_Addr=request.POST['Addr_Service']
			PC=str(request.POST['PinCode'])
			LEN1=len(PC)
			if(LEN1!=6):
				form = Form2()
				username = request.user.username
				OBJ1=Customer.objects.get(username=username)
				messages.info(request,"Enter a valid PinCode for the Address!!")	
				return render(request,'Queries/Base_Form.html',{'title': 'Housekeeping_Request','Form2':form,'Cust':OBJ1})			
			now=timezone.now()
			USRNM=request.user.username
			Instant = Customer.objects.get(username=USRNM)
			HouseKeep=HouseKeeping(customer=Instant,Activity=form.cleaned_data['Activity'],Preferred_Date=str(Service_date),Preferred_Time=str(Service_time),Address_of_Service=Service_Addr,PinCode=PC,Date_of_Complaint=now,Description=form.cleaned_data['Description'])
			HouseKeep.save()
			return redirect('Form-Completion-Request')
	else:
		form = Form2()
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Queries/Base_Form.html',{'title': 'Housekeeping_Request','Form2':form,'Cust':OBJ1})



@login_required(login_url="/SignIn/")
def Massage_Request(request):
	if request.method == 'POST':
		form = Form3(request.POST)
		if form.is_valid():
			Service_date=str(request.POST['Avail_date'])
			Service_time=str(request.POST['Avail_time'])
			Service_Addr=request.POST['Addr_Service']
			PC=str(request.POST['PinCode'])
			LEN1=len(PC)
			if(LEN1!=6):
				form = Form3()
				username = request.user.username
				OBJ1=Customer.objects.get(username=username)
				messages.info(request,"Enter a valid PinCode for the Address!!")	
				return render(request,'Queries/Base_Form.html',{'title': 'Massage_Request','Form3':form,'Cust':OBJ1})
			now=timezone.now()
			USRNM=request.user.username
			Instant = Customer.objects.get(username=USRNM)
			Mass=Massage(customer=Instant,Needed_For=form.cleaned_data['Needed_For'],Preferred_Date=str(Service_date),Preferred_Time=str(Service_time),Address_of_Service=Service_Addr,PinCode=PC,Date_of_Complaint=now,Description=form.cleaned_data['Description'])
			Mass.save()
			return redirect('Form-Completion-Request')
	else:
		form = Form3()
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Queries/Base_Form.html',{'title': 'Massage_Request','Form3':form,'Cust':OBJ1})



@login_required(login_url="/SignIn/")
def Plumbing_Fault(request):
	if request.method == 'POST':
		form = Form4(request.POST)
		if form.is_valid():
			Service_date=request.POST['Avail_date']
			Service_time=request.POST['Avail_time']
			Service_Addr=request.POST['Addr_Service']
			PC=str(request.POST['PinCode'])
			LEN1=len(PC)
			if(LEN1!=6):
				form = Form4()
				username = request.user.username
				OBJ1=Customer.objects.get(username=username)
				messages.info(request,"Enter a valid PinCode for the Address!!")	
				return render(request,'Queries/Base_Form.html',{'title': 'Plumbing_Fault','Form4':form,'Cust':OBJ1})	
			now=timezone.now()
			USRNM=request.user.username
			Instant = Customer.objects.get(username=USRNM)
			Plum=Plumber(customer=Instant,Problem_Type=form.cleaned_data['Problem_Type'],Preferred_Date=str(Service_date),Preferred_Time=str(Service_time),PinCode=PC,Date_of_Complaint=now,Address_of_Service=Service_Addr,Description=form.cleaned_data['Description'])
			Plum.save()
			return redirect('Form-Completion-Request')
	else:
		form = Form4()
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Queries/Base_Form.html',{'title': 'Plumbing_Fault','Form4':form,'Cust':OBJ1})




@login_required(login_url="/SignIn/")
def Trainer_Request(request):
	if request.method == 'POST':
		form = Form5(request.POST)
		if form.is_valid():
			Service_date=request.POST['Avail_date']
			Service_time=request.POST['Avail_time']
			Service_Addr=request.POST['Addr_Service']
			PC=str(request.POST['PinCode'])
			LEN1=len(PC)
			if(LEN1!=6):
				form = Form5()
				username = request.user.username
				OBJ1=Customer.objects.get(username=username)
				messages.info(request,"Enter a valid PinCode for the Address!!")	
				return render(request,'Queries/Base_Form.html',{'title': 'Trainer_Request','Form5':form,'Cust':OBJ1})
			now=timezone.now()
			USRNM=request.user.username
			Instant = Customer.objects.get(username=USRNM)
			Train=Trainer(customer=Instant,Needed_For=form.cleaned_data['Needed_For'],Activity=form.cleaned_data['Activity'],Preferred_Date=str(Service_date),Preferred_Time=str(Service_time),Address_of_Service=Service_Addr,PinCode=PC,Date_of_Complaint=now,Description=form.cleaned_data['Description'])	
			Train.save()
			return redirect('Form-Completion-Request')
	else:
		form = Form5()
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Queries/Base_Form.html',{'title': 'Trainer_Request','Form5':form,'Cust':OBJ1})



@login_required(login_url="/SignIn/")
def Salon_Request(request):
	if request.method == 'POST':
		form = Form6(request.POST)
		if form.is_valid():
			Service_date=request.POST['Avail_date']
			Service_time=request.POST['Avail_time']
			Service_Addr=request.POST['Addr_Service']
			PC=str(request.POST['PinCode'])
			LEN1=len(PC)
			if(LEN1!=6):
				form = Form6()
				username = request.user.username
				OBJ1=Customer.objects.get(username=username)
				messages.info(request,"Enter a valid PinCode for the Address!!")	
				return render(request,'Queries/Base_Form.html',{'title': 'Salon_Request','Form6':form,'Cust':OBJ1})
			now=timezone.now()
			USRNM=request.user.username
			Instant = Customer.objects.get(username=USRNM)
			Sallu=Salon(customer=Instant,Needed_For=form.cleaned_data['Needed_For'],Activity=form.cleaned_data['Activity'],Preferred_Date=str(Service_date),Preferred_Time=str(Service_time),Address_of_Service=Service_Addr,PinCode=PC,Date_of_Complaint=now,Description=form.cleaned_data['Description'])
			Sallu.save()
			return redirect('Form-Completion-Request')
	else:
		form = Form6()
		username = request.user.username
		OBJ1=Customer.objects.get(username=username)
		return render(request,'Queries/Base_Form.html',{'title': 'Salon_Request','Form6':form,'Cust':OBJ1})



@login_required(login_url="/SignIn/")
def Form_Submitted(request):
	return render(request,'Queries/Display_Form_Submitted.html',{'title': 'Form-Submitted'})