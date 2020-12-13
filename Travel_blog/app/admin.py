from django.contrib import admin
from Travel_blog.app.models import Destination, Comment


class CommentInLine(admin.StackedInline):
    model = Comment


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'year')
    inlines = (CommentInLine, )


admin.site.register(Destination, DestinationAdmin)
