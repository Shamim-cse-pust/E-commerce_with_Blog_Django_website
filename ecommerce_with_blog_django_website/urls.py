from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='Home'),
    path('blog/', include("blog.urls")),
    path('shop/', include("shop.urls")),
]