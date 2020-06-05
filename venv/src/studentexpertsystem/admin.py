from django.contrib import admin
from .models import Groups,Boards,Courses, DetailModel
# Register your models here.

admin.site.register(Groups)
admin.site.register(Boards)
admin.site.register(Courses)
admin.site.register(DetailModel)
