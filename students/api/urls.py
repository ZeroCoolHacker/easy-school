from django.conf.urls import url

from .views import StudentRUDView, StudentCreateView, StudentListView

urlpatterns = [
    url(r'^$', StudentListView.as_view(), name='student-list'),
    url(r'^create/$', StudentCreateView.as_view(), name='student-create'),
    url(r'^(?P<pk>\d+)/$', StudentRUDView.as_view(), name='student-rud'),
]
