from django.urls import path
from .views import BlogListView, BlogCreateVieww, BlogDetailView, BlogUpdateView, BlogDeleteView,BlogCreateUser

app_name = "blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),  
    path('Create/', BlogCreateVieww.as_view(), name="create"),
    path('<int:pk>', BlogDetailView.as_view(), name = "detail"),
    path('<int:pk>/update/',BlogUpdateView.as_view(),name = "update"),
    path('<int:pk>/delete/',BlogDeleteView.as_view(),name = "delete"),
    path('Createuser/',BlogCreateUser.as_view(), name="createuser"),
]