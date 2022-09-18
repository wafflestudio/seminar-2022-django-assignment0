from django.contrib import admin

from .models import Question, Choice


# Choice 객체가 Question 관리자 페이지에서 편집될 수 있도록 인라인으로 넣어줌.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 여러 개의 필드가 있는 경우 폼을 fieldset으로 분할하는 것이 유리
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# 관리사이트에서 poll app 변경 가능하도록 admin.py에 Question class가 있다고 알려주기
admin.site.register(Question, QuestionAdmin)
