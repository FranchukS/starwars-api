from __future__ import unicode_literals

from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from resources import views

router = routers.DefaultRouter()

router.register(r"people", views.PeopleViewSet)
router.register(r"planets", views.PlanetViewSet)
router.register(r"films", views.FilmViewSet)
router.register(r"species", views.SpeciesViewSet)
router.register(r"vehicles", views.VehicleViewSet)
router.register(r"starships", views.StarshipViewSet)


urlpatterns = patterns("",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^$", "swapi.views.index"),
    url(r"^documentation$", "swapi.views.documentation"),
    url(r"^people/schema$", "resources.schemas.people"),
    url(r"^planets/schema$", "resources.schemas.planets"),
    url(r"^films/schema$", "resources.schemas.films"),
    url(r"^species/schema$", "resources.schemas.species"),
    url(r"^vehicles/schema$", "resources.schemas.vehicles"),
    url(r"^starships/schema$", "resources.schemas.starships"),
    url(r"^", include(router.urls)),
)
