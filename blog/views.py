from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.


posts = [
    {
        'author': 'Arbaz Ahmed',
        'title': 'Post number 1',
        'content': 'Post goes here',
        'date_posted': 'June 16, 2020'
    },
    {
        'author': 'Archit Rathi',
        'title': 'Post number 2',
        'content': 'Post goes here for rathi',
        'date_posted': 'June 20, 2020'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})