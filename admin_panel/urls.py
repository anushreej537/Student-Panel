from django.urls import path
from . views import *
from admin_panel.api.api import *

urlpatterns = [
    path("", signup,name='signup'),
    path("create_user/", create_user,),
    path("login/",login,name='login'),
    path("login_user/",login_user,name='login_user'),
    path("addcourse/",addcourse,name='addcourse'),
    path('courses/',courses,name='courses'),
    path('updatecourse/<int:id>/',updatecourse,name='updatecourse'),
    path('course_view/',course_view,name='course_view'),
    path('deletecourses/<int:id>/',delete_courses,name='deletecourses'),
    path('dashboard/',dashboard,name='dashboard'),
    path('studentdetails/',studentdetails,name='studentdetails'),
    path('students/',students,name='students'),
    path('updatestudents/<int:id>/',update_students,name='updatestudents'),
    path('update_view/',update_view,name='update_view'),
    path('deletestudents/<int:id>/',delete_students,name='deletestudents'),
    path('searchstudent/',searchstudent,name='searchstudent'),
    path('teachers/',teachers,name='teachers'),
    path('addteachers/',addteachers,name='addteachers'),
    path('updateteacher/<int:id>/',update_teacher,name='updatetaecher'),
    path('teacher_view/',teacher_view,name='teacherview'),
    path('deleteteachers/<int:id>/',delete_teachers,name='deletetechers'),
    path('searchteacher/',searchteacher,name='searchteacher'),
    path('index/',index,name='index'),

    # api urls
    path('adminreg/',RegistrationViewSet.as_view()),
    path('showadmin/',RegistrationShowViewSet.as_view()),
    path('regcourse/',CourseViewSet.as_view()),
    path('showcourse/',CourseShowViewSet.as_view()),
    path('regstudent/',StudentViewSet.as_view()),
    path('showstudent/',StudentShowViewSet.as_view()),
    path('updatestudent/<int:id>/',UpdateStudentViewSet.as_view()),
    path('deletestudent/<int:id>/',DeleteStudentViewSet.as_view()),
    path('deletestu/<int:id>/',DestroyStudentViewSet.as_view())
]

