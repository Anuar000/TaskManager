from rest_framework import serializers
from django.utils import timezone
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    is_overdue = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status',
            'due_date', 'is_overdue', 'created_at', 'updated_at'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at', 'is_overdue')

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "Дата выполнения не может быть в прошлом"
            )
        return value

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Название задачи должно содержать минимум 3 символа"
            )
        return value.strip()


class TaskCreateSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        fields = [
            'title', 'description', 'status', 'due_date'
        ]


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']

    def validate_due_date(self, value):
        # При обновлении разрешаем прошлые даты для завершенных задач
        if (value < timezone.now() and
                self.instance and
                self.instance.status != 'done' and
                self.validated_data.get('status', self.instance.status) != 'done'):
            raise serializers.ValidationError(
                "Дата выполнения не может быть в прошлом для незавершенных задач"
            )
        return value