from django.urls import path
from .views import FilterRestaurantView, RestaurantDetailView, RestaurantListView, SearchRestaurantByLocationView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('search/location/', SearchRestaurantByLocationView.as_view(), name='search_by_location'),
    path('filter/', FilterRestaurantView.as_view(), name='filter_restaurant'),
]
