from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth import views as auth_views

from ToDoApp.accounts.forms import ProjectUserEditForm, UserLoginForm, ProjectUserCreateForm
from ToDoApp.accounts.models import CustomUser


# Create your views here.
class UserRegisterView(generic.CreateView):
    model = CustomUser
    form_class = ProjectUserCreateForm
    template_name = 'register-page.html'
    success_url = reverse_lazy('home-page')


@method_decorator(login_required, name='dispatch')
class UserEditView(generic.UpdateView):
    model = CustomUser
    form_class = ProjectUserEditForm
    template_name = 'profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'home-page.html'
    next_page = reverse_lazy('home-page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home-page')


@method_decorator(login_required, name='dispatch')
class UserDetailsView(generic.DetailView):
    model = CustomUser
    template_name = 'profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name='dispatch')
class UserDeleteView(generic.DeleteView):
    model = CustomUser
    template_name = 'profile-delete-page.html'
    success_url = reverse_lazy('home-page')

    def delete(self, request, *args, **kwargs):
        self.request.user.delete()
        return redirect(self.get_success_url())
