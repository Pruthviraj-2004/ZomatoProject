import pandas as pd
from django.core.management.base import BaseCommand
from zomatoapp.models import Restaurant

class Command(BaseCommand):
    help = 'Load Zomato restaurant data into the database'

    def handle(self, *args, **kwargs):
        # Path to the Zomato dataset CSV file
        csv_file_path = 'D:/Project/Django projects/Zomato/zomatoproject/zomato.csv'
        
        # Reading the CSV file with the correct encoding (e.g., ISO-8859-1)
        data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

        # Iterating over the rows of the CSV and saving to the database
        for index, row in data.iterrows():
            has_table_booking = True if row['Has Table booking'] == 'Yes' else False
            has_online_delivery = True if row['Has Online delivery'] == 'Yes' else False
            is_delivering_now = True if row['Is delivering now'] == 'Yes' else False
            switch_to_order_menu = True if row['Switch to order menu'] == 'Yes' else False

            restaurant = Restaurant(
                restaurant_id=row['Restaurant ID'],
                name=row['Restaurant Name'],
                country_code=row['Country Code'],
                city=row['City'],
                address=row['Address'],
                locality=row['Locality'],
                longitude=row['Longitude'],
                latitude=row['Latitude'],
                cuisines=row['Cuisines'],
                average_cost_for_two=row['Average Cost for two'],
                currency=row['Currency'],
                has_table_booking=has_table_booking,
                has_online_delivery=has_online_delivery,
                is_delivering_now=is_delivering_now,
                switch_to_order_menu=switch_to_order_menu,
                price_range=row['Price range'],
                aggregate_rating=row['Aggregate rating'],
                rating_color=row['Rating color'],
                rating_text=row['Rating text'],
                votes=row['Votes']
            )
            restaurant.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded Zomato data into the database'))
