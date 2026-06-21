from django import forms
from .models import (Blog, 
                     Notice, Teacher, 
                     Authority, Student, 
                     StudentClass, GalleryImage, 
                     Library, MadrasahDocuments,
                       MadrasahInformation, PrincipalMessage,
                    Routine)



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



INPUT_CLASS = "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
TEXTAREA_CLASS = "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
FILE_CLASS = "block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-blue-600 file:text-white hover:file:bg-blue-700"


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["title", "img"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Enter image title"
            }),
            "img": forms.FileInput(attrs={
                "class": FILE_CLASS
            }),
        }


class LibraryCreate(forms.ModelForm):
    class Meta:
        model = Library
        fields = ["b_name", "b_img", "author", "desc"]
        widgets = {
            "b_name": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Book Name"
            }),
            "author": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Author Name"
            }),
            "desc": forms.Textarea(attrs={
                "class": TEXTAREA_CLASS,
                "rows": 4,
                "placeholder": "Book Description"
            }),
            "b_img": forms.FileInput(attrs={
                "class": FILE_CLASS
            }),
        }


class MadrasahDocumentForm(forms.ModelForm):
    class Meta:
        model = MadrasahDocuments
        fields = ["title", "document_img", "desc"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Document Title"
            }),
            "desc": forms.Textarea(attrs={
                "class": TEXTAREA_CLASS,
                "rows": 4,
                "placeholder": "Document Description"
            }),
            "document_img": forms.FileInput(attrs={
                "class": FILE_CLASS
            }),
        }


class PrincipalMassegeForm(forms.ModelForm):
    class Meta:
        model = PrincipalMessage
        fields = ["title", "description", "admission_message"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Message Title"
            }),
            "description": forms.Textarea(attrs={
                "class": TEXTAREA_CLASS,
                "rows": 5,
                "placeholder": "Principal Message"
            }),
            "admission_massege": forms.Textarea(attrs={
                "class": TEXTAREA_CLASS,
                "rows": 5,
                "placeholder": "Admission Message"
            }),
        }


class MadrasahInformationForm(forms.ModelForm):
    class Meta:
        model = MadrasahInformation
        fields = [
            "m_ests",
            "m_about",
            "m_course",
            "m_vision",
            "m_phone",
            "m_email",
            "m_logo",
            "m_name",
        ]
        widgets = {
            "m_name": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Madrasah Name"
            }),
            "m_phone": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Phone Number"
            }),
            "m_email": forms.EmailInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Email Address"
            }),
            "m_ests": forms.TextInput(attrs={
                "class": INPUT_CLASS,
                "placeholder": "Established Year"
            }),
            "m_about": forms.Textarea(attrs={
                "class": TEXTAREA_CLASS,
                "rows": 4,
                "placeholder": "About Madrasah"
            }),
            "m_course": forms.Textarea(attrs={
                "class": TEXTAREA_CLASS,
                "rows": 4,
                "placeholder": "Courses"
            }),
            "m_vision": forms.Textarea(attrs={
                "class": TEXTAREA_CLASS,
                "rows": 4,
                "placeholder": "Vision"
            }),
            "m_logo": forms.FileInput(attrs={
                "class": FILE_CLASS
            }),
        }


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = "__all__"

        widgets = {
            "teacher": forms.Select(attrs={
                "class": "w-full border rounded-lg p-2"
            }),

            "student_class": forms.Select(attrs={
                "class": "w-full border rounded-lg p-2"
            }),

            "subject": forms.TextInput(attrs={
                "class": "w-full border rounded-lg p-2",
                "placeholder": "Enter Subject"
            }),

            "period": forms.NumberInput(attrs={
                "class": "w-full border rounded-lg p-2",
                "placeholder": "Enter Period"
            }),
        }