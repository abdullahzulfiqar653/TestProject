from django.db import connection
from rest_framework import serializers

from apis.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "duration", "created_at", "updated_at"]
        extra_kwargs = {"duration": {"required": False}}

    def validate_duration(self, duration):
        request = self.context.get("request")
        if request.method == "POST" and not duration:
            raise serializers.ValidationError({"duration": "duration is required."})
        return duration

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        title = validated_data.get("title")
        duration = validated_data.get("duration")

        if not title:
            raise serializers.ValidationError("Only the 'title' field can be updated.")
        if duration:
            raise serializers.ValidationError(
                {"duration": "duration cannot be updated."}
            )

        query = "UPDATE apis_task SET title = %s, updated_at = GETDATE() WHERE id = %s AND user_id = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [title, instance.id, instance.user.id])
        instance.refresh_from_db()
        return instance
