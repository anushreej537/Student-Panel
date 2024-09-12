from django.urls import path
from .models import *
from django.conf import settings
from django.conf.urls.static import static
from teacher_panel import views

urlpatterns = [
    path('tlogin/',views.tlogin),
    path('tlogin_user/',views.tlogin_user),
    path('alltask/',views.alltask),
    path('addtask/',views.addtask),
    path('deletetask/<int:id>/',views.deletetask),
    path('updatetask/<int:id>/',views.updatetask),
    path('update_view/',views.update_view),
    path('tdashboard/',views.tdashboard,name='tdashboard'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)