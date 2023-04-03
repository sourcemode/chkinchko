from django.contrib import admin

# Register your models here.
from web.models import CustomUser,CheckinCheckout


class CustomUserAdmin(admin.ModelAdmin):
    pass

class CheckinCheckoutAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CheckinCheckout, CheckinCheckoutAdmin)