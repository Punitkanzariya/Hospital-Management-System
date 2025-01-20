from django.contrib import admin
from home.models import Contact
from home.models import Appointment, Facility, Location, Doctor, Staff, PatientInquiry

@admin.register(PatientInquiry)
class PatientInquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'timestamp')

admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Facility)
admin.site.register(Location)