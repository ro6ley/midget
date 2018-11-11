from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_links

urlpatterns = {
    path('api/links/', manage_links, name="links"),
    path('<slug:link>', manage_links, name="short_url")
}

urlpatterns = format_suffix_patterns(urlpatterns)
