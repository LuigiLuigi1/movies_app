from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['Shrek', 'Happy Gilmore', 'Kung Pow']
    }
    return render(request,'movies/index.html', context)

def about(request):
    return render(request,'movies/about.html', {})

# python -m django startproject config .
# python manage.py startapp movies
# pip install django
# pip install gunicorn
# pip freeze requirements.txt
# python manage.py runserver

#app/templates/app/index.html
#movies/templates/movies/index.html