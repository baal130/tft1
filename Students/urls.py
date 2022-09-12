from django.conf.urls import include,url
from .views import (
	user_detail,
	
)

app_name = 'Students'

urlpatterns =[
	
	url(r'$',user_detail, name='user_detail'),
	
	
	

	
	
]