from django.db import models

from django.conf import settings

from constrainedfilefield.fields import ConstrainedFileField,ConstrainedImageField

from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator,MinValueValidator
User = settings.AUTH_USER_MODEL

Course_CHOICES = (
	(_('Tehnološki'), _('Tehnološki')),
	(_('Informatički'),_('Informatički')),
	(_('Matematički'), _('Matematički')),
	
)


def uplodad_location_application(instance, filename):
	
	return "%s/%s" %(instance.application,filename)
def uplodad_location_certificate(instance, filename):
	
	return "%s/%s" %(instance.endcertificate,filename)

class StudentDetails(models.Model):
	#user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	user               =models.OneToOneField(User, on_delete=models.CASCADE) #user.userdetails
	name  =models.CharField(max_length=80,blank=False,null=False,default="Pero") 
	surname  =models.CharField(max_length=80,blank=False,null=False,default="Perice")         
	birthday=models.DateTimeField(auto_now_add=False,auto_now=False)
	placeofbirth=models.CharField(max_length=80,blank=False,null=False,default="Zagreb")
	finishedschool=models.CharField(max_length=80,blank=False,null=False, default="nije zavrsio")
	application=ConstrainedFileField(
						upload_to=uplodad_location_application, null=True,blank=False,
							content_types=[],
							max_upload_size=2621440,#2.5 MB
							js_checker=True,)
	courseselection=models.CharField(max_length=40,choices=Course_CHOICES,default='Informatički',blank=False)
	endcertificate=ConstrainedFileField(
						upload_to=uplodad_location_certificate, null=True,blank=False,
							content_types=[],
							max_upload_size=2621440,#2.5 MB
							js_checker=True,)
	gradeaverage=models.DecimalField(decimal_places=2, max_digits=4, default=3.00,validators=[MaxValueValidator(5),MinValueValidator(0)])
	totalgraduationgrade=models.DecimalField(decimal_places=2, max_digits=4, default=3.00,validators=[MaxValueValidator(5),MinValueValidator(0)])
	
	noteforadmin =models.TextField(blank=True, null=True)
	aproved_by = models.ManyToManyField(User, related_name="aproved")
	approved= models.BooleanField(default=False)
	aproved_date=models.DateTimeField(auto_now=True)

	
	
	
	

	

	# def __unicode__(self):
	#  	return self.name #ono sto se vidi u databasa kad gledamo ( u adminu npr)
	def __str__(self):
		return self.user.username 
	def __unicode__(self):
		return self.user.username 
	def get_full_url(self):
		return self.build_absolute_uri(self.get_absolute_url())
			
	def get_file_object(self):
		if self.application:
			return {
				"url": self.build_absolute_uri(self.application.url),
				
			}	


class CourseManager(models.Manager):
	def new_or_get(self, request):
		qs = self.get_queryset().all()
		qs1=InformaticCourse.objects.all()
		qs2=MathCourse.objects.all()
		print(qs)
		if qs.count() == 1:
			new_obj = False
			course_obj = qs.first()
		   
		else:
			course_obj = TechCourse()
			course_obj.save()

			new_obj = True
			
		if qs1.count() == 1:
			
			courseInformatic_obj = qs1.first()
		   
		else:
			courseInformatic_obj = InformaticCourse()
			courseInformatic_obj.save()

		if qs2.count() == 1:
			
			mathCourse_obj = qs2.first()
		   
		else:
			mathCourse_obj = MathCourse()
			mathCourse_obj.save()	
		return course_obj,courseInformatic_obj,mathCourse_obj, new_obj

	
class TechCourse(models.Model):
	#user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	number       		=models.IntegerField(max_length=10,blank=True,null=True,default=0)
	limit       		=models.IntegerField(max_length=10,blank=False,null=False,default=20)

	objects = CourseManager()
	def __str__(self):
		return str(self.id)
class InformaticCourse(models.Model):
	#user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	number       		=models.IntegerField(max_length=10,blank=True,null=True,default=0)
	limit       		=models.IntegerField(max_length=10,blank=False,null=False,default=120)	
	def __str__(self):
		return str(self.id)
class MathCourse(models.Model):
	#user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	number       		=models.IntegerField(max_length=10,blank=True,null=True,default=0)
	limit       		=models.IntegerField(max_length=10,blank=False,null=False,default=10)	
	def __str__(self):
		return str(self.id)