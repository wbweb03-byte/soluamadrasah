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

    class Meta:
        model = Student

        fields = [
            # ======================================================
            # 1. Personal Information
            # ======================================================
            "full_name",
            "img",
            "date_of_birth",
            "gender",
            "blood_group",
            "religion",
            "adhaar_number",

            # ======================================================
            # 2. Guardian Information
            # ======================================================
            "father_name",
            "mother_name",
            "contact",
            "father_adhaar",
            "father_voter",

            # ======================================================
            # 3. Address Information
            # ======================================================
            "village",
            "post_office",
            "police_station",
            "district",
            "state",
            "pin",

            # ======================================================
            # 4. Academic Information
            # ======================================================
            "student_class",
            "class_roll",
            "previous_class",
            "session",
        ]

        labels = {

            # Personal Information
            "full_name": "Student Full Name",
            "img": "Student Photograph",
            "date_of_birth": "Date of Birth",
            "gender": "Gender",
            "blood_group": "Blood Group",
            "religion": "Religion",
            "adhaar_number": "Student Aadhaar Number",

            # Guardian Information
            "father_name": "Father's Full Name",
            "mother_name": "Mother's Full Name",
            "contact": "Mobile Number",
            "father_adhaar": "Father's Aadhaar Number",
            "father_voter": "Father's Voter ID",

            # Address Information
            "village": "Village",
            "post_office": "Post Office",
            "police_station": "Police Station",
            "district": "District",
            "state": "State",
            "pin": "PIN Code",

            # Academic Information
            "student_class": "Current Class",
            "class_roll": "Class Roll",
            "previous_class": "Previous Class",
            "session": "Academic Session",
        }

        widgets = {

            # ======================================================
            # 1. Personal Information
            # ======================================================

            "full_name": forms.TextInput(attrs={
                "placeholder": "Enter student's full name"
            }),

            "img": forms.ClearableFileInput(),

            "date_of_birth": forms.DateInput(attrs={
                "type": "date"
            }),

            "gender": forms.Select(),

            "blood_group": forms.Select(),

            "religion": forms.TextInput(attrs={
                "placeholder": "Religion"
            }),

            "adhaar_number": forms.TextInput(attrs={
                "placeholder": "12-digit Aadhaar Number"
            }),

            # ======================================================
            # 2. Guardian Information
            # ======================================================

            "father_name": forms.TextInput(attrs={
                "placeholder": "Father's full name"
            }),

            "mother_name": forms.TextInput(attrs={
                "placeholder": "Mother's full name"
            }),

            "contact": forms.TextInput(attrs={
                "placeholder": "10-digit Mobile Number"
            }),

            "father_adhaar": forms.TextInput(attrs={
                "placeholder": "Father's Aadhaar Number"
            }),

            "father_voter": forms.TextInput(attrs={
                "placeholder": "Father's Voter ID (Optional)"
            }),

            # ======================================================
            # 3. Address Information
            # ======================================================

            "village": forms.TextInput(attrs={
                "placeholder": "Village"
            }),

            "post_office": forms.TextInput(attrs={
                "placeholder": "Post Office"
            }),

            "police_station": forms.TextInput(attrs={
                "placeholder": "Police Station"
            }),

            "district": forms.TextInput(attrs={
                "placeholder": "District"
            }),

            "state": forms.TextInput(attrs={
                "placeholder": "State"
            }),

            "pin": forms.TextInput(attrs={
                "placeholder": "PIN Code"
            }),

            # ======================================================
            # 4. Academic Information
            # ======================================================

            "student_class": forms.Select(),

            "class_roll": forms.TextInput(attrs={
                "placeholder": "Class Roll Number"
            }),

            "previous_class": forms.TextInput(attrs={
                "placeholder": "Previous Class (Optional)"
            }),

            "session": forms.TextInput(attrs={
                "placeholder": "2026-27"
            }),
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