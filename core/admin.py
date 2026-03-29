from django.contrib import admin
from .models import Question, Option, TestSession, UserResponse, Result

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text_preview', 'test_type', 'trait', 'is_mcq', 'created_at']
    list_filter = ['test_type', 'trait', 'is_mcq', 'created_at']
    search_fields = ['text', 'trait']
    readonly_fields = ['id', 'created_at']
    ordering = ['test_type', 'trait', 'id']
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Question Text'

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_preview', 'text', 'score']
    list_filter = ['score']
    search_fields = ['text', 'question__text']
    ordering = ['question__id', 'id']
    
    def question_preview(self, obj):
        return obj.question.text[:30] + '...' if len(obj.question.text) > 30 else obj.question.text
    question_preview.short_description = 'Question'

@admin.register(TestSession)
class TestSessionAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'current_step', 'is_completed', 'created_at', 'updated_at']
    list_filter = ['current_step', 'is_completed', 'created_at']
    search_fields = ['session_id']
    readonly_fields = ['session_id', 'created_at', 'updated_at']
    ordering = ['-created_at']

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'session', 'question_preview', 'answer_value', 'selected_option', 'created_at']
    list_filter = ['created_at', 'question__test_type', 'question__trait']
    search_fields = ['session__session_id', 'question__text']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    def question_preview(self, obj):
        return obj.question.text[:30] + '...' if len(obj.question.text) > 30 else obj.question.text
    question_preview.short_description = 'Question'

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'session', 'top_domain', 'created_at']
    list_filter = ['top_domain', 'created_at']
    search_fields = ['session__session_id', 'top_domain']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
