from rest_framework import serializers
from django.contrib.auth.models import User
from learn.models import UserProfile, Plan
from recall.models import Flashcard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        UserProfile.objects.create(user=user)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ["id", "user", "phone_no", "profile_picture", "date_joined", "last_login"]


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ["id", "user", "subject", "goal", "days", "hours", "start_date", "end_date", "created_at"]
        read_only_fields = ["user", "created_at"]


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ["id", "user", "name", "subject", "question", "answer", "date_created"]
        read_only_fields = ["user", "date_created"]
