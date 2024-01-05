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

"""API Views"""

# from django.shortcuts import render
# pylint: disable=no-member
from rest_framework import generics

from .models import NuclearSite
from .serializers import NuclearSiteSerializer


class NuclearSiteListCreateView(generics.ListCreateAPIView):
    queryset = NuclearSite.objects.all()
    serializer_class = NuclearSiteSerializer


class NuclearSiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NuclearSite.objects.all()
    serializer_class = NuclearSiteSerializer