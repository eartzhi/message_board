from django.urls import path, include
from .views import PostList, PostCreate, PostDetail, PostEdit, SearchResponse

urlpatterns = [
   path('', (PostList.as_view()), name='posts'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit', PostEdit.as_view(), name='post_edit'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('search/', SearchResponse.as_view(), name='search_page'),
]