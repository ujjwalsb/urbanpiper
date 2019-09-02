from django.contrib import admin
from .models import hackerNewsAPI

class APIModelAdmin(admin.ModelAdmin):
    list_display = ["article_id", "title", "sentiment", "username"]

    class Meta:
        model = hackerNewsAPI

admin.site.register(hackerNewsAPI, APIModelAdmin)