from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from reviews.models import Review
from users.models import UserRoles
from reviews.forms import ReviewForm


class DogReviewListView(LoginRequiredMixin, ListView):
    model = Review
    extra_context = {
        'title': 'Все отзывы о собаке'
    }
    template_name = 'reviews/reviews.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(dog_pk=self.kwargs.get('pk'))
        queryset = queryset.filter(sign_of_review=True)

        return queryset


class DeactivatedDogReviewListView(LoginRequiredMixin, ListView):
    model = Review
    extra_context = {
        'title': 'Неактивные отзывы'
    }
    template_name = 'reviews/reviews.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(dog_pk=self.kwargs.get('pk'))
        queryset = queryset.filter(sign_of_review=False)

        return queryset



