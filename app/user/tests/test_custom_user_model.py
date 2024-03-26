import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestCustomUser:

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="adminuser", email="admin@example.com", password="adminpassword"
        )
        assert admin_user.username == "adminuser"
        assert admin_user.email == "admin@example.com"
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser
