from django import forms
from django.conf import settings
from .models import StudentDetails
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from datetime import date

from bootstrap_datepicker_plus import DatePickerInput

class StudentDetailsForm(forms.ModelForm):
	"""
	User-related CRUD form
	"""
	birthday=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,widget=DatePickerInput(),label=_('Datum rođenja'),required=False)
	
	class Meta:
		model = StudentDetails
		
		
		fields = [
			'name',
			'surname',
			'birthday',
			'placeofbirth',
			'finishedschool',
			#'billing_profile',
			'application',
			'courseselection',
			'endcertificate',
			'gradeaverage',
			'totalgraduationgrade',
			
			
		]
		labels = {'name': _('Ime'),
				  'surname': _('Prezime'),
				  'birthday': _('Dan,Mjesec i godina rođenja'),
				  'placeofbirth': _('Mjesto i adresa rođenja '),
				  'finishedschool': _('Ime završene škole'),
				  'application': _('Molba za upis na smjer'),
				  'courseselection': _('Izaberite jedan od smjerova'),
				  'endcertificate': _('Učitajte certifikat završene škole'),
				  'gradeaverage': _('Upišite prosjek ocjena'),
				  'totalgraduationgrade': _('Ocjena na maturi'),
				 
				 
				  
				

		}       
		error_messages = {
			'finishedschool': {
				# for example:
				'required': _("Morate upisati završenu školi"),
				'blank': _("This writer's name is too leng."),
			},
		}        
	# def __init__(self, *args, **kwargs):
	# 	super(AddressForm, self).__init__(*args, **kwargs)
	# 	self.fields['OIB'].error_messages = {'required': 'custom required message', 'max_length': 'custom required message'}    	
		