from django.contrib.postgres.fields import ArrayField
from django.db import models


class Source(models.Model):
    name = models.TextField(null=True)


class Listing(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    type = models.TextField(null=True)
    created_at = models.TextField(blank=True)
    last_updated = models.TextField(null=True)
    mls = models.TextField(null=True)
    status = models.TextField(null=True)
    price = models.TextField(null=True)
    description = models.TextField(null=True)
    extra_description = models.TextField(null=True)
    possession_notes = models.TextField(null=True)


class Room(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    width = models.TextField(null=True)
    length = models.TextField(null=True)
    level = models.TextField(null=True)
    features = ArrayField(models.TextField(null=True))


class Washroom(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    pieces = models.TextField(null=True)
    level = models.TextField(null=True)


class Location(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    fronting_on = models.TextField(null=True)
    full_address = models.TextField(null=True)
    street_name = models.TextField(null=True)
    street_number = models.TextField(null=True)
    street_abbrev = models.TextField(null=True)
    street_direction = models.TextField(null=True)
    apt_num = models.TextField(null=True)
    province = models.TextField(null=True)
    postal_code = models.TextField(null=True)
    area = models.TextField(null=True)
    municipality = models.TextField(null=True)
    community = models.TextField(null=True)
    district = models.TextField(null=True)


class Building(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    linked = models.NullBooleanField()
    bathrooms = models.SmallIntegerField(null=True)
    bathrooms_plus = models.SmallIntegerField(null=True)
    bedrooms = models.SmallIntegerField(null=True)
    bedrooms_plus = models.SmallIntegerField(null=True)
    kitchens = models.TextField(blank=True)
    kitchens_plus = models.TextField(blank=True)
    washrooms = models.TextField(blank=True)
    washrooms_plus = models.TextField(blank=True)
    style = models.TextField(blank=True)
    approx_age = models.TextField(blank=True)
    square_ft = models.TextField(blank=True)
    garage_type = models.TextField(blank=True)
    garage_spaces = models.TextField(blank=True)
    parking_spaces = models.TextField(blank=True)


class Agent(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    brokerage = models.TextField(blank=True)


class Photo(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
    sequence = models.SmallIntegerField()
    path = models.TextField(blank=True)
    identifier = models.TextField(blank=True)
    mime_type = models.TextField(blank=True)


class Land(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
    acreage = models.TextField(blank=True)
    access_type = models.TextField(blank=True)
    zoning = models.TextField(blank=True)
    lot_depth = models.TextField(blank=True)
    lot_length = models.TextField(blank=True)
