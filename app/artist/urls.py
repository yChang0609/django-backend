"""
URL mappings for artist API.
"""

from django.urls import path

from artist import views

app_name = "artist"

urlpatterns = [
    path("list/", views.ListArtists.as_view(), name="artist-list"),
    path("<int:pk>/like", views.ArtistLikeView.as_view(), name="artist-like")
]
