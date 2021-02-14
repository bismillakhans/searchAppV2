from django.contrib import admin

# Register your models here.
from colleges.models import NewCollegeBasicInfo

admin.site.register(NewCollegeBasicInfo)
class CollegeAdmin(admin.ModelAdmin):
    fields = ('college_name', )
    ordering = ('id',)