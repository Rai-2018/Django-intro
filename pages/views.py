from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#*args allow to pass as many as parameters
#**kwargs allow keyworded parameters, etc.. name = yasuo
#one of the parameters passed is request and it has request.user
	#Can be used for authentication
def home_view(request,*args,**kwargs):
	#bad to just return one line --> use django template
	#return HttpResponse("<h1>Hello World</h1>") #string of html code

	#should be return render(request,templatename,context)
	#render is imported from shortcuts

	#dictionary - can pass in context to our template, 
		#django takes template / templates context and mesh it turns it into html
	#context can be any data type
	my_context = {
		"my_text" : "this is about us",
		"my_number":123,
		"my_list" : [1,2,3]
	}
	return render(request,"home.html",my_context)
