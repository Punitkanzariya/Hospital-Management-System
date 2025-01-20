from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("department",views.department,name='department'),
    path('doctors', views.DoctorListView.as_view(), name='doctor-list'),
    path('staff', views.StaffListView.as_view(), name='staff-list'),
    path("appointment",views.appointment,name='appointment'),
    path('appointments', views.display_appointments_by_mobile, name='display_appointments_by_mobile'),
    path('visitor_information', views.visitor_information, name='visitor_information'),
    path("contact",views.contact,name='contact'),
    path('facility_list', views.facility_list, name='facility_list'),
    path('location_list/<int:facility_id>/', views.location_list, name='location_list'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('patient_inquiry', views.patient_inquiry, name='patient_inquiry'),
    path('view_inquiries', views.view_inquiries, name='view_inquiries'),
    path('mark_read/<int:inquiry_id>/', views.mark_inquiry_read, name='mark_read'),
    path('inquiry_status/', views.inquiry_status, name='inquiry_status'),
]
