from django.contrib import admin
from .models import Survey, Question, Choice


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date')
    list_filter = ('title',)
    list_display_links = ('title',)
    # list_editable = ('title',)
    search_fields = ('title', 'description')


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
admin.site.register(Choice)


