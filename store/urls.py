from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', views.user_login, name="login"),
    # path('register/', views.user_register, name="register"),
    path('logout/', views.user_log_out, name="logout")
]