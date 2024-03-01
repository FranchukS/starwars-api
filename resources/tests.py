from __future__ import unicode_literals

from django.test import TestCase

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship
)

import json

class TestAllEndpoints(TestCase):
    """ Test ALL the endpoints """
    fixtures = [
        "planets.json",
        "people.json",
        "species.json",
        "starships.json",
        "vehicles.json",
        "transport.json",
        "films.json"
    ]

    def get_query(self, url):
        return self.client.get(url)

    def test_people_root(self):
        self.assertEqual(
            self.get_query("/people/").status_code, 200)

    def test_people_schema(self):
        self.assertEqual(
            self.get_query("/people/schema").status_code, 200)

    def test_people_search(self):
        response = self.get_query("/people/?search=r2")
        json_data = json.loads(response.content)
        person = People.objects.get(name='R2-D2')
        self.assertEqual(response.status_code, 200)

        list_response = self.get_query("/people/")
        list_data = json.loads(list_response.content)
        self.assertLess(json_data["count"],list_data["count"])
        self.assertEqual(person.name, json_data["results"][0]["name"])

    def test_planets_root(self):
        self.assertEqual(
            self.get_query("/planets/").status_code, 200)

    def test_planets_schema(self):
        self.assertEqual(
            self.get_query("/planets/schema").status_code, 200)

    def test_planets_search(self):
        response = self.get_query("/planets/?search=yavin")
        json_data = json.loads(response.content)
        planet = Planet.objects.get(name='Yavin IV')
        self.assertEqual(response.status_code, 200)

        list_response = self.get_query("/planets/")
        list_data = json.loads(list_response.content)
        self.assertLess(json_data["count"],list_data["count"])
        self.assertEqual(planet.name, json_data["results"][0]["name"])

    def test_films_root(self):
        self.assertEqual(
            self.get_query("/films/").status_code, 200)

    def test_films_schema(self):
        self.assertEqual(
            self.get_query("/films/schema").status_code, 200)

    def test_films_search(self):
        response = self.get_query("/films/?search=sith")
        json_data = json.loads(response.content)
        film = Film.objects.get(title='Revenge of the Sith')
        self.assertEqual(response.status_code, 200)

        list_response = self.get_query("/films/")
        list_data = json.loads(list_response.content)
        self.assertLess(json_data["count"],list_data["count"])
        self.assertEqual(film.title, json_data["results"][0]["title"])

    def test_starships_root(self):
        self.assertEqual(
            self.get_query("/starships/").status_code, 200)

    def test_starship_schema(self):
        self.assertEqual(
            self.get_query("/starships/schema").status_code, 200)

    def test_starship_search(self):
        response = self.get_query("/starships/?search=x1")
        json_data = json.loads(response.content)
        ship = Starship.objects.get(name='TIE Advanced x1')
        self.assertEqual(response.status_code, 200)

        list_response = self.get_query("/starships/")
        list_data = json.loads(list_response.content)
        self.assertLess(json_data["count"],list_data["count"])
        self.assertEqual(ship.name, json_data["results"][0]["name"])

    def test_vehicles_root(self):
        self.assertEqual(
            self.get_query("/vehicles/").status_code, 200)

    def test_vehicle_schema(self):
        self.assertEqual(
            self.get_query("/vehicles/schema").status_code, 200)

    def test_vehicle_search(self):
        response = self.get_query("/vehicles/?search=crawler")
        json_data = json.loads(response.content)
        vehicle = Vehicle.objects.get(name='Sand Crawler')
        self.assertEqual(response.status_code, 200)

        list_response = self.get_query("/vehicles/")
        list_data = json.loads(list_response.content)
        self.assertLess(json_data["count"],list_data["count"])
        self.assertEqual(vehicle.name, json_data["results"][0]["name"])

    def test_species_root(self):
        self.assertEqual(
            self.get_query("/species/").status_code, 200)

    def test_species_schema(self):
        self.assertEqual(
            self.get_query("/species/schema").status_code, 200)

    def test_species_search(self):
        response = self.get_query("/species/?search=calamari")
        json_data = json.loads(response.content)
        species = Species.objects.get(name='Mon Calamari')
        self.assertEqual(response.status_code, 200)

        list_response = self.get_query("/species/")
        list_data = json.loads(list_response.content)
        self.assertLess(json_data["count"],list_data["count"])
        self.assertEqual(species.name, json_data["results"][0]["name"])

    def test_people_detail(self):
        response = self.get_query("/people/1/")
        json_data = json.loads(response.content)
        person = People.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(person.name, json_data["name"])

    def test_planets_detail(self):
        response = self.get_query("/planets/1/")
        json_data = json.loads(response.content)
        planet = Planet.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(planet.name, json_data["name"])

    def test_films_detail(self):
        response = self.get_query("/films/1/")
        json_data = json.loads(response.content)
        film = Film.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(film.title, json_data["title"])

    def test_starships_detail(self):
        response = self.get_query("/starships/2/")
        json_data = json.loads(response.content)
        starship = Starship.objects.get(pk=2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(starship.name, json_data["name"])

    def test_vehicles_detail(self):
        response = self.get_query("/vehicles/4/")
        json_data = json.loads(response.content)
        vehicle = Vehicle.objects.get(pk=4)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(vehicle.name, json_data["name"])

    def test_species_detail(self):
        response = self.get_query("/species/1/")
        json_data = json.loads(response.content)
        specie = Species.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(specie.name, json_data["name"])

    def test_etag(self):
        valid_etag = self.get_query("/")["ETag"]
        self.client.defaults['HTTP_IF_NONE_MATCH'] = valid_etag
        self.assertEqual(
            self.get_query("/").status_code, 304)
