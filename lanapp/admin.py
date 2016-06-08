from django.contrib import admin

from .models import Event, Game, Prize, Sponsor

# class GameInline(admin.TabularInline):
#     model = Game 
#     extra = 1

# class SponsorInline(admin.TabularInline):
#     model = Sponsor
#     extra = 1

# class PrizeInline(admin.TabularInline):
#     model = Prize
#     fieldsets = [
#         (None, {
#             'fields': ('name', 'url', 'image',),
#             'classes': ('collapse', 'wide'),
#         }),
#     ]
#     extra = 1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Info',               {'fields': ['event_name', 'event_description', 'image']}),
        ('Date information', {'fields': ['event_start_date', 'event_end_date'], 'classes': ['collapse']}),
        ('Location and Logistics information', {'fields': ['venue','logistics_information', 'street_address', 'city', 'state', 'zip_code'], 'classes': ['collapse']}),
        ('Sponsors, Games, Prizes', {'fields': ['sponsors', 'games', 'prizes'], 'classes': ['collapse']}),
    ]
    #inlines = [GameInline, SponsorInline, PrizeInline]
    filter_horizontal = ['sponsors', 'games', 'prizes']
    list_display = ('event_name', 'event_start_date', 'event_coming_soon')
    list_filter = ['event_start_date']
    search_fields = ['event_name']

class GameAdmin(admin.ModelAdmin):
    pass

class PrizeAdmin(admin.ModelAdmin):
    pass

class SponsorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(Sponsor, SponsorAdmin)
