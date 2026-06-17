from django import forms
from .models import Blog, Notice, Teacher, Authority, Student, StudentClass


class BlogCreate(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["title", "desc", "img"]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Enter blog title',
                'autocomplete': 'off'
            }),

            'desc': forms.Textarea(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Write blog description...',
                'rows': 6
            }),

            'img': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'title': 'Blog Title',
            'desc': 'Description',
            'img': 'Upload Image'
        }

        help_texts = {
            'img': 'Upload JPG, PNG or JPEG image'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters long."
            )

        return title



class NoticeCreate(forms.ModelForm):

    class Meta:
        model = Notice

        fields = ['title', 'desc']

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Enter notice title',
                'autocomplete': 'off'
            }),

            'desc': forms.Textarea(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Write notice description...',
                'rows': 5
            }),

        }

        labels = {
            'title': 'Notice Title',
            'desc': 'Description',
            'date': 'Publish Date'
        }

        help_texts = {
            'title': 'Maximum 100 characters'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters long."
            )

        return title



class TeacherCreate(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = [
            'name',
            'position',
            'qualification',
            'contact',
            'img',
            'documents',
            'is_active'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter teacher name'
            }),

            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter position'
            }),

            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter qualification'
            }),

            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }



class AuthorityCreate(forms.ModelForm):

    class Meta:
        model = Authority
        fields = [
            'name',
            'position',
            'qualification',
            'contact',
            'img',
            'documents',
            'is_active'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter teacher name'
            }),

            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter position'
            }),

            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter qualification'
            }),

            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }



class StudentForm(forms.ModelForm):
    """Simple form for Student model"""
    
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'full_name': 'Student Full Name',
            'img': 'Student Photograph',
            'father_name': "Father's Full Name",
            'mother_name': "Mother's Full Name",
            'adhaar_number': 'Aadhaar Number (12 digits)',
            'date_of_birth': 'Date of Birth',
            'father_adhaar': "Father's Aadhaar Number",
            'father_voter': "Father's Voter ID Card Number",
            'village': 'Village Name',
            'post_office': 'Post Office Name',
            'police_station': 'Police Station Name',
            'district': 'District Name',
            'state': 'State Name',
            'pin': 'PIN Code (Postal Code)',
            'admission_date': 'Admission Date',
            'student_class': 'Current Class',
            'class_roll': 'Roll Number in Class',
            'previous_class': 'Previous Class Attended',
            'created_at': 'Registration Date & Time',
        }


        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter father's name"}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter mother's name"}),
            'adhaar_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12-digit Aadhaar number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'father_adhaar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Father's 12-digit Aadhaar"}),
            'father_voter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Father's Voter ID (optional)"}),
            'village': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Village name'}),
            'post_office': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post office name'}),
            'police_station': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Police station name'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District name'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State name'}),
            'pin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '6-digit PIN code'}),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
            'class_roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Roll number'}),
            'previous_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Previous class (optional)'}),
        }

class StudentClassCreate(forms.ModelForm):

    class Meta:
        model = StudentClass
        fields = ["name"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter class name'})
        }