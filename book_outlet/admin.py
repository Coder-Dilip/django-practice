from django.contrib import admin
from .models import Book,Address,Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)} #automatically slugify the title for slug field
    list_filter=("author","rating",) # show options in admin panel for sorting the data by either author or rating 
    list_display=("title","author") # display the columns in 
admin.site.register(Book,BookAdmin)
admin.site.register(Address)
admin.site.register(Author)



