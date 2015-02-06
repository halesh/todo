# Create your views here.
#from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
import datetime 
from todo.models import Tasks

def home_page(request, home_template):
    today =  datetime.date.today()
    if request.method == 'POST':
        task_obj = Tasks()
        task_obj.task_name = request.POST['task_name']
        task_obj.task_desc = request.POST['description']
        task_obj.priority = request.POST['priority']
        task_obj.due_date = request.POST['due_date']
        task_obj.save()
    tasks = Tasks.objects.all()
    return render_to_response(home_template, {'tasks':tasks, 'today':today})

def change_todo(request, state, todo_id=None):
    if state == "Delete":
        task = Tasks.objects.get(id=todo_id)
        task.delete()
    else:
        task = Tasks.objects.get(id=todo_id)
        task.task_state = state
        task.save()
    return HttpResponseRedirect("/home/")

def filter_todo(request, date_filter_type):
    today =  datetime.date.today()
    if date_filter_type == "Today":
        tasks = Tasks.objects.filter(created_on=today)
    elif date_filter_type == "Week":
        tasks = Tasks.objects.filter(created_on=today)
    if date_filter_type == "Month":
        tasks = Tasks.objects.filter(created_on=today)

    return render_to_response('home.html', {'tasks':tasks, 'today':today})
