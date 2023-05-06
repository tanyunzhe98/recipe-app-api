"""
Tests for the Django admin modification
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='19981024tyz',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='admin@example.com',
            password='19981024tyz',
            name="Test User"
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse('adminicore_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)