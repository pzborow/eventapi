from tenants.views import TenantView, TenantViewRandomForm
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TenantView.as_view(), name="index"),
    path('sample-random/', TenantViewRandomForm.as_view(), name="random_form"),
    path('test/', TemplateView.as_view(template_name='test.html'), name="test"),
    path('admin/', admin.site.urls),
    ]
