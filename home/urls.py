from django.contrib import admin
from django.urls import path,include

from home.views import *
from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('', views.index),
    #path('login1',views.login),
    #path('Registration',views.Registration),
    path('assessment',views.assessment),
    path('addQuestion/',views.addQuestion)
    #path('addQuestion/',views.addQuestion,name='addQuestion')
]

#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)