from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework_gis.filters import DistanceToPointFilter
from .models import Occurrence, Category
from .serializers import OccurrenceDefaultSerializer, CategorySerializer, \
    OccurrenceListSerializer, OccurrenceStaffUpdateSerializer
from .custom_permissions import IsAuthorOrStaff


class OccurrenceFilter(filters.FilterSet):
    """ Filter class for occurrences searches """

    class Meta:
        model = Occurrence
        fields = ['category__name', 'author']


class OccurrenceView(viewsets.ModelViewSet):
    """
    Description:
        occurrence view;
        Uses prebuilt viewsets.ModelViewSet -> https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    """
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceDefaultSerializer
    permission_classes = (IsAuthorOrStaff,)
    distance_filter_field = 'point'
    filter_backends = (DistanceToPointFilter, filters.DjangoFilterBackend)  # backend for the search functionality
    filterset_class = OccurrenceFilter  # filters class used to search occurrences

    def get_serializer_class(self):
        """
        Returns different serializer class depending on the request method and user permissions.
        """
        serializer_class = self.serializer_class

        if self.request.method == 'GET':
            serializer_class = OccurrenceListSerializer

        if (self.request.method == 'PUT' or self.request.method == 'PATCH') and bool(
                self.request.user and self.request.user.is_staff):
            serializer_class = OccurrenceStaffUpdateSerializer

        return serializer_class


class CategoryView(viewsets.ModelViewSet):
    """
    Description:
        Category view;
        Uses prebuilt viewsets.ModelViewSet -> https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAdminUser,)  # prebuilt permission - only if user is_staff == True
