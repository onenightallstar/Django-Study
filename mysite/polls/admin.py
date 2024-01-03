from django.contrib import admin

from .models import Question

admin.site.register(Question) #注册Question模型

# admin.site 是一个Django自带的管理站点，它可以让你在一个地方管理所有注册的模型。
# admin.site.register(Question)告诉管理站点，Question对象需要被管理。默认情况下，Django为每个模型生成一个表单。