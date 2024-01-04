from django.contrib import admin

from .models import Question,Choice

# admin.site 是一个Django自带的管理站点，它可以让你在一个地方管理所有注册的模型。
# admin.site.register(Question)告诉管理站点，Question对象需要被管理。默认情况下，Django为每个模型生成一个表单。

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
# StackedInline表示以块的形式展示，TabularInline表示以表格的形式展示
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"] #过滤器 侧边栏
    search_fields = ["question_text"] #搜索框
    # (名称，{字段})元组的列表，每个元组都表示一个字段集。
    # inlines = [ChoiceInline]表示在Question的编辑页面中嵌入Choice模型的编辑页面
    # list_display = ["question_text", "pub_date", "was_published_recently"]表示在Question的列表页面中显示哪些字段


admin.site.register(Question, QuestionAdmin)
# QuestionAdmin类继承自admin.ModelAdmin类，它包含了一些选项，这些选项告诉Django：“在管理对象的页面上，显示哪些字段？”

admin.site.register(Choice)