from django.db import models

# Create your models here.

class Contact(models.Model):

	fullname = models.CharField(max_length=200, null=True, blank=True)
	lastname = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	subject = models.CharField(max_length=200, null=True, blank=True)
	message = models.CharField(max_length=200, null=True, blank=True)
	
	def __unicode__(self):
        	return self.fullname






class Truck(models.Model):
	loading = "Loading"
	unloading = "Unloading"
	unpacking = "Unpacking"
    	truck_choices = ((loading, "Loading"), (unloading, "Unloading"), (unpacking, "Unpacking"))
	post_id = models.CharField(max_length=200, null=True, blank=True)
	from_location = models.CharField(max_length=200, null=True, blank=True)
	to_location = models.CharField(max_length=200, null=True, blank=True)
	capacity = models.CharField(max_length=200, null=True, blank=True)
	scheduled_date = models.DateField(null=True, blank=True)
	posted_by = models.CharField(max_length=200, null=True, blank=True)
	truck_type = models.CharField(max_length=200, choices=truck_choices, null=True, blank=True)
	distance = models.CharField(max_length=200, null=True, blank=True)
	approx_travelling_time = models.CharField(max_length=200, null=True, blank=True)
	truck_image = models.ImageField(null=True, blank=True)
	
	def __unicode__(self):
        	return self.post_id
    	class Meta:
        	verbose_name_plural = 'Truck Details'
    
    	def calc_truck_id(self, x):
        	tnames = "TRUCK"
        	truck = tnames
        
        	post_id = truck +  str(self.id)
        	print "truck id is :", post_id
        	return post_id.upper()

    	def save(self, *args, **kwargs):
        	super(Truck, self).save(*args, **kwargs)
        	self.post_id = self.calc_truck_id(self)
        	super(Truck, self).save(*args, **kwargs)


class Load(models.Model):
	loading = "Loading"
	unloading = "Unloading"
	unpacking = "Unpacking"
    	truck_choices = ((loading, "Loading"), (unloading, "Unloading"), (unpacking, "Unpacking"))
	post_id = models.CharField(max_length=200, null=True, blank=True)
	from_location = models.CharField(max_length=200, null=True, blank=True)
	to_location = models.CharField(max_length=200, null=True, blank=True)
	capacity = models.CharField(max_length=200, null=True, blank=True)
	scheduled_date = models.DateField(null=True, blank=True)
	posted_by = models.CharField(max_length=200, null=True, blank=True)
	truck_type = models.CharField(max_length=200,choices=truck_choices, null=True, blank=True)
	distance = models.CharField(max_length=200, null=True, blank=True)
	approx_travelling_time = models.CharField(max_length=200, null=True, blank=True)
	truck_image = models.ImageField(null=True, blank=True)
	
	def __unicode__(self):
        	return self.post_id
    	class Meta:
        	verbose_name_plural = 'Load Details'
    
    	def calc_load_id(self, x):
        	tnames = "LOAD"
        	load = tnames
        
        	post_id = load +  str(self.id)
        	print "load id is :", post_id
        	return post_id.upper()

    	def save(self, *args, **kwargs):
        	super(Load, self).save(*args, **kwargs)
        	self.post_id = self.calc_load_id(self)
        	super(Load, self).save(*args, **kwargs)

			
