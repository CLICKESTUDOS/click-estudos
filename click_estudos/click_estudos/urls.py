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
    path('forum-home/', views.forum_home, name='forum_home'),
    path('forum-avaliacao/', views.forum_avaliacao, name='forum_avaliacao'),
    path('sobre/', views.sobre, name='sobre'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/senha/', auth_views.PasswordChangeView.as_view(template_name='clickestudosAPP/password_change.html'), name='password_change'),
    path('perfil/senha/sucesso/', auth_views.PasswordChangeDoneView.as_view(template_name='clickestudosAPP/password_change_done.html'), name='password_change_done'),
    path('disciplinas/', views.disciplinas, name='disciplinas'),
    path('forum-avaliacao/editar/<int:pk>/', views.editar_avaliacao, name='editar_avaliacao'),
    path('forum-avaliacao/deletar/<int:pk>/', views.deletar_avaliacao, name='deletar_avaliacao'),
    path('material/<int:pk>/deletar/', views.deletar_material, name='deletar_material')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)