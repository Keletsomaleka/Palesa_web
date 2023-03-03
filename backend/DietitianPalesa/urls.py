from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refres/', TokenRefreshView.as_view(),name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),
    path('api/programs/',include('programs.urls')),
    path('api/myprofile/',include('myprofile.urls')),
    path('api/contacts/',include('contacts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)