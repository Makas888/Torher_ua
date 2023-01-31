from django.contrib import admin
from news_letter_form.models import Newsletter


@admin.register(Newsletter)
class NewsLetterAdmin(admin.ModelAdmin):
    """displaying emails of subscribers to the newsletter in the admin panel"""

    list_display = ['email', 'date']
