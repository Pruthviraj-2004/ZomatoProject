from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'restaurant_id', 'name', 'city', 'country_code', 'cuisines', 
        'average_cost_for_two', 'aggregate_rating', 'votes'
    )
    list_filter = ('city', 'cuisines', 'country_code', 'price_range')
    search_fields = ('name', 'city', 'cuisines')
