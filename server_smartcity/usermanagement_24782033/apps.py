from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError


class Usermanagement24782033Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usermanagement_24782033'

    def ready(self):
        # Sambungkan handler post_migrate agar user admin dibuat setelah
        # migrasi dijalankan dan tanpa men-trigger query DB langsung di init.
        from django.db.models.signals import post_migrate

        post_migrate.connect(
            self.create_default_admin,
            dispatch_uid='usermanagement_24782033.create_default_admin',
        )

    def create_default_admin(self, sender, app_config=None, **kwargs):
        if app_config is not None and app_config.name != self.name:
            return

        try:
            User = get_user_model()
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@example.com',
                    'is_admin': True,
                    'is_staff': True,
                    'is_superuser': True,
                    'is_active': True,
                }
            )

            if created:
                admin_user.set_password('admin123')
                admin_user.save()
            else:
                updated = False
                if not admin_user.is_staff:
                    admin_user.is_staff = True
                    updated = True
                if not admin_user.is_superuser:
                    admin_user.is_superuser = True
                    updated = True
                if not admin_user.is_active:
                    admin_user.is_active = True
                    updated = True
                if not admin_user.is_admin:
                    admin_user.is_admin = True
                    updated = True
                admin_user.set_password('admin123')
                updated = True
                if updated:
                    admin_user.save()
        except (OperationalError, ProgrammingError):
            pass
