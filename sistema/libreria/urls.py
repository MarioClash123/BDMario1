from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path ('nosotros', views.nosotros, name='nosotros'),
    path ('cliente', views.cliente_views, name='cliente'),
    path('cliente/crear', views.crear, name='crear'),
    path('cliente/editar', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name ='eliminar'),
    path('cliente/editar/<int:id>', views.editar, name='editar'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)