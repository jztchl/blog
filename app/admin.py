from django.contrib import admin

# Register your models here.
from .models import contactMessage,blogItem,Category,commentItem,blogAuthor
# Register your models here.
admin.site.register(contactMessage)
admin.site.register(blogItem)
admin.site.register(Category)
admin.site.register(commentItem)
admin.site.register(blogAuthor)
