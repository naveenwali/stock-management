from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import *

def index(request):
	if request.method == 'GET':
		return render(request,'dashboard.html')

def add_item(request):
	if request.method == 'GET':
		context={}
		context['supplier'] = Supplier.objects.all()
		context['emp'] = Employee.objects.all()
		context['unit'] = Units.objects.all()
		return render(request,'add_order.html',{'context':context})

	elif request.method == 'POST':
		code = request.POST.get('code')
		name = request.POST.get('name')
		image = request.FILES['image']
		supplier = request.POST.get('supplier')
		emp = request.POST.get('emp')
		unit = request.POST.get('unit')
		item_obj = Items.objects.create(code=code,
										name=name,
										stock=stock,
										image=image,
										supplier=supplier,
										emp=emp,
										unit=unit)
		return HttpResponseRedirect('/add_items/')

def item_list(request):
	item_list = Items.objects.all()
	return render(request,'item_list.html',{'item_lists':item_list})

def supwisecount(request):
	if request.method == 'GET':
		supplier = Supplier.objects.all()
		return render(request,'supplier.html',{'supplier':supplier})

	elif request.method == 'POST':
		name = request.POST.get("name")
		item = Items.objects.filter(supplier__name__icontains=name).count()
		return HttpResponse(content=json.dumps(item), content_type='application/json')

def itemcount(request):
	if request.method == 'GET':
		item = Items.objects.all().values_list('date','name','emp__name').annotate(total= Count('emp__id'))
		return HttpResponse(content=json.dumps(item), content_type='application/json')

