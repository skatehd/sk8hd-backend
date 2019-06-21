# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta
from unittest.mock import patch, call
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import *

class TestUser(TestCase):

    

    @staticmethod
    def createusercall(client, username="testuser", email="test@me.com", password="thisisavalidpassword", format="json"):
        return client.post(reverse('rest_register'), {
            'username': username,
            'password1': password,
            'password2': password,
            'email': email
        }, **{"HTTP_USER_AGENT": "konekti-android", "HTTP_CLIENT": "OPO test"},
                           format=format)


    def test_create(self):
        """
        Test creation of a user
        """
        client = APIClient()

        response = self.createusercall(client, username="testusername")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response)




