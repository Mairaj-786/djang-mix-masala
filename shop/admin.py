from django.contrib import admin
from .models import Department, Student, Book,Reserved_Book
# Register your models here.

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Reserved_Book)