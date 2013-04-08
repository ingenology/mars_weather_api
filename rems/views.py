from rest_framework import generics

from .models import Report
from .serializers import ReportSerializer


class ReportList(generics.ListAPIView):
    model = Report
    serializer_class = ReportSerializer

report_list = ReportList.as_view()


class ReportDetail(generics.SingleObjectAPIView):
    model = Report
    serializer_class = ReportSerializer

report_detail = ReportDetail.as_view()
