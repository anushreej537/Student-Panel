from django.shortcuts import render,redirect
from .models import User,Course,Student,Teacher
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

def signup(request):
    return render(request,'signup.html')

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email = email).exists():
            messages.error(request,'email already exist')
        else:
            User.objects.create(name=name, email=email, password=password)
            return render(request,'login.html')
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email):
            if User.objects.filter(password=password):
                return redirect('/dashboard/')
            else:
                messages.error(request,'Wrong password')
        else:
            return redirect('/')
    else:
        return redirect('/')
    
def addcourse(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        fees = request.POST['fees']
        duration = request.POST['duration']
        if Course.objects.filter(course_name = course_name).exists():
            messages.error(request,'course name already exist')
        else:
            Course.objects.create(course_name = course_name,fees = fees,duration = duration)
            messages.success(request,'course added successfully')
            return redirect('/courses/')
    
def courses(request):
    course_obj = Course.objects.all()
    return render(request,'courses.html',{'course_obj':course_obj})

def updatecourse(request,id):
    course_obj = Course.objects.get(id=id)
    return render(request,'updatecourse.html',{'course_obj':course_obj})

def course_view(request):
    id = request.POST['id']
    course_name = request.POST['course_name']
    fees = request.POST['fees']
    duration = request.POST['duration']
    Course.objects.filter(id = id).update(course_name=course_name, fees=fees, duration=duration)
    return redirect('/courses/')

def delete_courses(request,id):
    delcourse = Course.objects.get(id = id)
    delcourse.delete()
    return redirect('/courses/')


def dashboard(request):
    obj = Course.objects.all().count()
    course_obj = Course.objects.all()
    totalstu = Student.objects.all().count()
    return render(request,'dashboard.html',{'obj':obj, 'course_obj':course_obj, 'totalstu':totalstu})

def studentdetails(request):
    course_obj = Course.objects.all()
    student_obj = Student.objects.all()
    return render(request,'students.html',{'course_obj':course_obj,'student_obj':student_obj})

def students(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenum = request.POST['phonenum']
        address = request.POST['address']
        degree = request.POST['degree']
        college = request.POST['college']
        totalamount = request.POST['totalamount']
        paidamount = request.POST['paidamount']
        dueamount = request.POST['dueamount']
        course_id = request.POST['course']
        stu_course = Course.objects.get(id=course_id)
        password = request.POST['password']
        if Student.objects.filter(email = email).exists():
            messages.error(request,'email already exist')
            return redirect('/studentdetails/')

        elif Student.objects.filter(phonenum=phonenum).exists():
            messages.error(request,'phonenum already exist')
            return redirect('/studentdetails/')

        else:
            Student.objects.create(name=name , email=email, phonenum=phonenum, 
                                   address=address, degree=degree, college=college,
                                     totalamount=totalamount,paidamount=paidamount,
                                     dueamount=dueamount,course=stu_course,password=password)
            return redirect('/studentdetails/')
    else:
        return render(request,'students.html')
        
def update_students(request,id):
    studata = Student.objects.get(id=id)
    coursedata = Course.objects.all()
    return render(request,'updatestudent.html',{'studata':studata, 'coursedata':coursedata})

def update_view(request):
    id = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']
    phonenum = request.POST['phonenum']
    address = request.POST['address']
    degree = request.POST['degree']
    college = request.POST['college']
    totalamount = request.POST['totalamount']
    paidamount = request.POST['paidamount']
    dueamount = request.POST['dueamount']
    course_id = request.POST['course']
    stucourse = Course.objects.get(id = course_id)
    Student.objects.filter(id=id).update(name=name, email=email, phonenum=phonenum, 
                                        address=address, degree=degree, college=college, 
                                        totalamount=totalamount, paidamount=paidamount,
                                        dueamount=dueamount, course = stucourse)
    return redirect('/students/')

def delete_students(request,id):
    delstu = Student.objects.get(id = id)
    delstu.delete()
    return redirect('/studentdetails/')

def searchstudent(request):
    if 'q' in request.GET:
        q = request.GET['q']

        multiple_q = Q(name__istartswith=q)
        student_obj = Student.objects.filter(multiple_q)
        print(student_obj)
        return render(request,'students.html',{'student_obj':student_obj})
    else:
        student_obj = Student.objects.all()
        return render(request,'students.html',{'student_obj':student_obj})

        
def teachers(request):
    allteacher = Teacher.objects.all()
    allcourse = Course.objects.all()
    return render(request,'teachers.html',{'allteacher':allteacher,'allcourse':allcourse})

def addteachers(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenum = request.POST['phonenum']
        course_id = request.POST['course']
        password = request.POST['password']
        
        teacher_course = Course.objects.get(id=course_id)
        
        # Check if the email or phone number already exists
        if Teacher.objects.filter(email=email).exists():
            messages.error(request, 'Teacher email already exists')
            return render(request, 'teachers.html')  # Return the form with an error message
        elif Teacher.objects.filter(phonenum=phonenum).exists():
            messages.error(request, 'Phone number already exists')
            return render(request, 'teachers.html')  # Return the form with an error message
        else:
            # Create the teacher and redirect to dashboard
            Teacher.objects.create(name=name, email=email, phonenum=phonenum, course=teacher_course, password=password)
            messages.success(request, 'Teacher added successfully')
            return redirect('/teachers/')  # Redirect to the dashboard on success
    
    # If request method is GET or no post data, show the form page
    return render(request, 'teachers.html')

def update_teacher(request,id):
    teacher_data = Teacher.objects.get(id=id)
    course_data = Course.objects.all()
    return render(request,'updateteacher.html',{'teacher_data':teacher_data, 'course_data':course_data})

def teacher_view(request):
    id = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']
    phonenum = request.POST['phonenum']
    Teacher.objects.filter(id=id).update(name=name, email=email, phonenum=phonenum)
    return redirect('/teachers/')

def delete_teachers(request,id):
    delteacher = Teacher.objects.get(id=id)
    delteacher.delete()
    return redirect('/teachers/')

def searchteacher(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(name__istartswith=q)
        allteacher = Teacher.objects.filter(multiple_q)
        return render(request,'teachers.html',{'allteacher':allteacher})
    else:
        allteacher = Student.objects.all()
        return render(request,'teachers.html',{'allteacher':allteacher})

def profile(request):
    return render(request,'profile.html')

def index(request):
    return render(request,'dashboard.html')