from django.urls import path
from student_panel import views

urlpatterns = [
    path('slogin/',views.slogin,name='slogin'),
    path('sdashboard/',views.sdashboard, name='sdashboard'),
    path('slogin_user/',views.slogin_user,name='sloginuser'),
    path('viewtask/<int:id>/',views.viewtask,name='viewtask'),
    path('updateview/<int:id>/',views.updateview),
]
