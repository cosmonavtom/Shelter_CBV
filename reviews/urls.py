from django.urls import path

from reviews.apps import ReviewsConfig
from reviews.views import ReviewListView, DeactivatedDogReviewListView

app_name = ReviewsConfig.name

urlpatterns = [
    path('',ReviewListView.as_view(), name='list_reviews'),
    path('deactivated/', DeactivatedDogReviewListView.as_view(), name='deactivated_reviews_list'),
]
