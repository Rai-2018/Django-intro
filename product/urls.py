
from django.urls import path

from .views import dynamic_lookup_view,product_forms,product_delete_view,product_list_all

app_name = "product"
urlpatterns = [
    #can be slug type or any time you specify, the name in the tag has to match the one in the view
	path("<int:my_id>/",dynamic_lookup_view,name = "product_detail"),
    path("<int:my_id>/delete",product_delete_view),
    path("list/",product_list_all),
]
