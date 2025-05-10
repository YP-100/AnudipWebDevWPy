from django.shortcuts import render, redirect
from .models import Customer

# Create a new customer and list all customers
def index(request):
    data = {}
    if request.method == "POST":
        a = request.POST["customer_name"]
        b = request.POST["customer_email"]
        c = request.POST["customer_city"]
        obj = Customer(cname=a, cemail=b, ccity=c)
        obj.save()
    data["record"] = Customer.objects.all()
    return render(request, "index.html", data)

# Update an existing customer
def customer_edit(request, id):
    data = {}
    if request.method == 'POST':
        a = request.POST["customer_name"]
        b = request.POST["customer_email"]
        c = request.POST["customer_city"]
        obj = Customer.objects.get(id=id)
        obj.cname = a
        obj.cemail = b
        obj.ccity = c
        obj.save()
    data["record"] = Customer.objects.get(id=id)
    return render(request, "customer_edit.html", data)

# Delete a customer
def customer_delete(request, id):
    Customer.objects.get(id=id).delete()
    return redirect(index)
