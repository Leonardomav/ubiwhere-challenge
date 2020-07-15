import self as self
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action


from .models import Occurrence, Category
from .serializers import OccurrenceSerializer, CategorySerializer, OccurrenceListSerializer, \
    OccurrenceInstanceSerializer, OccurrenceUpdateSerializer
from .custom_permissions import IsOwnerOrStaff
from rest_framework.response import Response


class OccurrenceView(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = (IsOwnerOrStaff,)

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'GET':
            serializer_class = OccurrenceInstanceSerializer

        if (self.request.method == 'PUT' or self.request.method == 'PATCH') and bool(self.request.user and self.request.user.is_staff):
            serializer_class = OccurrenceUpdateSerializer

        return serializer_class


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAdminUser,)
