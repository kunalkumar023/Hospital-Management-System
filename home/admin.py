from django.contrib import admin
from .models import doctor,patient,appoint,bills
# Register your models here.

admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(appoint)
admin.site.register(bills)