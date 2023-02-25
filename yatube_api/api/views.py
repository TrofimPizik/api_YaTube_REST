from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment, Follow
from api.permissions import IsAuthor, ReadOnly, IsAuthenticated

from .serializers import (
    PostSerializer, GroupSerializer,
    CommentSerializer, FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthor | ReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthor | ReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor | ReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs['post_id'])
        )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        comments_is_post_queryset = post.comments.select_related('author')
        return comments_is_post_queryset


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self,):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
