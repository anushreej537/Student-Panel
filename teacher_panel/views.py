from django.shortcuts import render,redirect
from .models import Teacher_task
from admin_panel.models import Teacher,Student
from django.contrib import messages

def tlogin(request):
    return render(request,'tlogin.html')

def tlogin_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Teacher.objects.filter(email = email):
           if Teacher.objects.filter(password=password):
               messages.error(request,'your email and password are correct..')
               print('hi')
               return redirect('/tdashboard/')
           else:
               messages.error(request,'your email and password are wrong..')
               print('hello')
               return redirect('/tlogin/')
        else:
            return redirect('/tlogin/')
    else:
        return redirect('/tlogin/')
               

def alltask(request):
    task_obj = Teacher_task.objects.all()
    stu_obj = Student.objects.all()
    return render(request,'task.html',{'task_obj':task_obj,'stu_obj':stu_obj})

def addtask(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        document = request.FILES['document']
        student_id = request.POST['student']
        student = Student.objects.get(id=student_id)
        Teacher_task.objects.create(
            title=title, 
            description=description, 
            status='Incomplete',  # Default status
            document=document, 
            student=student
        )
        return redirect('/alltask/')
    else:
        return render(request, 'task.html')



def deletetask(request,id):
    obj = Teacher_task.objects.get(id=id)
    obj.delete()
    return redirect('/alltask/')

def updatetask(request,id):
    t_obj = Teacher_task.objects.get(id=id)
    stu_obj = Student.objects.all()
    print(t_obj)
    return render(request,'tupdate.html',{'t_obj':t_obj,'stu_obj':stu_obj})

def update_view(request):
    id = request.POST['id']
    title = request.POST['title']
    description = request.POST['description']
    status = request.POST['status']
    document = request.FILES['document']
    id = request.POST['student']
    student_id = Student.objects.get(id=id)
    Teacher_task.objects.filter(id=id).update(title=title, description=description, status=status, document=document, student=student_id)
    return redirect('/alltask/')
    

def tdashboard(request):
    task_count = Teacher_task.objects.all().count()
    student_count = Student.objects.all().count()
    return render(request,'tdashboard.html',{'task_count':task_count,'student_count':student_count})