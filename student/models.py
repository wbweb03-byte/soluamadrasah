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

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='student/')

    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)

    adhaar_number = models.CharField(max_length=12, validators=[aadhaar_validator])

    date_of_birth = models.DateField()

    father_adhaar = models.CharField( max_length=12,validators=[aadhaar_validator])

    father_voter = models.CharField(max_length=100, blank=True,null=True)

    village = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100)
    police_station = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    pin = models.CharField(max_length=6, validators=[pin_validator])

    admission_date = models.DateField(auto_now_add=True)

    student_class = models.ForeignKey("StudentClass",  on_delete=models.CASCADE)
    class_roll = models.CharField(max_length=10)

    previous_class = models.CharField(max_length=10,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name