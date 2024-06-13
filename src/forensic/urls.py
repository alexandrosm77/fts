from django.urls import include, path
from django.views.generic.base import RedirectView

from . import views


app_name = "forensic"
urlpatterns = [
    path("", RedirectView.as_view(pattern_name="forensic:instructions")),
    path("instructions/", include([
        path("", views.InstructionList.as_view(), name="instructions"),
        path(
            "with-too-many-hair-samples/",
            views.too_many_hair_samples,
            name="too_many_hair_samples",
        ),
        path("<int:pk>/", include([
            path(
                "",
                views.InstructionDetail.as_view(),
                name="instruction_detail",
            ),
        ])),
    ])),
    path("instruction-groups/", include([
        path("", views.InstructionGroupList.as_view(), name="instruction_group"),
        path("<int:pk>/", include([
            path(
                "",
                views.InstructionGroupDetail.as_view(),
                name="instruction_group_detail",
            ),
        ])),
    ])),
    path("collections/", include([
        path("", RedirectView.as_view(pattern_name="forensic:instructions")),
        path(
            "<int:pk>/",
            views.CollectionDetail.as_view(),
            name="collection_detail",
        ),
    ])),
    path("samples/", include([
        path("", RedirectView.as_view(pattern_name="forensic:instructions")),
        path(
            "<int:pk>/",
            views.SampleDetail.as_view(),
            name="sample_detail",
        ),
    ])),
]
