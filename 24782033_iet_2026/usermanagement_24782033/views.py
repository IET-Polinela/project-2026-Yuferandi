from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Import form custom kamu (pastikan sudah buat forms.py seperti saran sebelumnya)
# Jika belum buat, gunakan UserCreationForm bawaan tapi pastikan modelnya benar
from .forms import CitizenRegistrationForm 

# LOGIN VIEW
class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True  # Jika sudah login, dilempar ke success_url

    def form_valid(self, form):
        messages.success(self.request, f"Selamat datang kembali, {form.cleaned_data.get('username')}!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, "Username atau password salah. Coba lagi!")
        return super().form_invalid(form)


# LOGOUT
# Kita gunakan fungsi biasa agar bisa diakses lewat link (GET) 
# karena Django 5 mewajibkan POST untuk LogoutView bawaan.
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Anda telah berhasil logout dari Axel City.")
    return redirect('login')


# REGISTER VIEW
class RegisterView(CreateView):
    # Menggunakan custom form agar tersambung ke CustomUser
    form_class = CitizenRegistrationForm 
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        # Kalau user sudah login, jangan kasih mereka register lagi
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        
        # Sesuai Aturan Lab Session 6
        user.is_admin = False
        user.is_member = True
        
        user.save()
        
        messages.success(self.request, "Akun berhasil dibuat! Silakan gunakan username & password kamu untuk masuk.")
        return redirect('login')

    def form_invalid(self, form):
        messages.error(self.request, "Gagal registrasi. Pastikan data sudah benar!")
        return super().form_invalid(form)