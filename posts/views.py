from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogPostForm
from django.utils import timezone


def get_posts(request):
    """
    Create a view that will get a list of posts published before 'now'
    Render them to 'blogposts.html' template
    """
    
def post_details(request, pk):
    """
    Create a view that returns a single Post object
    based on the post id (pk) and render it to 'postdetails.html' template
    or return a 404 if it isn't found
    """
    
def create_or_edit_post(request, pk=None):
    """ create_or_edit_post
    
    Create a view that allows us to create or edit a post
    depending on whether pk is empty or not
    
    """
    

