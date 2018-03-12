from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from myproject.models import *
from myproject.forms import *
from django.db.models import Q
# Create your views here.

def index(request):
    context_dict = {}
    return render(request, 'home.html', context_dict)

def form(request):
    context_dict = {}
    return render(request, 'form.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'about.html', context_dict)

def enrollment(request):
    context_dict = {}
    return render(request, 'enrollment.html', context_dict)

def contact_form(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        #print "request post : ", request.POST
        if contact_form.is_valid():
            contact = contact_form.save()
            done = True
        else:
            "sorry "
            print contact_form.errors
    else:
        contact_form = ContactForm()
    return render_to_response('contact.html',
     {'contact_form': contact_form,
     'done': done}, context)
	 
	 
@login_required	 
def fm16(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        fm16_form = Fm16Form(data=request.POST)
        #print "request post : ", request.POST
        if fm16_form.is_valid():
            fm16 = fm16_form.save()
            done = True
        else:
            "sorry "
            print fm16_form.errors
    else:
        fm16_form = Fm16Form()
    return render_to_response('fm16.html',
     {'fm16_form': fm16_form,
     'done': done}, context)
	 

@login_required
def enrollment_form(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        enrollment_form = EnrollmentForm(data=request.POST)
        #print "request post : ", request.POST
        if enrollment_form.is_valid():
            enroll = enrollment_form.save()
            done = True
        else:
            "sorry "
            print enrollment_form.errors
    else:
        enrollment_form = EnrollmentForm()
    return render_to_response('enrollment.html',
     {'enrollment_form': enrollment_form,
     'done': done}, context)


@login_required
def search(request):
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    
    trucks = Truck.objects.filter(Q(post_id__icontains = q) | Q(from_location__icontains=q))
    loads =  Load.objects.filter(Q(post_id__icontains = q) | Q(from_location__icontains=q))
    trucks_from = Truck.objects.filter(Q(from_location__icontains = q) & Q(to_location__icontains=q))
    loads_from = Load.objects.filter(Q(from_location__icontains = q) & Q(to_location__icontains=q))	
    
    return render_to_response('search.html', {'trucks': trucks,'loads':loads,'trucks_from':trucks_from, 'loads_from':loads_from, 'category': q}, context)
