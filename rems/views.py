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
    return Response(latest.data)


class ReportList(generics.ListAPIView):
    model = Report
    serializer_class = ReportSerializer
    paginate_by = 10

report_list = ReportList.as_view()


"""
class ReportDetail(generics.SingleObjectAPIView):
    model = Report
    serializer_class = ReportSerializer

report_detail = ReportDetail.as_view()
"""
