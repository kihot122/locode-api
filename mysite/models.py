from django.db import models

class Location(models.Model):
    LOCODE = models.CharField(max_length=5)
    NameWoDiacritics = models.CharField(max_length=50)
    Port = models.BooleanField("Is a port")
    RailwayTerminal = models.BooleanField("Is a rail terminal")
    RoadTerminal = models.BooleanField("Is a road terminal")
    Airport = models.BooleanField("Is an airport")
    PostalExchange = models.BooleanField("Is a postal exchange office")
    MultimodalFunction = models.BooleanField("Multimodal function")
    FixedTransportFunction = models.BooleanField("Fixed transport function")
    BorderCrossing = models.BooleanField("Is a border crossing")
    Unknown = models.BooleanField("Unknown function")
    Date = models.DateField()
    Coords = models.CharField(max_length=12)
