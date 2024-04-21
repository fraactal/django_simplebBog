from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Import models
from .models import Post, Category
from .forms import PostForm, EditForm


# Create your views here.
#def home(request):
    #return render(request, "paralax.html", {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    

#Category
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    
def CategoryView(request, cats):
    #query database -> atribute neds to be same as class model
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-',' '), 'category_posts':category_post })
