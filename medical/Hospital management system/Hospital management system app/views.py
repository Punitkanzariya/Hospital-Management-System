from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Appointment
from home.models import Appointment, Facility, Location, Doctor, Staff
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import ListView
#new
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from .models import PatientInquiry
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserCreationForm

from twilio.rest import Client 

User = get_user_model()

def is_superuser(user):
    return user.is_superuser

@login_required(login_url='/login') 
def inquiry_status(request):
    user_inquiries = PatientInquiry.objects.filter(email=request.user.email)
    return render(request, 'inquiry_status.html', {'user_inquiries': user_inquiries})

@user_passes_test(is_superuser, login_url='/login')
def view_inquiries(request):
    read_inquiries = PatientInquiry.objects.filter(is_read=True)
    unread_inquiries = PatientInquiry.objects.filter(is_read=False)
    return render(request, 'view_inquiries.html', {'read_inquiries': read_inquiries, 'unread_inquiries': unread_inquiries})

def mark_inquiry_read(request, inquiry_id):
    inquiry = PatientInquiry.objects.get(pk=inquiry_id)
    inquiry.is_read = True
    inquiry.save()
    return redirect('view_inquiries')

@login_required(login_url='/login') 
def patient_inquiry(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        inquiry_text = request.POST.get('inquiry')

        # Create and save a PatientInquiry object
        patient_inquiry = PatientInquiry(full_name=full_name, email=email, inquiry=inquiry_text)
        patient_inquiry.save()

        messages.success(request, 'Your inquiry has been submitted.')
        return redirect('home')

    return render(request, 'patient_inquiry.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

        else:        
            messages.success(request, 'invalid username or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page
 
#new

# Create your views here.
def index(request):
    #return HttpResponse("this is home page")
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')

def department(request):
    return render(request,'department.html')

def doctor(request):
    return render(request,'doctor.html')

def appointment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        doctor = request.POST.get('doctor')
        department = request.POST.get('department')
        message = request.POST.get('message')
        appointment = Appointment(name=name, email=email, phone=phone,doctor=doctor,department=department,message=message, date=date)
        appointment.save()
        
        messages.success(request, "Your appointment request has been sent successfully. Thank you!")
        name = request.POST['name']
        phone = request.POST['phone']

        # Send SMS using Twilio
        account_sid = 'ACa3f8901f757a1f68aaf7256560cd7cfe'
        auth_token = '78149a7c5ff9d8af353954f17c7ed6b8'
        client = Client(account_sid, auth_token)
        
        sms_body = (
            f"Hello {name}, your appointment has been scheduled.\n"
            f"Appointment Details:\n"
            f"Date: {date}\n"
            f"Department: {department}\n"
            f"Doctor: {doctor}\n"
            f"Message: {message}\n"
            "Thank you for choosing our services."
        )
        
        message = client.messages.create(
            body=sms_body,
            from_="+15188686760",
            to=phone
        )
        

    return render(request, 'appointment.html')

def display_appointments_by_mobile(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('phone')
        appointments = Appointment.objects.filter(phone=mobile_number)
    else:
        appointments = None

    return render(request, 'appointment_template.html', {'appointments': appointments})


def visitor_information(request):
    return render(request, 'visitor_information.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone,message=message, date=datetime.today())
        contact.save()
        
        messages.success(request, "Your message has been sent.")
    return render(request,'contact.html')

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'facility_list.html', {'facilities': facilities})


def location_list(request, facility_id):
    facility = Facility.objects.get(pk=facility_id)
    locations = Location.objects.filter(facility=facility)
    return render(request, 'location_list.html', {'facility': facility, 'locations': locations})

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'

class StaffListView(ListView):
    model = Staff
    template_name = 'staff_list.html'
    context_object_name = 'staff'