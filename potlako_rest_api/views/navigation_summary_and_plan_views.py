from rest_framework import viewsets

from potlako_subject.models import NavigationSummaryAndPlan
from ..serializers import NavigationSummaryAndPlanSerializers


class NavigationSummaryAndPlanView(viewsets.ModelViewSet):
    queryset = NavigationSummaryAndPlan.objects.all().order_by('diagnostic_plan')
    serializer_class = NavigationSummaryAndPlanSerializers
