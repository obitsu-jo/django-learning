from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, get_user_model, logout
from django.shortcuts import redirect, render

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/diary/')

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = 'registration/user_confirm_delete.html'
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        logout(self.request)
        response = super().form_valid(form)
        return response

class ConfirmLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'registration/logout.html')


signup = SignUpView.as_view()
userdelete = UserDeleteView.as_view()
confirm_logout = ConfirmLogoutView.as_view()

"""
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm

class SignUpView(View):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})
"""