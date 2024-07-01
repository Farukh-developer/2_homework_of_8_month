from django.contrib import admin
from .models import Courses, Teachers, Students
# Register your models here.
admin.site.register([Courses, Teachers, Students])