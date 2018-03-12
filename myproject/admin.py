from django.contrib import admin
from .models import *

# Register your models here.

class TrucksAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'from_location', 'to_location', 'capacity', 'scheduled_date', 'posted_by', 'truck_type', 'distance', 'approx_travelling_time', 'truck_image',]
    exclude = ['post_id',]
    class Meta:
        model = Truck

admin.site.register(Truck, TrucksAdmin)


class LoadsAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'from_location', 'to_location', 'capacity', 'scheduled_date', 'posted_by', 'truck_type', 'distance', 'approx_travelling_time', 'truck_image',]
    exclude = ['post_id',]
    class Meta:
        model = Load

admin.site.register(Load, LoadsAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
	class Meta:
		model = Enrollment

admin.site.register(Enrollment, EnrollmentAdmin)

admin.site.register(Fm16)
