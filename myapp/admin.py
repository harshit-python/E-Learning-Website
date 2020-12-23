from django.contrib import admin
from .models import Tutorial, Quiz, MockTest

admin.site.register(Tutorial)
admin.site.register(Quiz)
admin.site.register(MockTest)