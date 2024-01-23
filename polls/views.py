from http.client import METHOD_NOT_ALLOWED
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from manager.models import Poll, Option
from poll_manager.settings import BASE_DIR
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'templates/index.html')

@csrf_protect
def polls_controller(request):
    if request.method == "GET":
        get_polls(request)
    else:
        return METHOD_NOT_ALLOWED

@csrf_protect
def get_polls(request):
    polls = Poll.objects.all()
    polls_group = []

    for poll_item in polls:
        options = list(Option.objects.filter(poll = poll_item))
        polls_group.append(options)

    return render(request, 'templates/polls.html', 
                  {
                    'result': polls_group
                  })

def get_options(request):
    opt_result = list(Option.objects.all().values)
    return JsonResponse(opt_result, safe=False)

def create_poll(request):
    return render(request, 'templates/create_poll.html')



def get_options_by_pollId(request, pollId):
    poll = get_object_or_404(Poll, id=pollId)
    options = list(Option.objects.filter(poll_id = pollId).values())
    return JsonResponse(options, safe=False)
