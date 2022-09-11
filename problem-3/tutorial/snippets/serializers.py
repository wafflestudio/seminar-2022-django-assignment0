from typing import Dict

from django.db.models import query
from rest_framework import serializers
from snippets import models


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={"base_template": "textarea.html"})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=models.LANGUAGE_CHOICES, default="python")
#     style = serializers.ChoiceField(choices=models.STYLE_CHOICES, default="friendly")

#     def create(Self, validated_data) -> models.Snippet:
#         return models.Snippet.objects.create(**validated_data)

#     def update(Self, instance: models.Snippet, validated_data: Dict) -> Dict:
#         instance.title = validated_data.get("title", instance.title)
#         instance.code = validated_data.get("code", instance.code)
#         instance.linenos = validated_data.get("linenos", instance.linenos)
#         instance.language = validated_data.get("language", instance.language)
#         instance.style = validated_data.get("title", instance.title)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
