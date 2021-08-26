from django.contrib import admin
from .models import About , Skill ,Experience , Link
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class AboutModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description')
admin.site.register(About,AboutModelAdmin)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Link)

