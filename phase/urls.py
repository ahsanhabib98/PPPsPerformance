from django.urls import path
from .views import category, sub_category, child_category


urlpatterns = [
    path('category/', category, name='category'),
    path('sub/category/<int:id>', sub_category, name='subcategory'),
    path('child/category/<int:id>', child_category, name='childcategory')
]