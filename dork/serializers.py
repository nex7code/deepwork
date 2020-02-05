from rest_framework import serializers
from dork.models import WorkBoard


class WorkBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkBoard
        fields = "__all__"

    #    fields = ['title', 'priority', 'color', 'backgroud_image', 'create_date',
    # 'start_time','expected_end_time','real_end_time','expected_total_time',
    # 'real_total_time','description']

