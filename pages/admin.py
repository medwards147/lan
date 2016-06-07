from django.contrib import admin

from .models import HomePage

class HomePageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Home Page Info',          {'fields': ['homepage_name', 'current_homepage']}),
        ('Banner Info',             {'fields': ['banner_image', 'heading', 'subheading']}),
        ('First Content Row Info',  {'fields': [('first_content_heading', 'first_image',)]}),
        ('Second Content Row Info', {'fields': [('second_content_heading', 'second_image',)]}),
        ('Third Content Row Info',  {'fields': [('third_content_heading', 'third_image',)]}),
    ]
    #inlines = [GameInline, SponsorInline, PrizeInlines
    list_display = ('homepage_name', 'current_homepage',)
    #list_filter = ['updated']
    search_fields = ['updated']

admin.site.register(HomePage, HomePageAdmin)
