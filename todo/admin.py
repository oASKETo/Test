from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    list_editable = ('done',)
    list_filter = ('done',)

# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('lat1', 'lat2','adres')

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('title',)
#     search_fields = ('title',)


admin.site.register(Todo, TodoAdmin)
# admin.site.register(Category, CategoryAdmin)
