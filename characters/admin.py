from django.contrib import admin

from .models import Character, Universe, Api

admin.site.register(Character)
admin.site.register(Universe)
admin.site.register(Api)
