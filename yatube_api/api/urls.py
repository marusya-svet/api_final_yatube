from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, \
    GroupViewSet, FollowViewSet
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView,\
    TokenRefreshView, TokenVerifyView


app_name = 'api'

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]