from django.urls import path
from .views import LicenseListView, LicenseDetailView

urlpatterns = [
    path("", LicenseListView.as_view(), name="license_list"),
    path("<int:pk>/", LicenseDetailView.as_view(), name="license_detail"),
]
