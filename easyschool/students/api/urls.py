
from .views import StudentRUDView

from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', StudentRUDView.as_view(), name='student-rud'),
]
