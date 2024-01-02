from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
# urlpatterns 是 Python列表，用于定义在 Django项目中应用的路由映射。
# include()函数允许引用其它URLconfs。每当Django遇到include()时，它会截断与此项匹配的URL的部分，并将剩余的字符串发送到URLconf以供进一步处理。
# admin.site.urls 是唯一一个正则表达式，它将admin/开头的URLs映射到Django自带的管理站点。