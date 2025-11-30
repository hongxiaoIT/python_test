from django.conf.urls import url
from booktest import booktest_views

urlpatterns = [
    url(r'^set_session$', booktest_views.set_session),
    url(r'^get_session$', booktest_views.get_session),
]
