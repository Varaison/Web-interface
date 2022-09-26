from django.contrib import admin

from .models import Gs
from .models import Rubric


class GsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )


admin.site.register(Gs, GsAdmin)     #Регистрация приложения на сайте.
admin.site.register(Rubric)