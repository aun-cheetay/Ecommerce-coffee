from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(CoffeeMachineProduct)
admin.site.register(CoffeePodProduct)
admin.site.register(PackSize)
admin.site.register(CoffeePodFlavour)


