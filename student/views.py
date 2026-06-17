from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeacherCreate, NoticeCreate, BlogCreate, AuthorityCreate, StudentForm, StudentClassCreate
from .models import Blog, Notice, Teacher, Authority, Student, StudentClass
from django.contrib import messages
from django.db.models import Q

# Create your views here.


# dash board 
def dashboard(request):
    return render(request, 'admin/dashboard.html')

# blog views 
def blog_view(request):
    abouts = Blog.objects.all()
    notices = Notice.objects.all()
    teachers = Teacher.objects.all()
    authority = Authority.objects.all()

    context = {
        'principal':teachers.filter(position = "principal").first(),
        'assistance_principal':teachers.filter(position = "Assistant Principal").first(),
        'clerk':teachers.filter(position = "clerk").first(),
        'precident':authority.filter(position = "Precident").first(),
        'accountant':authority.filter(position__icontains = "Accountant").first(),
        'secratory':authority.filter(position__iexact = "Secretary").first(),
        'abouts': abouts,
        'notices':notices,
        
    }
    return render(request, 'home/blog.html', context)


# about add 
def blog_add(request):

    if request.method == 'POST':
        form = BlogCreate(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return redirect('/')   
    else:
        form = BlogCreate()
  
    return render(request, 'blog/b_add.html', {'form':form})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/b_list.html',{'blogs':blogs} )

def blog_details(request, id):
    blog  = get_object_or_404(Blog, id=id)
    
    context = {'blog':blog}
    return render(request, 'blog/b_details.html', context )


def blog_update(request, id):
    blogs = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogCreate(request.POST, request.FILES, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('blog_list')   
    else:
        form = BlogCreate(instance=blogs)

    context = {'form':form, "blogs":blogs}

  
    return render(request, 'blog/b_add.html', context)


def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    if request.method == "POST":
        blog.delete()
        messages.success(request, f"Blog '{blog.title}' deleted successfully!")
        return redirect("blog_list")
    
    return render(request, 'blog/b_delete.html', {'blog': blog})


    # notice


def notice_add(request):
    if request.method == 'POST':
        form = NoticeCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoticeCreate()
    return render(request, 'notice/n_add.html', {'form':form})


def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'notice/n_list.html',{'notices':notices} )



def notice_details(request, id):
    notice  = get_object_or_404(Notice, id=id)
    
    context = {'notice':notice}
    return render(request, 'notice/n_details.html', context )


def notice_update(request, id):
    notice = get_object_or_404(Notice, id=id)
    if request.method == 'POST':
        form = NoticeCreate(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice_list')   
    else:
        form = NoticeCreate(instance=notice)

    context = {'form':form, "notice":notice}

  
    return render(request, 'notice/n_add.html', context) 


def notice_delete(request, id):
    notice = get_object_or_404(Notice, id=id)
    
    if request.method == "POST":
        notice.delete()
        messages.success(request, f"notice '{notice.title}' deleted successfully!")
        return redirect("notice_list")
    
    return render(request, 'notice/n_delete.html', {'notice': notice})


#blog 
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/t_list.html',{'teachers':teachers} )


def teacher_add(request):
    if request.method == 'POST':
        form = TeacherCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherCreate()
    return render(request, 'teacher/t_add.html', {'form':form})

def teacher_details(request, id):
    teacher  = get_object_or_404(Teacher, id=id)
    
    context = {'teacher':teacher}
    return render(request, 'teacher/t_details.html', context )


def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        form = TeacherCreate(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')   
    else:
        form = TeacherCreate(instance=teacher)

    context = {'form':form, "teacher":teacher}
    return render(request, 'teacher/t_add.html', context )


# authority


def authority_add(request):
    if request.method == 'POST':
        form = AuthorityCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorityCreate()
    return render(request, 'authority/a_add.html', {'form':form})


def authority_list(request):
    authorities = Authority.objects.all()
    return render(request, 'authority/a_list.html',{'authorities':authorities} )


def authority_details(request, id):
    authority  = get_object_or_404(Authority, id=id)
    
    context = {'authority':authority}
    return render(request, 'authority/a_details.html', context )


def authority_update(request, id):
    authority = get_object_or_404(Authority, id=id)
    if request.method == 'POST':
        form = AuthorityCreate(request.POST, request.FILES, instance=authority)
        if form.is_valid():
            form.save()
            return redirect('authority_list')   
    else:
        form = AuthorityCreate(instance=authority)

    context = {'form':form, "authority":authority}
    return render(request, 'authority/a_add.html', context )

def student_details(request, student_id):

    student = get_object_or_404(Student, id=student_id)
    
    return render(request, 'student/details.html',{"student":student} )


from django.db.models import Q

def student_list(request):

    search_query = request.GET.get("search", "")
    selected_class = request.GET.get("student_class")

    students = Student.objects.all()

    # Search
    if search_query:
        students = students.filter(
            Q(full_name__icontains=search_query) |
            Q(adhaar_number__icontains=search_query) |
            Q(class_roll__icontains=search_query)
        )

    # Filter by class
    if selected_class:
        students = students.filter(student_class__id=selected_class)

    context = {
        "students": students,
        "search_query": search_query,
        "selected_class": selected_class,
        "student_class": StudentClass.objects.all(),
    }

    return render(request, "student/list.html", context)


def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method =="POST":
        students = StudentForm(request.POST, request.FILES, instance=student)
        if students.is_valid():
            students.save()
            return redirect("student_list")
    else:
         students = StudentForm(instance=student)
    
    return render(request, "student/add.html", {"students":students, "student":student })



    
def student_add(request):
    if request.method =="POST":
        students = StudentForm(request.POST, request.FILES)
        if students.is_valid():
            students.save()
            return redirect("student_list")
    else:
         students = StudentForm()
    
    return render(request, "student/add.html", {"students":students})



#class
def class_add(request):
    if request.method == "POST":
        form = StudentClassCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class added successfully!')
            return redirect('class_add')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentClassCreate()
    
    return render(request, 'classes/c_add.html', {'form': form})

def check(request):
    return render(request, 'bill.html') 