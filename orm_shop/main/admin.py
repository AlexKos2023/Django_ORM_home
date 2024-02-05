from django.contrib import admin

from main.models import Car, Client, Sale

# зарегистрируйте необходимые модели
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Sale)
