from django.urls import path
from . import views

app_name = "polls" #防止不同应用有同名的url
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
# as_view()函数将类视图转换成函数视图
# 类视图：将视图逻辑写在类中，类视图的优点是可以继承，可以重写父类的方法，可以使用多重继承
# 函数视图： 将视图逻辑写在函数中，函数视图的优点是简单，逻辑清晰
# 因为url()函数只接受函数视图，不接受类视图，所以要把类视图转换成函数视图