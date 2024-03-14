from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from .forms import UserForm, ProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user == user:
        photos = user.photo_set.filter(is_public=True)[:20]
        context = {"profile_user": user, "photos": photos}
        return render(request, "accounts/profile.html", context)
    else:
        messages.error(request, "접근할 수 없는 프로필입니다.")
        return redirect(reverse("root"))


class ProfileUpdate(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_form = UserForm(
            initial={
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )

        if hasattr(user, "profile"):
            profile = user.profile
            profile_form = ProfileForm(
                initial={
                    "nickname": profile.nickname,
                    "profile_photo": profile.profile_photo,
                }
            )
        else:
            profile_form = ProfileForm()

        return render(
            request,
            "accounts/profile_update.html",
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=user.profile if hasattr(user, "profile") else None,
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("profile", args=[user.pk]))
        else:
            return render(
                request,
                "accounts/profile_update.html",
                {"user_form": user_form, "profile_form": profile_form},
            )


class ChangePassword(PasswordChangeView):
    success_url = reverse_lazy("root")
