from django.contrib import admin
#from django import forms
from .models import Shu, Pp, Uch, Prof, Users

"""
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
"""
@admin.register(Shu)
class ShuAdmin(admin.ModelAdmin):
    """Шахта управление"""
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

@admin.register(Pp)
class PpAdmin(admin.ModelAdmin):
    """Шахта управление"""
    list_display = ("name", "shu", "user")
    list_display_links = ("name", "shu", "user")
    search_fields = ("name", "shu", "user")

@admin.register(Uch)
class UchAdmin(admin.ModelAdmin):
    """Шахта управление"""
    list_display = ("name", "shu", "pp")
    list_display_links = ("name", "shu", "pp")
    search_fields = ("name", "shu", "pp")

@admin.register(Prof)
class ProfAdmin(admin.ModelAdmin):
    """Првффесия"""
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """Лоди"""
    list_display = ("name", "nomer", "shu", "pp", "uch", "prof")
    list_display_links = ("name",)
    search_fields = ("name",)

admin.site.site_title = "Экзаменатор"
admin.site.site_header = "Digital Land"

'''
class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''