class Fm16(models.Model):
	gate1 = "Gate1"
	gate2 = "Gate2"
	gate3 = "Gate3"
    	gate_choices = ((gate1, "Gate1"), (gate2, "Gate2"), (gate3, "Gate3"))
		
			
	
	gate = models.CharField(max_length=200,choices=gate_choices, null=True, blank=True)
	vehicle_no = models.CharField(max_length=200, null=True, blank=True)
	vehicle_load =  models.CharField(max_length=200, null=True, blank=True)
	comments = models.TextField(null=True, blank=True)
	
	g_salary = models.CharField(max_length=200, null=True, blank=True)
	p_tax = models.CharField(max_length=200, null=True, blank=True)
	i_tax_paid = models.CharField(max_length=200, null=True, blank=True)
	bank_interest = models.CharField(max_length=200, null=True, blank=True)
	us_17_2 = models.CharField(max_length=200, null=True, blank=True)
	us_17_3 = models.CharField(max_length=200, null=True, blank=True)
	other_income = models.CharField(max_length=200, null=True, blank=True)
	gpf = models.CharField(max_length=200, null=True, blank=True)
	
	ppf = models.CharField(max_length=200, null=True, blank=True)
	gis = models.CharField(max_length=200, null=True, blank=True)
	lic = models.CharField(max_length=200, null=True, blank=True)
	pli = models.CharField(max_length=200, null=True, blank=True)
	edu_expense = models.CharField(max_length=200, null=True, blank=True)
	hbl_principal = models.CharField(max_length=200, null=True, blank=True)
	mf = models.CharField(max_length=200, null=True, blank=True)
	nsc = models.CharField(max_length=200, null=True, blank=True)
	
	sukanya = models.CharField(max_length=200, null=True, blank=True)
	other_savings_name = models.CharField(max_length=200, null=True, blank=True)
	other_savings = models.CharField(max_length=200, null=True, blank=True)
	mediclaim = models.CharField(max_length=200, null=True, blank=True)
	edu_loan = models.CharField(max_length=200, null=True, blank=True)
	hbl_interest = models.CharField(max_length=200, null=True, blank=True)
	donation = models.CharField(max_length=200, null=True, blank=True)
	other_80_name_1 = models.CharField(max_length=200, null=True, blank=True)
	
	other_80_1 = models.CharField(max_length=200, null=True, blank=True)
	other_80_name_2 = models.CharField(max_length=200, null=True, blank=True)
	other_80_2 = models.CharField(max_length=200, null=True, blank=True)
	house_rent_exempt = models.CharField(max_length=200, null=True, blank=True)
	us_10_14 = models.CharField(max_length=200, null=True, blank=True)
	tax_relief_89 = models.CharField(max_length=200, null=True, blank=True)
	relief_80ccc = models.CharField(max_length=200, null=True, blank=True)
	relief_80ccd = models.CharField(max_length=200, null=True, blank=True)
	
	name_employee = models.CharField(max_length=200, null=True, blank=True)
	desig_employee = models.CharField(max_length=200, null=True, blank=True)
	pan_employee = models.CharField(max_length=200, null=True, blank=True)
	name_employer = models.CharField(max_length=200, null=True, blank=True)
	desig_employer = models.CharField(max_length=200, null=True, blank=True)
	tan_employer = models.CharField(max_length=200, null=True, blank=True)
	pan_employer = models.CharField(max_length=200, null=True, blank=True)
	date_employer_sign = models.CharField(max_length=200, null=True, blank=True)
        office_address = models.TextField(null=True, blank=True)
	place_employer_sign = models.CharField(max_length=200, null=True, blank=True)
	name_employer_father = models.CharField(max_length=200, null=True, blank=True)

        def __unicode__(self):
           return unicode(self.first_name) or u''	
	
##	def __unicode__(self):
##        	return self.first_name
## 


class Enrollment(models.Model):

	canter_jumbo = "Canter Jumbo"
    	canters_mt = "Canters 7.5MT/ 6 Wheel"
    	containers_truck = "Containers Truck"
    	lowbed_trailer = "Low Bed Trailer"
	multiaxle_trailer = "Mulit Axle Trailer"
    	truck_choices = ((canter_jumbo, "Canter Jumbo"), (canters_mt, "Canters 7.5MT/ 6 Wheel"), (containers_truck, "Containers Truck"), (lowbed_trailer, "Low Bed Trailer"), (multiaxle_trailer, "Mulit Axle Trailer"))
	name = models.CharField(max_length=200, null=True, blank=True)
	phone1 = models.CharField(max_length=200, null=True, blank=True)
	phone2 = models.CharField(max_length=200, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	aadhar_card = models.CharField(max_length=16)
	vehicle_no = models.CharField(max_length=10, null=True, blank=True)
	vehicle_type = models.CharField(max_length=200, choices=truck_choices, null=True, blank=True)
	attach_files = models.ImageField(null=True, blank=True)
	driving_license = models.CharField(max_length=30, null=True, blank=True)
	cbook = models.CharField(max_length=30, null=True, blank=True)

	def __unicode__(self):
        	return self.name
	class Meta:
        	verbose_name_plural = 'Enrollment'

