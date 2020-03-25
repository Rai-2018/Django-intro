from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm,RawProductForm


# Create your views here.

#Creating pure django form
# def product_forms(request):
# 	#default to render the form , can fill in request.get but its probably empty at the start
# 	form = RawProductForm()
# 	#request.POST  --> passing into body of a http response message and send it back
# 	#will validate if the form in the html
# 	if request.method == "POST":
# 		form = RawProductForm(request.POST)
# 		if form.is_valid():
# 			#validate the data, now the data is good
# 			print(form.cleaned_data)
# 			Product.objects.create(**form.cleaned_data)
# 		else:
# 			print(form.errors)
# 	context = {
# 		"form" :form
# 	}
# 	return render(request,"products/products_create.html",context)

# #Create a raw html form - introduction
# def product_forms(request):
# 	#print(request.GET)
# 	#print(request.POST)
# 	if request.method == "POST":
# 		title = request.POST.get("title")
# 		print(title)
# 	context = {}
# 	return render(request,"products/products_create.html",context)


# #Creating a form using ModelForm
def product_forms(request):
	#can initialize form value by specifying a dictionary then append, initial = .. dictionary name
	#to change a obj, find it and save it to variable, append instance = saved obj name
	form  = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form  = ProductForm()
	context = {
		"form" : form
	}
	return render(request,"products/products_create.html",context)


#passing in context and rendering a page
# def product_detail_view(request):
# 	obj = Product.objects.get(id=1)
# 	#context = {
# 	#	"title" : obj.title,
# 	#	"description" : obj.description
# 	#}
# 	context = {
# 		"objects" : obj
# 	}
# 	return render(request,"products/products_detail.html",context)

#dynamic url lookup
def dynamic_lookup_view(request,my_id):
	#does not work if product not exist
	#obj = Product.objects.get(id=my_id)

	#to deal with object not exist
	#First Method
	#obj = get_object_or_404(Product,id=my_id)
	
	#Second method
	try:
		obj = Product.objects.get(id=my_id)
	except Product.DoesNotExist:
		raise Http404


	context = {
		"object":obj
	}
	return render(request,"products/products_detail.html",context)

def product_delete_view(request,my_id):
	obj = get_object_or_404(Product,id = my_id)
	if request.method == "POST":
		obj.delete()
		#redirecting one directory up
		return redirect("../")
	context = {
		"object":obj
	}
	return render(request,"products/products_delete.html",context)

def product_list_all(request):
	queryset = Product.objects.all()
	context = {
		"object" : queryset
	}
	return render(request,"products/products_list.html",context)

