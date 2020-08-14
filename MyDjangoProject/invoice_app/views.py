from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime
from invoice_app.models import CustomerModel
from invoice_app.forms import CustomerForm

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


def dashboard(request:HttpRequest):
    return render(request, "invoice/dashboard.html")

def invoices(request:HttpRequest):
    return render(request, "invoice/invoices.html")

def customers(request:HttpRequest):
    records = CustomerModel.objects.all()
    context = {
        "customers": records
    }
    return render(request, "invoice/customers.html", context = context)

def customer_details(request:HttpRequest):
    return render(request, "invoice/customer-details.html")


def customer_delete(request:HttpRequest, id:int = None):

    record = CustomerModel.objects.get(id = id)
    record.delete()

    return redirect("/invoice/customers")


def customer_edit(request:HttpRequest, id: int = None):

    if request.method == "POST":
        if id is None:
            form = CustomerForm(request.POST)
        else:
            record = CustomerModel.objects.get(id = id)
            form = CustomerForm(request.POST, instance=record)

        if form.is_valid():
            form.save(True)
            return redirect("/invoice/customers")
        else:
            #messages.error(request, "Form contains error: " + str(form.errors))
            return render(request, "invoice/customer-edit.html", context={
                "form": form,
                "recordId": id
            })
    else:
        if id is None:
            form = CustomerForm()
        else:
            record = CustomerModel.objects.get(id = id)
            form = CustomerForm(instance=record)

        return render(request, "invoice/customer-edit.html", context={
            "form":  form,
            "recordId": id
        })

def invoice_details(request:HttpRequest):
    return render(request, "invoice/invoice-details.html")

def invoice_edit(request:HttpRequest):
    return render(request, "invoice/invoice-edit.html")