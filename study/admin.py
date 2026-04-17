from django.contrib import admin
from .models import Study

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'study_date',
        'hours',
        'minutes',
        'created_at',
    )
    list_filter = ('category', 'study_date')
    search_fields = ('title', 'memo')
    ordering = ('-study_date', '-created_at')