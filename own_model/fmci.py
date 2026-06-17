from abc import ABC, abstractmethod
from enum import Enum


class SocialFunction(Enum):
    LIVING = "Living"
    WORKING = "Working"
    SUPPLYING = "Supplying"
    CARING = "Caring"
    LEARNING = "Learning"
    ENJOYING = "Enjoying"


class SpatialObject(ABC):
    def __init__(self, unique_id, geometry):
        self.unique_id = unique_id
        self.geometry = geometry

    @abstractmethod
    def get_info(self):
        pass


class PointOfInterest(SpatialObject):
    def __init__(self, unique_id, name, category: SocialFunction, weight, geometry=None):
        super().__init__(unique_id, geometry)
        self.name = name
        self.category = category
        self.weight = weight

    def get_info(self):
        return f"POI: {self.name} ({self.category.value}, weight={self.weight})"


class RoadSegment(SpatialObject):
    def __init__(self, unique_id, length_meters, geometry=None):
        super().__init__(unique_id, geometry)
        self.length = length_meters
        self.connected_pois = []  # relationship to POIs

    def add_poi_connection(self, poi: PointOfInterest):
        self.connected_pois.append(poi)

    def get_info(self):
        return f"RoadSegment {self.unique_id}: {self.length}m, connected POIs={len(self.connected_pois)}"


class CatchmentIsochrone(SpatialObject):
    def __init__(self, unique_id, time_limit, geometry=None):
        super().__init__(unique_id, geometry)
        self.time_limit = time_limit

        # relationships (composition/aggregation)
        self.pois = []
        self.roads = []

    # --- UML methods ---
    def add_poi(self, poi: PointOfInterest):
        self.pois.append(poi)

    def add_road(self, road: RoadSegment):
        self.roads.append(road)

    def calculate_completeness(self):
        return sum(poi.weight for poi in self.pois)

    def get_info(self):
        return f"Catchment {self.time_limit}min: {len(self.pois)} POIs, {len(self.roads)} roads"