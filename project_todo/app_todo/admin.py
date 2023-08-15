from django.contrib import admin
from .models import taskModel

# Register your models here.
class taskAdminModel(admin.ModelAdmin):
    list_display= ('title','desc','due_date','completed')

admin.site.register(taskModel,taskAdminModel)
