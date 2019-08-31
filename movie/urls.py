from .views import MovieDetail, MovieList, MovieCategory, MovieLanguage, MovieSearch, MovieYear
from django.urls import path


app_name = 'movie'


urlpatterns = [

    path('', MovieList.as_view(),name= 'Movie_List'),
    path('category/<str:category>', MovieCategory.as_view(), name= 'Movie_Category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name= 'Movie_Language'),
    path('search', MovieSearch.as_view(), name= 'Movie_Search'),
    path('<int:pk>', MovieDetail.as_view(),name= 'Movie_Detail'),
    path('year/<int:year>', MovieYear.as_view(),name= 'Movie_Year'),
]