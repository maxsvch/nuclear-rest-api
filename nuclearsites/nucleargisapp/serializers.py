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

"""API Serializers"""

# pylint: disable=too-few-public-methods
# from rest_framework_gis import serializers
from rest_framework import serializers

from .models import NuclearSite


class NuclearSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NuclearSite
        geo_field = "location"
        fields = ("id", "name", "power_mw", "reactor_type", "location")
