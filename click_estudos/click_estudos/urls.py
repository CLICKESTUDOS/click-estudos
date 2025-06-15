from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from clickestudosAPP import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_material, name='upload_material'),
    path('material/<int:pk>/deletar/', views.deletar_material, name='deletar_material')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)