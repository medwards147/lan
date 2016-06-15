from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Info',               {'fields': ['event_name', 'pay_button_text']}),
        ('Date information', {'fields': ['event_start_date', 'event_end_date'], 'classes': ['collapse']}),
        ('Location and Logistics information', {'fields': ['venue','street_address', 'city', 'state', 'zip_code'], 'classes': ['collapse']}),
    ]
    list_display = ('event_name', 'event_start_date', 'event_coming_soon')
    list_filter = ['event_start_date']
    search_fields = ['event_name']

admin.site.register(Event, EventAdmin)
