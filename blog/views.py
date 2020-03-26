from django.shortcuts import render,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.urls import reverse
from django.views import View
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)

# Create your views here.
def article_list_all(request):
	queryset = Article.objects.all()
	context = {
		"object_list" : queryset
	}
	return render(request,"article/article_list.html",context)

def article_detail(request,my_id):
	obj = get_object_or_404(Article,id=my_id)
	context = {
		"object" : obj
	}
	return render(request,"article/article_detail.html",context)

class ArticleListView(ListView):
	#the variable in the html will be called object_list
	template_name = "article/article_list.html"
	queryset = Article.objects.all() #blog/<modelname>_list.html

class ArticleDetailView(DetailView):
	#the variable in the html will be called object_list
	template_name = "article/article_detail.html"

	#limit the choice for the DetailView
	#queryset = Article.objects.all() #blog/<modelname>_list.html

	#overriding a method - built into detail view
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

class ArticleCreateView(CreateView):
	#need to bring in model form
	form_class = ArticleForm
	template_name = "article/article_create.html"

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)
	#it requires get_absolute_url to be defined in models.py (critical to update/create/delete view)
	#can over-ride by defining success_url = '/' or def get_success_url(self)


class ArticleUpdateView(UpdateView):
	template_name = "article/article_create.html"
	#need to bring in the form for update
	form_class = ArticleForm
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id = id_)

class ArticleDeleteView(DeleteView):
	template_name = "article/article_delete.html"
	#need to bring in the form for update
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id = id_)
	#critical - setting success url
	#will not delete if not define
	def get_success_url(self):
		return reverse("article:article_list")

#simple render --> converting to View from function - based view
class ArticleView(View):
	#the name now matters depending on the HTTP method that is trying to handle
	#need to add self because get is reference or no META error 
	def get(self,request,*args,**kwargs):
		return render(request,"article/about.html",{})
		#can also do 
		# template_name = "about.html"
		#return render(request,self.template_name,{})

#Raw Detail Class based view
class ArticleDetailViewRaw(View):
	template_name = "article/article_detail.html"
	#need to pass in id = none, id is no longer required
	#this is because we want it this view to be able to work with about.html
	def get(self,request,id=None,*args,**kwargs):
		#Get method
		context = {}
		if id is not None:
			obj = get_object_or_404(Article,id = id)
			context["object"] = obj
		return render(request,self.template_name,context)

class ArticleListViewRaw(View):
	template_name = "article/article_listraw.html"
	queryset = Article.objects.all()
	
	#mimic generic queryset - for inheritance 
	#need to redefine queryset because it is ony initialize once at the start
	def get_queryset(self):
		self.queryset = Article.objects.all()
		return self.queryset

	def get(self,request,*args,**kwargs):
		print("HI")
		context = {
			"object_list":self.get_queryset
		}
		print(self.queryset[id==2].text)
		return render(request,self.template_name,context)

class ArticleCreateViewRaw(View):
	template_name = "article/article_create.html"

	def get(self,request,*args,**kwargs):
		#Get method
		form = ArticleForm()
		#needs to be form for key because in form is named that in create template
		context = {"form":form}
		return render(request,self.template_name,context)
	
	def post(self,request,*args,**kwargs):
		#grabbing request.post 
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			#to generate a new form 
			form = ArticleForm()
		context = {"form":form}
		return render(request,self.template_name,context)

class ArticleUpdateViewRaw(View):
	template_name = "article/article_create.html"
	def get_object(self):
		id = self.kwargs.get("id")

		obj = None
		if id is not None:
			obj = get_object_or_404(Article,id = id)
			#context["object"] = obj
		return obj

	def get(self,request,*args,**kwargs):
		#Get method
		context = {}
		#needs to be form for key because in form is named that in create template
		obj = self.get_object()
		if obj is not None:
			form = ArticleForm(instance = obj)
			context["object"] = obj
			context['form'] = form
		return render(request,self.template_name,context)
	
	def post(self,request,*args,**kwargs):
		context = {}
		#needs to be form for key because in form is named that in create template
		obj = self.get_object()
		if obj is not None:
			form = ArticleForm(request.POST,instance=obj)
			if form.is_valid():
				form.save()
			context["object"] = obj
			context['form'] = form
		return render(request,self.template_name,context)

#to reduce code redunancy 
#takes in object - python object / just making an extension of the object class - mother of all classes
	#only makes a difference in python2
#class ArticleObjectMixin(object):
#	model = Article
#	def get_object(self):
#		id = self.kwargs.get(self.lookup)
		# obj = None
		# if id is not None:
		# 		obj = get_object_or_404(self.model,id = id)
		# return obj

#now we can do class ArticleUpdateViewRaw(ArticleMixin,View):