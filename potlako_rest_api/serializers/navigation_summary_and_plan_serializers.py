from rest_framework import serializers

from potlako_subject.models import NavigationSummaryAndPlan, EvaluationTimeline


class EvaluationTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationTimeline
        fields = ('id',
                  'pk',
                  'navigation_plan_id',
                  'key_step',
                  'target_date',
                  'adjusted_target_date',
                  'key_step_status',
                  'completion_date',
                  'review_required',
                  )


class NavigationSummaryAndPlanSerializers(serializers.ModelSerializer):
    evaluation_timeline = EvaluationTimelineSerializer(many=True, read_only=True)

    class Meta:
        model = NavigationSummaryAndPlan
        fields = ('id',
                  'subject_identifier',
                  'diagnostic_plan',
                  'notes',
                  'evaluation_timeline')
