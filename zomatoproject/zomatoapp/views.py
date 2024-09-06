from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Restaurant
from django.db.models import Q

class RestaurantListView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        paginator = Paginator(restaurants, 10)  # Show 10 restaurants per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'zomatoapp/restaurant_list.html', {'restaurants': page_obj, 'page_obj': page_obj})

class RestaurantDetailView(View):
    def get(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
        return render(request, 'zomatoapp/restaurant_detail.html', {'restaurant': restaurant})

class SearchRestaurantByLocationView(View):
    def get(self, request):
        return render(request, 'zomatoapp/search_by_location.html')

    def post(self, request):
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        range_km = float(request.POST.get('range_km'))
        
        # Example filtering logic for latitude and longitude range
        restaurants = Restaurant.objects.filter(
            Q(latitude__range=(latitude - range_km, latitude + range_km)) &
            Q(longitude__range=(longitude - range_km, longitude + range_km))
        )

        return render(request, 'zomatoapp/search_by_location.html', {'restaurants': restaurants})

class FilterRestaurantView(View):
    def get(self, request):
        countries = Restaurant.objects.values_list('country_code', flat=True).distinct()
        cuisines = Restaurant.objects.values_list('cuisines', flat=True).distinct()
        
        country = request.GET.get('country')
        average_spend_min = request.GET.get('spend_min')
        average_spend_max = request.GET.get('spend_max')
        cuisine = request.GET.get('cuisine')
        search_query = request.GET.get('search_query')

        restaurants = Restaurant.objects.all()

        if country:
            restaurants = restaurants.filter(country_code=country)
        if average_spend_min and average_spend_max:
            restaurants = restaurants.filter(average_cost_for_two__gte=average_spend_min, average_cost_for_two__lte=average_spend_max)
        if cuisine:
            restaurants = restaurants.filter(cuisines__icontains=cuisine)
        if search_query:
            restaurants = restaurants.filter(name__icontains=search_query)

        paginator = Paginator(restaurants, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'restaurants': page_obj,
            'page_obj': page_obj,
            'countries': countries,
            'cuisines': cuisines,
        }

        return render(request, 'zomatoapp/filter_restaurants.html', context)
