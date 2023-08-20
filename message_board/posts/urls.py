from django.urls import path, include
from .views import PostList, PostCreate, PostDetail

urlpatterns = [
   path('', (PostList.as_view()), name='posts'),
   path('create/', PostCreate.as_view(), name='create_post'),
   path('ckeditor/', include('ckeditor_uploader.urls')),
   path('<int:pk>', PostDetail.as_view(), name='post'),
]