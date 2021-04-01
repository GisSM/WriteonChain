from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__','data_creazione','utente']
    list_filter = ['data_creazione']
    search_fields = ['titolo','testo']
    prepopulated_fields = {"slug": ("titolo",)}

    class Meta:
        model = Post

admin.site.register(Post,PostAdmin)