from .views import MovieDetail, MovieList
from django.urls import path

urlpatterns = [

    path('', MovieList.as_view(),name= 'Movie_List'),
    path('<int:pk>', MovieDetail.as_view(),name= 'Movie_Detail'),
]