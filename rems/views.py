import django_filters

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Report
from .serializers import ReportSerializer


@api_view(['GET'])
def report_root(request, format=None):
    return Response({
        'latest': reverse('report_latest', request=request),
        'archive': reverse('report_list', request=request),
    })


@api_view(['GET'])
def report_latest(request, format=None):
    latest = ReportSerializer(Report.objects.latest())
    return Response({'report': latest.data})


class ReportFilterSet(django_filters.FilterSet):
    terrestrial_date_start = django_filters.DateFilter(
        name='terrestrial_date',
        lookup_type='gte'
        )
    terrestrial_date_end = django_filters.DateFilter(
        name='terrestrial_date',
        lookup_type='lte',
        )

    class Meta:
        model = Report
        fields = (
            'sol',
            'ls',
            'min_temp',
            'max_temp',
            'pressure',
            'abs_humidity',
            'wind_speed',
            'season',
            'terrestrial_date',
            'terrestrial_date_start',
            'terrestrial_date_end',
            )


class ReportList(generics.ListAPIView):
    model = Report
    serializer_class = ReportSerializer
    filter_class = ReportFilterSet

report_list = ReportList.as_view()
