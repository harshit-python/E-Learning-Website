from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "E-Learning4U Admin"
admin.site.site_title = "E-Learning$U Admin Portal"
admin.site.index_title = "Welcome to E-Learning4U"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('myapp.urls')),
    path("accounts/", include("accounts.urls"))
]
