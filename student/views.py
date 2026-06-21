from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import( 
    TeacherCreate,
    NoticeCreate, 
    BlogCreate, 
    AuthorityCreate, 
    StudentForm, 
    StudentClassCreate,
    GalleryImageForm,                  
    LibraryCreate,
    MadrasahDocumentForm,
    PrincipalMassegeForm,
    MadrasahInformationForm,
    RoutineForm)
from .models import (Blog, Notice, 
    Teacher, Authority, 
    Student, StudentClass, 
    GalleryImage,
    Library,
    MadrasahDocuments,
    PrincipalMessage,
    MadrasahInformation,
    Routine
       )
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,  logout 

# Create your views here.

# Login 
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("dashboard")

    return render(request, "admin/login.html")

def user_logout(request):
    logout(request)
    return redirect("login_view")

# dash board 
def pre_dash(request):
    return render(request, 'pre_dash.html')

@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

# blog views 
def blog_view(request):
    abouts = Blog.objects.all()
    notices = Notice.objects.all()
    teachers = Teacher.objects.all()
    authority = Authority.objects.all()
    images = GalleryImage.objects.order_by('-created_at') 
    context = {
        'principal':teachers.filter(position = "principal").first(),
        'assistance_principal':teachers.filter(position = "Assistant Principal").first(),
        'clerk':teachers.filter(position = "clerk").first(),
        'precident':authority.filter(position = "Precident").first(),
        'accountant':authority.filter(position__icontains = "Accountant").first(),
        'secratory':authority.filter(position__iexact = "Secretary").first(),
        'abouts': abouts,
        'notices':notices,
        'images':images,
        
    }
    return render(request, 'home/blog.html', context)


# about add 
@login_required
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

@login_required
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

@login_required
def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    if request.method == "POST":
        blog.delete()
        messages.success(request, f"Blog '{blog.title}' deleted successfully!")
        return redirect("blog_list")
    
    return render(request, 'blog/b_delete.html', {'blog': blog})


    # notice

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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



@login_required
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
@login_required
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


# image add
@login_required
def image_add(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("image_list")
    else:
        form = GalleryImageForm()

    return render(request, "image/image_add.html", {"form": form})
@login_required
def image_update(request, id):
    image = get_object_or_404(GalleryImage, id=id)
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES, instance=image)

        if form.is_valid():
            form.save()
            return redirect("image_list")
    else:
        form = GalleryImageForm(instance=image)

    return render(request, "image/image_add.html", {"form": form})

@login_required
def image_delete(request, id):
    image = get_object_or_404(GalleryImage, id=id)

    if request.method == "POST":
        image.delete()
        return redirect("image_list")

    return render(request,"image/image_delete.html",{"image": image})


def image_list(request):
    images = GalleryImage.objects.order_by("-created_at")
    return render(request,"image/image_list.html",{"images": images})


# library 
@login_required
def library_create(request):
    form = LibraryCreate(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("library_list")

    return render(request, "library/book_add.html", {"form": form})

def library_list(request):
    books = Library.objects.all()
    return render(request, "library/book_list.html", {"books": books})

@login_required
def library_update(request, id):
    book = get_object_or_404(Library, id=id)

    form = LibraryCreate(
        request.POST or None,
        request.FILES or None,
        instance=book
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("library_list")

    return render(request, "library/book_add.html", {"form": form})

@login_required
def library_delete(request, pk):
    book = get_object_or_404(Library, pk=pk)
    book.delete()
    return redirect("library_list")

@login_required
def document_create(request):
    form = MadrasahDocumentForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("document_list")

    return render(request, "dashboard/document/document_form.html", {"form": form})

def document_list(request):
    documents = MadrasahDocuments.objects.all()
    return render(request, "dashboard/document/document_list.html", {"documents": documents})


@login_required
def document_update(request, pk):
    document = get_object_or_404(MadrasahDocuments, pk=pk)

    form = MadrasahDocumentForm(
        request.POST or None,
        request.FILES or None,
        instance=document
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("document_list")

    return render(request, "dashboard/document/document_form.html", {"form": form})


@login_required
def document_delete(request, pk):
    document = get_object_or_404(MadrasahDocuments, pk=pk)
    document.delete()
    return redirect("document_list")


def principal_message(request):
    message = PrincipalMessage.objects.first()

    form = PrincipalMassegeForm(
        request.POST or None,
        request.FILES or None,
        instance=message
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("principal_message")

    return render(request, "dashboard/principal/principal_form.html", {"form": form})


def madrasah_information(request):
    info = MadrasahInformation.objects.first()

    form = MadrasahInformationForm(
        request.POST or None,
        request.FILES or None,
        instance=info
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("about_list")

    return render(request, "about/about_add.html", {"form": form})


def madrasah_information_list(request):
   
    info = MadrasahInformation.objects.first()

    return render( request,"about/about_list.html",{"madrasah_info": info})



def routine_list(request):
    routines = Routine.objects.select_related(
        "teacher",
        "student_class"
    ).order_by("student_class", "period")

    return render(request,"routine/rotine_list.html",{"routines": routines})

@login_required
def routine_create(request):
    RoutineFormSet = modelformset_factory(
        Routine,
        form=RoutineForm,
        extra=1,
        can_delete=True
    )

    if request.method == "POST":
        formset = RoutineFormSet(
            request.POST,
            queryset=Routine.objects.none()
        )

        if formset.is_valid():
            formset.save()
            messages.success(request, "Routines added successfully.")
            return redirect("routine_list")

    else:
        formset = RoutineFormSet(
            queryset=Routine.objects.none()
        )

    return render(request,"routine/rotine.html", {"formset": formset})


@login_required
def routine_edit(request, id):
    routine = get_object_or_404(Routine, id=id)

    if request.method == "POST":
        form = RoutineForm(request.POST, instance=routine)

        if form.is_valid():
            form.save()
            messages.success(request, "Routine updated successfully.")
            return redirect("routine_list")

    else:
        form = RoutineForm(instance=routine)

    return render(request,"routine/rotine.html",{"form": form})

@login_required
def routine_delete(request, pk):
    routine = get_object_or_404(Routine, pk=pk)

    if request.method == "POST":
        routine.delete()
        messages.success(request, "Routine deleted successfully.")
        return redirect("routine_list")

    return render(
        request,
        "routine/routine_delete.html",
        {"routine": routine}
    )
