from django.contrib import admin
from .models import Question, Account_Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'answer')
    list_display_links = ('id','text', 'answer')
    search_fields = ('text',)
    list_per_page = 25

class Account_QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'user_answer')
    list_display_links = ('question','user', 'user_answer')
    search_fields = ('id',)
    list_per_page = 25


admin.site.register(Question, QuestionAdmin)
admin.site.register(Account_Question, Account_QuestionAdmin)