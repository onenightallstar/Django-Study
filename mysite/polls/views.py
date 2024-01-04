from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
#pub_data__lte=timezone.now()表示pub_date小于等于当前时间
#generic.ListView是一个通用视图，它帮助我们减少重复代码，因为它将常见的模式抽象化了

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
#默认使用App名/模型名_detail.html作为模板文件
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list]) #join()函数将列表中的元素以指定的字符连接生成一个新的字符串
    template = loader.get_template("polls/index.html") #loader.get_template()函数加载polls/index.html模板文件并返回一个Template对象
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request)) 
    #template.render()函数将context字典传入模板文件中，返回一个包含模板内容的字符串
    #template.render(context, request)中request的作用是将request对象传入模板文件中，以便在模板文件中使用request对象中的一些属性 

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    #selected_choice 代表用户选择的选项
    #pk=request.POST["choice"] 代表用户选择的选项的id
    #如果没有choice会引发KeyError异常
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    # reverse()函数返回一个url arg代表参数
    # question.id,是为了将其视为元组，而不是一个整数