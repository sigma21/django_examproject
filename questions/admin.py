from django.contrib import admin
from .models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'soru')
    list_display_links = ('id','soru')
    search_fields = ('soru',)
    list_per_page = 25

admin.site.register(Question, QuestionAdmin)