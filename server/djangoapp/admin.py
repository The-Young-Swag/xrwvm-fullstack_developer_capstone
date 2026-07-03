from django.contrib import admin
from .models import CarMake, CarModel


# Inline editor for CarModel – allows editing models inside CarMake
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    list_filter = ['type', 'year', 'car_make']
    search_fields = ['name']


# Admin class for CarMake, including the inline for CarModel
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']


# Register the models with their admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
