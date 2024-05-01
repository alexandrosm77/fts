from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

import forensic.urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("forensic/", include(forensic.urls)),

    path("", RedirectView.as_view(pattern_name="forensic:instructions")),
]
