# Django 2 - Getting Started


## Introduction

Throughout this tutorial, we’ll walk you through the creation of a movies categorization application.

## Dependencies

* Python 3
* [Django 2.0.1](https://www.djangoproject.com/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## Contributors

* [Marcos Pereira](marcospereira.mpj@gmail.com)


## Project Structure

```
    | - manage.py 
    | - getting_started
        \ - settings.py
        \ - urls.py
        \ - wsgi.py
    | - flix
        \ - migrations
        \ - models
            \ - category.py
            \ - movie.py   
        \ - templates
            \ - home_page.html
        \ - views 
            \ - home_page.py
        \ - admin.py
        \ - apps.py
        \ - urls.py
```

## Start Development Server

1. Run `python manage.py migrate` to create the application models.

2. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a genre and a movie (you'll need the Admin app enabled).

3. Visit http://127.0.0.1:8000/flix/.


## URLs

* Admin: http://127.0.0.1:8000/admin/
* Home Page: http://127.0.0.1:8000/flix/