from django.contrib import admin
from . import models

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...
@admin.register(models.Hamburgers)
class HamburgersAdmin(admin.ModelAdmin):
    ...
@admin.register(models.SideDishes)
class SideDishesAdmin(admin.ModelAdmin):
    ...
    
@admin.register(models.SweetsTreats)
class SweetsTreatsAdmin(admin.ModelAdmin):
    ...
    
@admin.register(models.UserApp)
class UserAppAdmin(admin.ModelAdmin):
    ...
    

@admin.register(models.Clube)
class ClubeAdmin(admin.ModelAdmin):
  ...

@admin.register(models.Crew)
class CrewAdmin(admin.ModelAdmin):
    ...