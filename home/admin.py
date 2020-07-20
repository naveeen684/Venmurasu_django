from django.contrib import admin

# Register your models here.
from home.models import Word


class WordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Word, WordAdmin)
