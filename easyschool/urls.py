from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.views.generic.base import TemplateView
from teachers import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='soon.html'), name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.TeacherSignUpFormView.as_view(), name='signup'),
    path('login/', views.login, name='login'),
]
if settings.DEBUG:
    import debug_toolbar  # Add debugging urls

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # Static Files URLS
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
