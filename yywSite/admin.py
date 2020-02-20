from django.contrib import admin
from yywSite.models import *
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
admin.site.register(BookInfo,BookInfoAdmin)