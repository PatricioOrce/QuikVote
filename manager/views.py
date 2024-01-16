from django.http import HttpResponse
from manager.models import Poll, Option
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def new_poll(request):
    if request.method == 'POST':
        description = request.POST["description"]
        print(description)
        return HttpResponse("<h2 style='color: green;'>Here you´ll create your polls</h2>")
        