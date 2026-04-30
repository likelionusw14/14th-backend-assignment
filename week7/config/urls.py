from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/lions/')),
    path('admin/', admin.site.urls),
    path('lions/', include('lions.urls')),
]
