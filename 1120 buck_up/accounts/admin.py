from django.contrib import admin

#カスタムユーザインポート
from .models import CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username')
    list_display_links = ('id','username')

#サイトに登録
admin.site.register(CustomUser,CustomUserAdmin)

