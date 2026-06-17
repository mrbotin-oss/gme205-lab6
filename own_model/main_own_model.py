from fmci import PointOfInterest, CatchmentIsochrone, SocialFunction, RoadSegment


def main():
    print("--- Initializing 15-Minute City Model ---")

    # 1. Create POIs
    hospital = PointOfInterest("p1", "Manila General", SocialFunction.CARING, 0.10)
    market = PointOfInterest("p2", "Public Market", SocialFunction.SUPPLYING, 0.15)
    school = PointOfInterest("p3", "City University", SocialFunction.LEARNING, 0.05)

    # 2. Create Roads
    road1 = RoadSegment("r1", 500)
    road2 = RoadSegment("r2", 300)

    # 3. Create Catchment (15-minute isochrone)
    catchment_15 = CatchmentIsochrone("c1", 15)

    # 4. Establish UML Relationships
    catchment_15.add_poi(hospital)
    catchment_15.add_poi(market)
    catchment_15.add_poi(school)

    catchment_15.add_road(road1)
    catchment_15.add_road(road2)

    road1.add_poi_connection(hospital)
    road1.add_poi_connection(market)

    road2.add_poi_connection(school)

    # 5. Demonstrate system behavior
    print(f"\nAnalyzing {catchment_15.time_limit}-minute walk radius:")

    for poi in catchment_15.pois:
        print(f" - Found: {poi.get_info()}")

    for road in catchment_15.roads:
        print(f" - Road: {road.get_info()}")

    score = catchment_15.calculate_completeness()
    print(f"\nTotal Neighborhood Completeness Score: {score * 100:.2f}%")


if __name__ == "__main__":
    main()