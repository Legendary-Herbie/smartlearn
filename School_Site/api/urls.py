from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, ProfileViewSet, PlanViewSet, FlashcardViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"register", RegisterViewSet, basename="register")
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"plans", PlanViewSet, basename="plans")
router.register(r"flashcards", FlashcardViewSet, basename="flashcards")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
