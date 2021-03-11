from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from rest_framework import routers
from event_manager_app.views import UserView, EventViewSet

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'event', EventViewSet)

# urls dla projektu
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('event_manager_app.urls')),
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  url(r"^register/", include("django.contrib.auth.urls"), name='password_change'),
                  url('', include(router.urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
