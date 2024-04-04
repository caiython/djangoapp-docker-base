from django.http import HttpResponse, JsonResponse

from . import tasks


# Create your views here.
def index(request):
    return JsonResponse({'Hello': 'world!'})


def celery_hello_world(request: HttpResponse) -> JsonResponse:
    tasks.hello_world.delay()
    return JsonResponse({'Hello': 'world!'})
