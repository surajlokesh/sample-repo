from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
from home.forms import StudentSearchForm,StudentEditModelForm,StudentCreateForm
# def home(request):
#     form=StudentSearchForm()
#     context={'form':form}
#     return render(request,'forms.html',context)
    
from home.models import Student

def home_view(request):
    if request.method=='POST':
        search=StudentSearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            result=Student.objects.filter(student_name=value)
            return render(request,'home.html',{'result':result,'form':StudentSearchForm()})

    else:
        form=StudentSearchForm()
        result=Student.objects.all()
        return render(request,'home.html',{'form':form,'result':result
        })


def deletestudent(request,id):
    result=Student.objects.get(id=id)
    result.delete()
    messages.success(request,'Deleted Sucessfully',)
    return redirect('/')

def edit(request,id):
    result=Student.objects.get(id=id)
    if request.method=='POST':
        ModelForms=StudentEditModelForm(request.POST,instance=result)
        if ModelForms.is_valid():
            ModelForms.save()
            return redirect('/')

    else:
        ModelForm= StudentEditModelForm(instance=result)
        return render(request,'edit.html',{'form':ModelForm})

# def contact(request):
#     return render(request,'home.html')

def CreateStudent(request):
        if request.method=='POST':
                form=StudentCreateForm(request.POST)
                if form.is_valid():
                        student=Student.objects.create(student_name=form.cleaned_data.get('Student_name'),
                        department=form.cleaned_data.get('department'))
                        student.save()
                        messages.success(request,'CREATED SUCESSFULLY')
                        return redirect('/')
        else:
                form=StudentCreateForm()
                return render(request,'create.html',{'form':form})

def home_view1(request):
        return render(request,'testpage.html')