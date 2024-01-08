# Copyright 2023 Maximilien Soviche.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""API Tests"""

# pylint: disable=no-member
from django.contrib.gis.geos import Point
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import NuclearSite

# from .serializers import NuclearSiteSerializer


class NuclearSiteModelTestCase(TestCase):
    """Model test case"""

    def setUp(self):
        NuclearSite.objects.create(
            name="Test Site", power_mw=1000.0, reactor_type="Test Reactor", location=Point(0, 0, srid=4326)
        )

    def test_nuclear_site_model(self):
        """Test NuclearSite model elements"""

        test_site = NuclearSite.objects.get(name="Test Site")
        self.assertEqual(test_site.power_mw, 1000.0)
        self.assertEqual(test_site.reactor_type, "Test Reactor")
        self.assertEqual(test_site.location.x, 0)
        self.assertEqual(test_site.location.y, 0)


class NuclearSiteAPITestCase(TestCase):
    """API test case"""

    def setUp(self):
        self.client = APIClient()
        self.site_data = {
            "name": "New Site",
            "power_mw": 1500.0,
            "reactor_type": "New Reactor",
            "location": Point(1, 1, srid=4326),
        }
        # self.site_data = {
        #     "name": "New Site",
        #     "power_mw": 1500.0,
        #     "reactor_type": "New Reactor",
        #     "location": "POINT(1 1)",
        # }
        # self.site_data = {
        #     "type": "Feature",
        #     "properties": {
        #         "name": "New Site",
        #         "power_mw": 1500.0,
        #         "reactor_type": "New Reactor",
        #     },
        #     "geometry": {
        #         "type": "Point",
        #         "coordinates": [1, 1]
        #     }
        # }

    def test_create_nuclear_site(self):
        """Test POST operation on nuclear sites API"""

        url = reverse("add-nuclear-site")
        response = self.client.post(url, self.site_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NuclearSite.objects.count(), 1)
        self.assertEqual(NuclearSite.objects.get().name, "New Site")

    def test_retrieve_nuclear_site(self):
        """Test GET operation on nuclear sites API"""

        NuclearSite.objects.create(**self.site_data)
        response = self.client.get("/api/nuclear-sites/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "New Site")

    def test_update_nuclear_site(self):
        """Test PUT operation on nuclear sites API"""

        NuclearSite.objects.create(**self.site_data)
        updated_data = {
            "name": "Updated Site",
            "power_mw": 2000.0,
            "reactor_type": "Updated Reactor",
            "location": Point(2, 2, srid=4326),
        }
        # updated_data = {
        #     "name": "Updated Site",
        #     "power_mw": 2000.0,
        #     "reactor_type": "Updated Reactor",
        #     "location": "POINT(2 2)",
        # }
        # updated_data = {
        #     "type": "Feature",
        #     "properties": {
        #         "name": "Updated Site",
        #         "power_mw": 2000.0,
        #         "reactor_type": "Updated Reactor",
        #     },
        #     "geometry": {
        #         "type": "Point",
        #         "coordinates": [2, 2]
        #     }
        # }
        response = self.client.put("/api/nuclear-sites/1/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(NuclearSite.objects.get().name, "Updated Site")

    def test_delete_nuclear_site(self):
        """Test DELETE operation on nuclear sites API"""

        NuclearSite.objects.create(**self.site_data)
        response = self.client.delete("/api/nuclear-sites/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NuclearSite.objects.count(), 0)

    def test_list_nuclear_sites(self):
        """Test GET operation for all nuclear sites API elements"""

        NuclearSite.objects.create(**self.site_data)
        response = self.client.get("/api/nuclear-sites/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
