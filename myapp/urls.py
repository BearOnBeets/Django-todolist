from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.form),
    path('create/',views.create),
    path('alltasks/',views.alltasks),
    path('delete/',views.delete),
    path('edit/',views.edit),
    path('edit/update/',views.update),
    path('search/',views.search)
]