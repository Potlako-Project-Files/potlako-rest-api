from rest_framework import viewsets

from potlako_subject.models import NavigationSummaryAndPlan, EvaluationTimeline
from ..serializers import NavigationSummaryAndPlanSerializers, \
    EvaluationTimelineSerializer


class NavigationSummaryAndPlanView(viewsets.ModelViewSet):
    queryset = NavigationSummaryAndPlan.objects.all().order_by('subject_identifier')
    serializer_class = NavigationSummaryAndPlanSerializers


class EvaluationTimelineView(viewsets.ModelViewSet):
    queryset = EvaluationTimeline.objects.all().order_by('navigation_plan')
    serializer_class = EvaluationTimelineSerializer
