from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

# blog section 
class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    img = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Teacher(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    qualification = models.CharField(max_length=150)
    contact = models.CharField(max_length=15)
    img = models.ImageField(upload_to='teachers/profile/')
    documents = models.FileField(upload_to='teachers/documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.name
    

class Authority(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    qualification = models.CharField(max_length=150)
    contact = models.CharField(max_length=15)
    img = models.ImageField(upload_to='authorities/profile/')
    documents = models.FileField(upload_to='authorities/documents/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =  ['name']
        verbose_name = 'Authority'
        verbose_name_plural = 'Authorities'

    def __str__(self):
        return self.name

class StudentClass(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name


aadhaar_validator = RegexValidator(
        regex=r'^\d{12}$',
        message='Aadhaar number must contain exactly 12 digits.'
    )

pin_validator = RegexValidator(
        regex=r'^\d{6}$',
        message='PIN code must contain exactly 6 digits.'
    )

phone_validator = RegexValidator(
            regex=r'^[6-9]\d{9}$',
            message="Enter a valid 10-digit mobile number."
        )

contact = models.CharField(
        max_length=10,
        unique=True,
        validators=[phone_validator],
    )

class Student(models.Model):

    # ======================================================
    # 1. Personal Information
    # ======================================================

    full_name = models.CharField(max_length=200)

    img = models.ImageField(upload_to="student/")

    date_of_birth = models.DateField()

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default="male",
    )

    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES,
        blank=True,
        null=True,
    )

    religion = models.CharField(
        max_length=30,
        default="Islam",
    )

    adhaar_number = models.CharField(
        max_length=12,
        validators=[aadhaar_validator],
    )

    # ======================================================
    # 2. Guardian Information
    # ======================================================

    father_name = models.CharField(max_length=200)

    mother_name = models.CharField(max_length=200)

    contact = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
        validators=[phone_validator],
    )

    father_adhaar = models.CharField(
        max_length=12,
        validators=[aadhaar_validator],
    )

    father_voter = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    # ======================================================
    # 3. Address Information
    # ======================================================

    village = models.CharField(max_length=100)

    post_office = models.CharField(max_length=100)

    police_station = models.CharField(max_length=100)

    district = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    pin = models.CharField(
        max_length=6,
        validators=[pin_validator],
    )

    # ======================================================
    # 4. Academic Information
    # ======================================================

    student_class = models.ForeignKey(
        "StudentClass",
        on_delete=models.CASCADE,
    )

    class_roll = models.CharField(max_length=10)

    previous_class = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    session = models.CharField(
        max_length=9,
        default="2026-27",
    )

    # ======================================================
    # 5. Registration & System Information
    # ======================================================

    admission_no = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    registration_no = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    admission_date = models.DateField(
        auto_now_add=True,
    )

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("registered", "Registered"),
        ("inactive", "Inactive"),
        ("tc", "Transfer Certificate"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.full_name
    
   


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title or self.img.name


class MadrasahInformation(models.Model):
    
    m_ests = models.IntegerField(default=1977)
    m_about = models.TextField(max_length=1000)
    m_course = models.TextField(max_length=1000)
    m_vision = models.TextField(max_length=1000)
    m_phone = models.CharField(max_length=13)
    m_email = models.EmailField(default="soluamadrasahaofficial12@gmail.com")
    m_logo = models.ImageField(upload_to='logo/')
    m_name = models.CharField(max_length=200, default="Solua Madrasah Darul Quran")
   

    def __str__(self):
        return self.m_name

class PrincipalMessage(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField()

    admission_message = models.TextField()

    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class MadrasahDocuments(models.Model):
    title = models.CharField(max_length=200)
    document_img = models.ImageField(upload_to="mad_docu/")
    desc = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)    

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Madrasah Document"
        verbose_name_plural = "Madrasah Documents"

    def __str__(self):
        return self.title


class Library(models.Model):
    b_name = models.CharField(max_length=200)
    b_img = models.ImageField(upload_to="books/")
    author = models.CharField(max_length=300)
    desc = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Library"
        verbose_name_plural = "Libraries"

    def __str__(self):
        return self.b_name
    

class Routine(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="routines")

    student_class = models.ForeignKey(StudentClass,on_delete=models.CASCADE,related_name="routines")

    subject = models.CharField(max_length=100)
    period = models.PositiveIntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["student_class", "period"],name="unique_class_period")]

    def __str__(self):
        return f"{self.student_class.name} - Period {self.period} - {self.subject}"