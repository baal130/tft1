from django.contrib import admin

# Register your models here.
from .models import StudentDetails,TechCourse,InformaticCourse,MathCourse

class StudentDetailsAdmin(admin.ModelAdmin):
	list_display=["__unicode__","user"]
	#list_filter=["timestamp"]
	search_fields =["placeofbirth",'birthday','user']
	class Meta:
		model=StudentDetails
admin.site.register(StudentDetails,StudentDetailsAdmin)
admin.site.register(TechCourse)
admin.site.register(InformaticCourse)
admin.site.register(MathCourse)