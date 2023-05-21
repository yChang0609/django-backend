"""
Views for artist API.
"""
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from artist.serializer import ArtistSerializer
from core.models import Artist


class ListArtists(mixins.ListModelMixin, GenericAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ArtistLikeView(mixins.CreateModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(id=self.kwargs["pk"])

    def post(self, request, *args, **kwargs):
        artist = self.get_object()
        user = self.request.user
        print("=================",user)
        is_like_obj = artist.likes.filter(user=user)
        if is_like_obj.exists():
            is_like_obj.delete()
            message = "dislike"
        else:
            artist.likes.create(user=user)
            message = "like"
        artist.save()

        return Response({"message": message})