from fmci import PointOfInterest, RoadSegment

def get_manila_data():
    """Simulates fetching records from PostGIS."""
    pois = [
        PointOfInterest("p1", "UP Manila", "Learning", 0.14),
        PointOfInterest("p2", "SM Manila", "Supplying", 0.11),
        PointOfInterest("p3", "PGH", "Caring", 0.20),
        PointOfInterest("p4", "Rizal Park", "Enjoying", 0.10),
        PointOfInterest("p5", "Intramuros Office", "Working", 0.9),
        PointOfInterest("p6", "Condo Unit", "Living", 0.10)
    ]
    
    roads = [
        RoadSegment("r1", (14.58, 120.98), (14.59, 120.98), 250),
        RoadSegment("r2", (14.59, 120.98), (14.59, 120.99), 300)
    ]
    
    return pois, roads