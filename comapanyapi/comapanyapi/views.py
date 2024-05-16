from django.http import HttpResponse, JsonResponse



def home_page(request):
    print('hello')
    friends=[
        'bharat',
        'yadsav',
        'ravi'
    ]
    #return HttpResponse("this is home page")
    return JsonResponse(friends, safe=False)
