from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description')
admin.site.register(Post,PostModelAdmin)