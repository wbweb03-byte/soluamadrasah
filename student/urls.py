from django.urls import path
from . import views
urlpatterns = [

    #dashboard
    path('dashboard/',views.dashboard, name='dashboard'),
    path('pre_dash/',views.pre_dash, name='pre_dash'),
    # login
   
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

    #image
    path('image/add/', views.image_add, name='image_add'),
    path('image/list/', views.image_list, name='image_list'),
    path('image/update/<int:id>/', views.image_update, name='image_update'),
    path('image/delete/<int:id>/', views.image_delete, name='image_delete'),

    # check

    # Library
    path("library/", views.library_list, name="library_list"),
    path("library/add/", views.library_create, name="library_create"),
    path("library/<int:id>/edit/", views.library_update, name="library_update"),
    path("library/<int:pk>/delete/", views.library_delete, name="library_delete"),

    # Documents
    path("documents/", views.document_list, name="document_list"),
    path("documents/add/", views.document_create, name="document_create"),
    path("documents/<int:pk>/edit/", views.document_update, name="document_update"),
    path("documents/<int:pk>/delete/", views.document_delete, name="document_delete"),

    # Principal
    path("principal-message/", views.principal_message, name="principal_message"),

    # Madrasah Information
    path("about_list/", views.madrasah_information_list, name="about_list"),
    path("about_add/", views.madrasah_information, name="about_add"),
     # routine 
    path("routine/", views.routine_list, name="routine_list"),
    path("routine/add/", views.routine_create, name="routine_create"),
    path("routine/<int:id>/edit/", views.routine_edit, name="routine_edit"),
    path("routine/<int:pk>/delete/", views.routine_delete, name="routine_delete"),
    path('admit/', views.student_admit, name='student_admit'),
    path(
    "student/<int:pk>/admit-card/",
    views.student_admit_card,
    name="student_admit_card",
    ),
    path(
    "student/admit/bulk/",
    views.bulk_admit_card,
    name="bulk_admit_card",
    ),
    path(
    "student/register/<int:pk>/",
    views.student_register,
    name="student_register",
    ),

    # login

    path("login/", views.user_login, name="login_view"),
    path("logout/", views.user_logout, name="logout"),

]
