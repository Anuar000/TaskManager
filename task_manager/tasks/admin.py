from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'due_date', 'is_overdue', 'created_at']
    list_filter = ['status', 'created_at', 'due_date']
    search_fields = ['title', 'description']
    list_per_page = 20

    def is_overdue(self, obj):
        return obj.is_overdue

    is_overdue.boolean = True
    is_overdue.short_description = 'Просрочена'