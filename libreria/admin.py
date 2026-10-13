from django.contrib import admin
from .models import editorial, libro



class editorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre',)
admin.site.register(editorial, editorialAdmin)
    



class libroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'fecha_publicacion', 'isbn')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('editorial',)

admin.site.register(libro, libroAdmin)
