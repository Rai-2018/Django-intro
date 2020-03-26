
from django.urls import path

from .views import(
	article_detail,
	article_list_all,
	ArticleListView,
	ArticleDetailView,
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView,
	ArticleView,
	ArticleDetailViewRaw,
	ArticleListViewRaw,
	ArticleCreateViewRaw,
	ArticleUpdateViewRaw
)
app_name = "article"
urlpatterns = [
    #can be slug type or any time you specify, the name in the tag has to match the one in the view
	path("<int:my_id>/",article_detail,name = "article_detail"),
    path("list/",article_list_all),
    path("list_new",ArticleListView.as_view(),name = "article_list"),
    #defaulted to pk or slug , pk is id field -> primary key
    #path("test/<int:pk>/",ArticleDetailView.as_view(),name = "article_detail1")

    #if i want to change it to id 
    path("test/<int:id>/",ArticleDetailView.as_view(),name = "article_detail1"),
    path("create/",ArticleCreateView.as_view(),name = "article_detail1"),
    path("update/<int:id>/",ArticleUpdateView.as_view()),
    path("delete/<int:id>/",ArticleDeleteView.as_view()),
    #to change the template can do 
    #path("about",ArticleView.as_view(template_name = "contact.html")),
	path("about",ArticleView.as_view()),


    path("view/about",ArticleDetailViewRaw.as_view(template_name="article/about.html")),
    path("view/<int:id>/",ArticleDetailViewRaw.as_view()),
    path("view/list/",ArticleListViewRaw.as_view()),
    path("view/create/",ArticleCreateViewRaw.as_view()),
    path("view/update/<int:id>",ArticleUpdateViewRaw.as_view())
]
