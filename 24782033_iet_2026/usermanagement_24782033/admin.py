from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # 1. Menentukan kolom apa saja yang muncul di tabel daftar user (List View)
    # Ini yang paling penting untuk Screenshot 6 kamu
    list_display = ['username', 'email', 'is_admin', 'is_member', 'is_staff', 'is_active']
    
    # 2. Menambahkan filter di sebelah kanan agar mudah mencari user berdasarkan role
    list_filter = ['is_admin', 'is_member', 'is_staff', 'is_active']
    
    # 3. Menambahkan field custom kita ke dalam halaman detail/edit user di Admin Panel
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Roles (Axel City)', {'fields': ('is_admin', 'is_member')}),
    )
    
    # 4. Menambahkan field custom kita ke form "Add User" (jika admin buat user dari backend)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Roles (Axel City)', {'fields': ('is_admin', 'is_member')}),
    )

# Daftarkan model CustomUser menggunakan class CustomUserAdmin yang baru kita buat
admin.site.register(CustomUser, CustomUserAdmin)