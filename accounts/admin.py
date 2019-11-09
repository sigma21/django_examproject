from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class AccountAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "date_joined", "last_login")
    search_fields = ("email", "first_name", "last_name")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()

admin.site.register(Account, AccountAdmin)