from django.contrib import admin
from pollingapp.models import Question,Choice,Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title",'status','created_by','created_at','updated_at','start_date','end_date')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','text','created_at','updated')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user','choice','created_at','updated_at')
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Answer)
admin.site.register(Question,QuestionAdmin)

