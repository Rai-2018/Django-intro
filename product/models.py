from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length = 20) #max_length required
	description = models.TextField(blank = True, null = True)
	price = models.DecimalField(decimal_places=2,max_digits=1000)
	#blank has how field is render (false = field is required in the form), validation purpose
	#null is with the db
	summary = models.TextField(blank=True,null=False)

	#Adding attribute - make migration / migrate
	#Will have to resolve new attribute value for old existent row
		#Can do null = true -> set old ones to true 
		#Can do default = true
	#Or during makemigration press 1 and set a default value, old value will have true and new value waitiing for input
	featured = models.BooleanField(default= True)

	def get_absolute_url(self):
		#dynamic url routing -- hard coding
		#f is f_string --> formmated string literal similar to % in printf for c
		#return f"/product/{self.id}/"
		
		#dynamic reverse url routing
		#in the url related to the name product_detail, pass in my_id
		#reverse is now based off app_name: product
		#returns a url
		return reverse("product:product_detail",kwargs={"my_id":self.id})
		#or
		#return reverse("product_detail",kwargs={"my_id":self.id},name = "product")