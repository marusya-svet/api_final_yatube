from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, \
    GroupViewSet, FollowViewSet
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView,\
    TokenRefreshView, TokenVerifyView


app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
v1_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
