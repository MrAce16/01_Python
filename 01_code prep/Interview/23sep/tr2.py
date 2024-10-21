# create CRUD 
# ip address (strng) and  need to create 3 field tenant & status: 
# tenant name : techstar and status : active


from django.shortcuts import redirect, render
from .forms import OrderForm
from .models import Orders
from django.db import models

url = [path('Crud', admin.urls),path['/api/ipam/create',include('/api/ipam/create')]]

# Crud 
#Post method
class post(models.Model):
    def orderFormView(request):
        form = OrderForm()
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show_url')
        template_name = 'crudapp/order.html'
        context = {'form': form}
        return render(request, template_name, context)

#Delete

def deleteView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)

#update

def updateView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

#Read

def showView(request):
    obj = Orders.objects.all()
    template_name = 'crudapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)