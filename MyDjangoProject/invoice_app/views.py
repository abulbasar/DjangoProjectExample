from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
# Example handling url parameters
def home_page(request:HttpRequest):
    names = request.GET.getlist("name") # multiple value for same url name
    department = request.GET.get("department")
    context = {
        "names": names,
        "department": department,
        "time": datetime.now()
    }
    return render(request, "index.html", context = context)

def ping(request:HttpRequest):
    #return HttpResponse("Hello world!")
    now = datetime.now()
    return JsonResponse({"message": "hello world"
                            , "current_time": str(now)})