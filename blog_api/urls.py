from django.urls import path, re_path
from .views import PostList, PostDetail, UserPostList
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    re_path('^user/(?P<username>.+)/$', UserPostList.as_view()),
    path('scheme/', SpectacularAPIView.as_view(), name='scheme'),
    path('scheme/redoc/', SpectacularRedocView.as_view(url_name='scheme'), name='redoc'),
    path('scheme/swagger-ui/', SpectacularSwaggerView.as_view(url_name='scheme'), name='swagger-ui'),
]
