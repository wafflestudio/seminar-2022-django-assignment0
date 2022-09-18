from typing import List

from django import http, shortcuts, urls
from django.template import loader
from django.utils import timezone
from django.views import generic
from polls import models


def index(request: http.HttpRequest) -> http.HttpResponse:
    # Normal
    # template = loader.get_template("polls/index.html")
    # return http.HttpResponse(template.render(context, request))

    # ShortCut
    latest_question_list = models.Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return shortcuts.render(request, "polls/index.html", context)


def detail(request: http.HttpRequest, question_id: int) -> http.HttpResponse:
    # Normal
    # try:
    #     question = models.Question.objects.get(pk=question_id)
    # except models.Question.DoesNotExist:
    #     raise http.Http404("Question does not exist")

    # ShortCut
    question = shortcuts.get_object_or_404(models.Question, pk=question_id)
    context = {"question": question}
    return shortcuts.render(request, "polls/detail.html", context)


def results(request: http.HttpRequest, question_id: int) -> http.HttpResponse:
    question = shortcuts.get_object_or_404(models.Question, pk=question_id)
    context = {"question": question}
    return shortcuts.render(request, "polls/results.html", context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> List:
        return models.Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = models.Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return models.Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = "polls/results.html"


def vote(request: http.HttpRequest, question_id: int) -> http.HttpResponse:
    question = shortcuts.get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice: models.Choice = question.choice_set.get(
            pk=request.POST["choice"]
        )
    except (KeyError, models.Choice.DoesNotExist):
        error_context = {
            "question": question,
            "error_message": "You didn't select a choice",
        }
        return shortcuts.render(request, "polls/detail.html", error_context)
    selected_choice.votes += 1
    selected_choice.save()
    return http.HttpResponseRedirect(urls.reverse("polls:results", args=(question.id,)))
