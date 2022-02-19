from django.urls import path, include

urlpatterns = [
    path('', include('core.field_values_suggestions.urls')),

]
