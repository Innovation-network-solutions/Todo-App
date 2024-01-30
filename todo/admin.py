from django.contrib import admin
from .models import Todo


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'completed', 'created')
    search_fields = ['task']


admin.site.register(Todo, TaskAdmin)
