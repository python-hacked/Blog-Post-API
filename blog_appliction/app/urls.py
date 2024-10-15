from django.urls import include, path
from . views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.routers import DefaultRouter

from . views import ProductViewSet,PayPalPaymentView
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("ragister", register),
    path("get_user/", get_user),
    path("login", login),
    path("category/", create_category),
    path("category/<int:pk>/", update_category, name="category"),
    path("list_category", get_category),
    path("delete_category/<int:pk>/", delete_category, name="delete_category"),
    path("post", create_post),
    path("list_post", get_post),
    path("update_post/<int:pk>/", update_post, name="update_post"),
    path("delete_post/<int:pk>/", delete_post, name="delete_post"),
    path("comment", create_comment),
    path("list_comment", get_comment),
    path("update_comment/<int:pk>/", update_comment, name="update_comment"),
    path("delete_comment/<int:pk>/", delete_comment, name="delete_comment"),
    path('api', include(router.urls)),
    path('paypal/', PayPalPaymentView.as_view(), name='paypal'),         

]


