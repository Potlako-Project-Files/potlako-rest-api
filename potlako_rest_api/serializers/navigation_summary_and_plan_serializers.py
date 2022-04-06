from rest_framework import serializers

from potlako_subject.models import NavigationSummaryAndPlan


class NavigationSummaryAndPlanSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavigationSummaryAndPlan
        fields = ('subject_identifier', 'diagnostic_plan', 'notes')
