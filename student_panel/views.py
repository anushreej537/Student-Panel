from django.shortcuts import render,redirect
from admin_panel.models import Student
from teacher_panel.models import Teacher_task
from django.contrib import messages


def slogin(request):
    return render(request,'slogin.html')

def slogin_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Student.objects.filter(email=email):
            if Student.objects.filter(password=password):
                messages.error(request,'correct email and password')
                print('hi')
                return redirect('/sdashboard/')
            else:
                return redirect('/slogin/')
        else:
            messages.error(request,'wrong email')
            return redirect('/slogin/')
    else:
        return redirect('/slogin/')


def sdashboard(request):
    task_obj = Teacher_task.objects.all()
    task_count = Teacher_task.objects.all().count()
    return render(request,'sdashboard.html',{'task_obj':task_obj,'task_count':task_count})


def viewtask(request,id):
    task = Teacher_task.objects.get(id=id)
    stu_obj = Student.objects.all()
    return render(request,'sview.html',{'task':task,'stu_obj':stu_obj})

def updateview(request,id):
    id = request.POST['id']
    title = request.POST['title']
    description = request.POST['description']
    status = request.POST['status']
    document = request.FILES['document']
    id = request.POST['student']
    student_id = Student.objects.get(id=id)
    Teacher_task.objects.filter(id=id).update(title=title, description=description, status=status, document=document, student=student_id)
    return redirect('/sdashboard/')