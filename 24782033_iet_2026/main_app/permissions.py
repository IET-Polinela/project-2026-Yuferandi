from rest_framework import permissions

class SmartCityRolePermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Admin dilarang melakukan aksi Create (membuat laporan baru)
        if view.action == 'create' and request.user.is_staff:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        # Mengizinkan siapa saja melihat detail laporan (Read-Only)
        if request.method in permissions.SAFE_METHODS:
            return True
          
        if request.method == 'DELETE':
            # Admin dilarang menghapus. Citizen hanya hapus miliknya saat DRAFT
            if request.user.is_staff:
                return False 
            return obj.reporter == request.user and obj.status == 'DRAFT'
          
        if request.method in ['PUT', 'PATCH']:
            # Admin diizinkan lolos untuk edit status. Citizen hanya edit miliknya saat DRAFT
            if request.user.is_staff:
                return True 
            return obj.reporter == request.user and obj.status == 'DRAFT'
          
        return False