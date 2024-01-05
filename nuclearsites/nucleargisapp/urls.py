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

"""API Urls"""

from django.urls import path

from .views import NuclearSiteDetailView, NuclearSiteListCreateView

urlpatterns = [
    path("nuclear-sites/", NuclearSiteListCreateView.as_view(), name="nuclear-site-list-create"),
    path("nuclear-sites/<int:pk>/", NuclearSiteDetailView.as_view(), name="nuclear-site-detail"),
]
