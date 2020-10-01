"""easyschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render

from teachers.views import TeacherSignUpFormView
from teachers.views import Login


def coming_soon(request, *args, **kwargs):
    return render(request, 'soon.html', {})


urlpatterns = [
    url(r'^$', coming_soon, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/students/', include('students.api.urls')),
    url(r'^signup/', TeacherSignUpFormView.as_view(), name='signup'),
    path('login/',Login,name ='login'),
]
if settings.DEBUG:
    import debug_toolbar  # Add debugging urls

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    # Static Files URLS
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
