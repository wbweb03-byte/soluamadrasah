from django.urls import path
from . import views
urlpatterns = [

    #dashboard
     path('dashboard/',views.dashboard, name='dashboard'),

    path('',views.blog_view, name='blogs' ),
    #blog
    path('blog_add/',views.blog_add, name='blog_add' ),
    path('blog_list/',views.blog_list, name='blog_list' ),
    path('blog_details/<int:id>/',views.blog_details, name='blog_details' ),
    path('blog_update/<int:id>/',views.blog_update, name='blog_update' ),
    path('blog_delete/<int:id>/',views.blog_delete, name='blog_delete' ),
    

    # notice 
    path('notice_add/',views.notice_add, name='notice_add' ),
    path('notice_list/',views.notice_list, name='notice_list' ),
    path('notice_details/<int:id>/',views.notice_details, name='notice_details' ),
    path('notice_update/<int:id>/',views.notice_update, name='notice_update' ),
    path('notice_delete/<int:id>/',views.notice_delete, name='notice_delete' ),


    # teacher
    path('teacher_add/',views.teacher_add, name='teacher_add' ),
    path('teacher_list/',views.teacher_list, name='teacher_list' ),
    path('teacher_details/<int:id>/',views.teacher_details, name='teacher_details' ),
    path('teacher_update/<int:id>/',views.teacher_update, name='teacher_update' ),

    # authority

    path('authority_add/',views.authority_add, name='authority_add' ),
    path('authority_list/',views.authority_list, name='authority_list' ),
    path('authority_details/<int:id>/',views.authority_details, name='authority_details' ),
    path('authority_update/<int:id>/',views.authority_update, name='authority_update' ),
    
    #student 
    path('student_list/', views.student_list, name='student_list'),
    path('student/details/<int:student_id>/', views.student_details, name='student_details'),
    path('student/update/<int:id>/', views.student_update, name='student_update'),
    path('student/add/', views.student_add, name='student_add'),

    #class 
    path('studentclass/add/', views.class_add, name='class_add'),

    # check

    path('check/',views.check, name='check' ),

]
