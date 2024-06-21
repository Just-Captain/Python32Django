from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
# Create your views here.

def render_index_page(request):
    return render(request=request, template_name='blog/index.html')



def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/list/')
    else:
        form = PostForm()
        return render (
            request=request,
            template_name="blog/create_post.html",
            context={"form": form})


def list_post(request):
    if request.method == "GET":
        posts = Post.objects.filter(published=True)
        data = {"posts": posts}
        return render(
            request=request,
            template_name="blog/list_post.html",
            context=data)
    
    
