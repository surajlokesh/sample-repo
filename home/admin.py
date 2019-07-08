from django.contrib import admin


# Register your models here.

from home.models import Student
from home.models import Library
from home.models import section
from home.models import book
from home.models import Teacher



# admin.site.register(Student)
# admin.site.register(Library)
# admin.site.register(section)
# admin.site.register(book)
# admin.site.register(Teacher)

@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    search_fields=('book',)
    #pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_name','timestamp')
    list_filter=('student_name','department')
    fields=('student_name','department')

@admin.register(section)
class sectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    search_fields=('Library_name','books')
    #pass

