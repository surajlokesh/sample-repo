from django import forms
from home.models import Student

class StudentSearchForm(forms.Form):
    q=forms.CharField(label='',
    widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30',
    'placeholder':'Serach'}))

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        #student_name,department we will give
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Student_Name'}),
            'department':forms.Select(attrs={'class':'cutom-select'})
        }

class StudentCreateForm(forms.Form):
    Student_name=forms.CharField(label='',
    widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'student_name'}))
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))