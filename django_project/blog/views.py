from django.shortcuts import render
from django.http import HttpResponse

# pretend database call
posts = [
    {
            'author': 'CoreyMs',
            'title': 'Blog post',
            'content': 'First post content',
            'date_posted': 'August 27, 2018'
    },
        {
            'author': 'Jane Doe',
            'title': 'Blog post 2',
            'content': '2nd post content',
            'date_posted': 'August 28, 2018'
    }
]

def home(request):

    # pass in the posts database via context object
    context = {        
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

