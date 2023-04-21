from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Vote)

