from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views, get_user_model
from django.views import generic as views
from ecommerce_django.accounts.forms import CreateUserForm, EditUserForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)

        return response


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = 'store'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['username'] = self.request.user.username
        context['email'] = self.request.user.email

        return context


class UserEditView(views.UpdateView):
    form_class = EditUserForm
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
    
