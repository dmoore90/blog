from django.urls import path
from .views import register, login, create_blog, update_blog, delete_blog, index_page, show_item

urlpatterns = [
	path('', index_page, name="index_page"),
	path('item_page/<int:id>/', show_item, name="show_item"),
	path('register/', register, name="register"),
	path('login/', login, name="login"),
	path('new/', create_blog, name="create_blog"),
	path('update/<int:id>/', update_blog, name="update_blog"),
	path('delete/<int:id>/', delete_blog, name="delete_blog"),
]
