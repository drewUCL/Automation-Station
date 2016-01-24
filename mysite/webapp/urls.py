from django.conf.urls import url
from . import views # . means relative import (import from current package)

#^ start // $ end
urlpatterns = [
	url(r'^$', views.index,name='index') #views is the file; index is the finction it will return
]

 