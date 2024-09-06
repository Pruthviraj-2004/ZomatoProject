from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('zomato/', include('zomatoapp.urls')),  # Include zomatoapp URLs
    path('', include('zomatoapp.urls')),  # Include zomatoapp URLs
]
