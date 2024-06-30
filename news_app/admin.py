from django.contrib import admin
from .models import News, Category, Contact


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "publish_time", "status"]
    list_filter = ["publish_time", "status", "category"]
    search_fields = ["title", "body"]
    ordering = ["-publish_time"]
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Contact)

