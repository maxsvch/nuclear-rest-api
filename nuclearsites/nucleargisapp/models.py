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

"""API Models"""

from django.contrib.gis.db import models as gis_models
from django.db import models


class NuclearSite(models.Model):
    """NuclearSite model"""

    name = models.CharField(max_length=255)
    power_mw = models.FloatField()
    reactor_type = models.CharField(max_length=255)
    location = gis_models.PointField(srid=4326)

    def __str__(self):
        return str(self.name)
