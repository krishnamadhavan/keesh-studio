"""
URLs for keesh_studio.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

app_name = "keesh_studio"

urlpatterns = [
    re_path(r'', TemplateView.as_view(template_name="keesh_studio/base.html")),
]
