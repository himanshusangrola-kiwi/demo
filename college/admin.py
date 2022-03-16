from django.contrib import admin

from authentication.models import CustomUser

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('full_name','email','username')


admin.site.register(CustomUser,UserAdmin)