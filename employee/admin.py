from django.contrib import admin
from employee.models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','designation','salary')



admin.site.register(Profile,ProfileAdmin)