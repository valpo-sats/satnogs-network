from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .forms import UserForm
from .models import User
from base.forms import StationForm

from base.models import Station, Observation


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:view_user",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UserForm

    model = User

    def get_success_url(self):
        return reverse("users:view_user",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


def view_user(request, username):
    """View for user page."""
    user = User.objects.get(username=username)
    observations = Observation.objects.filter(author=user)[0:10]
    stations = Station.objects.filter(owner=user)
    form = StationForm()
    if request.method == 'POST':
        form = StationForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = user
            f.save()
            form.save_m2m()
            messages.success(request, 'New Ground Station added!')
            return redirect(reverse('users:view_user', kwargs={'username': username}))

    return render(request, 'users/user_detail.html',
                  {'user': user,
                   'observations': observations,
                   'stations': stations,
                   'form': form})
