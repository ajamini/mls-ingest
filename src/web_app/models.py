from django.contrib.postgres.fields import ArrayField
from django.db import models


class Source(models.Model):
    name = models.TextField(null=True)


class Listing(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    type = models.TextField(null=True)
    created_at = models.TextField(null=True)
    last_updated = models.TextField(null=True)
    mls = models.TextField(null=True)
    status = models.TextField(null=True)
    price = models.TextField(null=True)
    description = models.TextField(null=True)
    extra_description = models.TextField(null=True)
    possession_notes = models.TextField(null=True)
    media_updated_at = models.TextField(null=True)
    media_updated = models.BooleanField(default=True)


class Room(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    sequence = models.SmallIntegerField()
    width = models.TextField(null=True)
    length = models.TextField(null=True)
    level = models.TextField(null=True)
    features = ArrayField(models.TextField(null=True))


class Washroom(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    sequence = models.SmallIntegerField()
    pieces = models.TextField(null=True)
    level = models.TextField(null=True)


class Location(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
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
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
    linked = models.NullBooleanField()
    bedrooms = models.IntegerField(null=True)
    bedrooms_plus = models.IntegerField(null=True)
    kitchens = models.IntegerField(null=True)
    kitchens_plus = models.IntegerField(null=True)
    washrooms = models.IntegerField(null=True)
    washrooms_plus = models.IntegerField(null=True)
    style = models.TextField(null=True)
    approx_age = models.TextField(null=True)
    square_ft = models.TextField(null=True)
    garage_type = models.TextField(null=True)
    garage_spaces = models.TextField(null=True)
    parking_spaces = models.TextField(null=True)


class Agent(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
    name = models.TextField(null=True)
    brokerage = models.TextField(null=True)


class Photo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    sequence = models.SmallIntegerField()
    path = models.TextField(null=True)
    identifier = models.TextField(null=True)
    mime_type = models.TextField(null=True)


class Land(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
    acreage = models.TextField(null=True)
    access_type = models.TextField(null=True)
    zoning = models.TextField(null=True)
    lot_depth = models.TextField(null=True)
    lot_length = models.TextField(null=True)
