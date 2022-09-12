from django.shortcuts import render
from .models import StudentDetails,TechCourse,InformaticCourse,MathCourse
from .forms import StudentDetailsForm
from allauth.account.decorators import verified_email_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
# Create your views here.
def home(request):
	
	
	context={
		
		
	}

		
	
	return render(request,"landing.html",context) #first page


@verified_email_required
@login_required
def user_detail(request):
	if not request.user.is_authenticated:
		raise Http404
	user_detail_instance=StudentDetails.objects.filter(user=request.user) #  instanca od detalja 
	# Institate frist time or just get objects
	course_obj,courseInformatic_obj,mathCourse_obj, new_obj = TechCourse.objects.new_or_get(request)

	print (courseInformatic_obj)
	print(new_obj)
	if user_detail_instance.exists():    # means alreday filled once this table  
		user_detail_instance=StudentDetails.objects.get(user=request.user)
	
		verificated=False
		title="Prijava je zaprimljena  "
		form= StudentDetailsForm( request.POST or None, request.FILES or None,instance=user_detail_instance ) #instance of the form
		
		
		
		
		if form.is_valid(): 
			user_detail_instance=form.save(commit=False)
			user_detail_instance.user=request.user
			if(user_detail_instance.courseselection=="Tehnološki"):
				course_obj.number+=1
				course_obj.save()
				print(course_obj.number)
			print(user_detail_instance.courseselection)

			user_detail_instance.save()
			messages.success(request,_('Vaša prijava je zaprimljena'),extra_tags='')#message.tag salje sve tagove(npr sucess + extra tag) i loppa kao charachter stringa
			
				
		if form.errors:
			messages.error(request, _('Oprostite,dogodila se greška probajte ponovno'),extra_tags='')
		
			   
		context={
		"form":form,
		"instance":user_detail_instance,
		"verificated":verificated,
		"title":title,
		"course_obj":course_obj,
		"courseInformatic_obj":courseInformatic_obj,
		"mathCourse_obj":mathCourse_obj,
		} 
	else:
		title="Popunite prijavu za fakultet"
		form= StudentDetailsForm( request.POST or None, request.FILES ) 

		if form.is_valid(): 
			user_detail_instance=form.save(commit=False)
			user_detail_instance.user=request.user
			if(user_detail_instance.courseselection=="Tehnološki"):
				if(course_obj.limit!=course_obj.number):
					course_obj.number+=1
					course_obj.save()
				
					user_detail_instance.save()
					messages.success(request,_('Vaša prijava je zaprimljena'),extra_tags='')
				else:
					messages.error(request, _('Limit smjera, upisite drugi smjer'),extra_tags='')
			if(user_detail_instance.courseselection=="Informatički"):
				if(courseInformatic_obj.limit!=courseInformatic_obj.number):
					courseInformatic_obj.number+=1
					courseInformatic_obj.save()
				
					user_detail_instance.save()
					messages.success(request,_('Vaša prijava je zaprimljena'),extra_tags='')
				else:
					messages.error(request, _('Limit smjera, upisite drugi smjer'),extra_tags='')
			if(user_detail_instance.courseselection=="Matematički"):
				if(mathCourse_obj.limit!=mathCourse_obj.number):
					mathCourse_obj.number+=1
					mathCourse_obj.save()
				
					user_detail_instance.save()
					messages.success(request,_('Vaša prijava je zaprimljena'),extra_tags='')
				else:
					messages.error(request, _('Limit smjera, upisite drugi smjer'),extra_tags='')		
		context={
		 "form":form,
		
		"title":title,
		"course_obj":course_obj,
		"courseInformatic_obj":courseInformatic_obj,
		"mathCourse_obj":mathCourse_obj,
		} 



	
	return render(request,"user_detail.html",context)