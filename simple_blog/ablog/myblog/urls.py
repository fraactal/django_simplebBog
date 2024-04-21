from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailsView, AddPostView, UpdatePostView, DeletePostView
from .views import AddCategoryView, CategoryView

urlpatterns = [
    #path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),  # we need to put something ahead of url article/<int:pk>/remove
    
    #category
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),  

]
