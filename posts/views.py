from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogPostForm
from django.utils import timezone


def get_posts(request):
    """
    Create a view that will get a list of posts published before 'now'
    Render them to 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date') # soring by published date desc
    return render(request, 'blogposts.html', {'posts': posts })
    
    
    
def post_detail(request, pk):
    """
    Create a view that returns a single Post object
    based on the post id (pk) and render it to 'postdetails.html' template
    or return a 404 if it isn't found
    """
    
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'postdetails.html', {'post': post})
    
def create_or_edit_post(request, pk=None):
    """ create_or_edit_post
    
    Create a view that allows us to create or edit a post
    depending on whether pk is empty or not
    
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(instance=post)
        
    return render(request, 'blogpostform.html', {'form': form})
    

