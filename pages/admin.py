from django.contrib import admin

from .models import About, HomePage

class AboutAdmin(admin.ModelAdmin):
    fieldsets = [
        ('About Page Info',          {'fields': ['title', 'description']}),      
    ]
    #inlines = [GameInline, SponsorInline, PrizeInlines
    list_display = ('title', 'last_page_updated', 'updated', 'created', )

class HomePageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Home Page Info',          {'fields': ['homepage_name', 'current_homepage']}),
        ('Banner Image',             {'fields': ['banner_image', ]}),
        ('First Image',  {'fields': [('first_image', ) ]}),
        ('Second Image', {'fields': [('second_image', ) ]}),
        ('Third Image',  {'fields': [('third_image', ) ]}),
    ]
    #inlines = [GameInline, SponsorInline, PrizeInlines
    list_display = ('homepage_name', 'current_homepage',)
    #list_filter = ['updated']
    search_fields = ['updated']

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(About, AboutAdmin)
