from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    country_code = models.IntegerField()
    city = models.CharField(max_length=100)
    address = models.TextField()
    locality = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    cuisines = models.CharField(max_length=255)
    average_cost_for_two = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=50)
    has_table_booking = models.BooleanField()
    has_online_delivery = models.BooleanField()
    is_delivering_now = models.BooleanField()
    switch_to_order_menu = models.BooleanField()
    price_range = models.IntegerField()
    aggregate_rating = models.FloatField()
    rating_color = models.CharField(max_length=50)
    rating_text = models.CharField(max_length=50)
    votes = models.IntegerField()

    def __str__(self):
        return self.name
    
