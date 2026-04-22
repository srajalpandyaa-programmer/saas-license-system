from django.shortcuts import render
from rest_framework import generics
from .models import License
from .serializers import LicenseSerializer

class LicenseListView(generics.ListCreateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class LicenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
