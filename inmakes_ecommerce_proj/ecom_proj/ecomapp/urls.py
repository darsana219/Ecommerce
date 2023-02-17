from django.urls import path
from . import views

app_name = 'ecomapp'

urlpatterns = [
    path('',views.AllCategoryProduct,name = 'AllCategoryProduct'),
    path('<slug:c_slug>/',views.AllCategoryProduct,name = 'productsbycat'),
    path('<slug:c_slug>/<slug:p_slug>/',views.ProductDetail,name = 'productdetail')
]