from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5] template = loader.get_template('polls/index.html') context = {'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context.request))

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5] output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	reponse = "You're looking at the results of question %s."
	return HttpResponse(reponse % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)