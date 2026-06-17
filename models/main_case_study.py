from parcel import Parcel
from building import Building
from road import Road
from household import Household


def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    # ---------------------------------------------------------
    # 1. Create parcels
    # ---------------------------------------------------------
    p1 = Parcel(
        parcel_id="P001",
        geometry={"x": 10, "y": 10},
        area=500.0,
        zone="Residential"
    )

    p2 = Parcel(
        parcel_id="P002",
        geometry={"x": 40, "y": 12},
        area=800.0,
        zone="Commercial"
    )

    # ---------------------------------------------------------
    # 2. Create buildings and assign them to parcels
    # ---------------------------------------------------------
    b1 = Building(
        building_id="B001",
        geometry={"x": 11, "y": 10},
        height=12.5,
        usage="Residential",
        parcel=p1
    )

    b2 = Building(
        building_id="B002",
        geometry={"x": 41, "y": 12},
        height=20.0,
        usage="Mixed-use",
        parcel=p2
    )

    # ---------------------------------------------------------
    # 3. Create road and connect it to parcels
    # ---------------------------------------------------------
    r1 = Road(
        road_id="R001",
        geometry={"x": 25, "y": 10},
        length=120.0,
        road_type="Collector"
    )

    r1.add_adjacent_parcel(p1)
    r1.add_adjacent_parcel(p2)

    # ---------------------------------------------------------
    # 4. Create households and assign them to buildings
    # ---------------------------------------------------------
    h1 = Household(
        household_id="H001",
        num_people=4,
        income=25000,
        tenure_type="Owner",
        building=b1
    )

    h2 = Household(
        household_id="H002",
        num_people=3,
        income=18000,
        tenure_type="Renter",
        building=b1
    )

    h3 = Household(
        household_id="H003",
        num_people=5,
        income=42000,
        tenure_type="Owner",
        building=b2
    )

    # ---------------------------------------------------------
    # 5. Show object descriptions
    # ---------------------------------------------------------
    print_header("PARCELS")
    print(p1.describe())
    print(p2.describe())

    print_header("BUILDINGS")
    print(b1.describe())
    print(b2.describe())

    print_header("ROAD")
    print(r1.describe())

    print_header("HOUSEHOLDS")
    print(h1.describe())
    print(h2.describe())
    print(h3.describe())

    # ---------------------------------------------------------
    # 6. Demonstrate class-specific behaviors
    # ---------------------------------------------------------
    print_header("CLASS-SPECIFIC METHODS")
    print(f"{p1.parcel_id} area: {p1.compute_area()}")
    print(f"{b1.building_id} height: {b1.get_height()}")
    print(f"{r1.road_id} length: {r1.get_length()}")
    print(f"{h1.household_id} total income: {h1.calculate_total_income()}")
    print(f"{b1.building_id} combined household income: {b1.total_household_income()}")

    # ---------------------------------------------------------
    # 7. Demonstrate shared spatial behavior
    # ---------------------------------------------------------
    print_header("SHARED SPATIAL BEHAVIOR")
    print(f"Distance from {p1.parcel_id} to {p2.parcel_id}: {p1.distance_to(p2):.2f}")
    print(f"Distance from {b1.building_id} to {r1.road_id}: {b1.distance_to(r1):.2f}")
    print(f"Does {p1.parcel_id} intersect {b1.building_id}? {p1.intersects(b1, threshold=2.0)}")

    # ---------------------------------------------------------
    # 8. Demonstrate relationships explicitly
    # ---------------------------------------------------------
    print_header("RELATIONSHIPS")
    print(f"Building {b1.building_id} is located on Parcel {b1.parcel.parcel_id}")
    print(f"Building {b2.building_id} is located on Parcel {b2.parcel.parcel_id}")

    for household in b1.households:
        print(f"Household {household.household_id} lives in Building {b1.building_id}")

    for household in b2.households:
        print(f"Household {household.household_id} lives in Building {b2.building_id}")

    for parcel in r1.adjacent_parcels:
        print(f"Road {r1.road_id} is adjacent to Parcel {parcel.parcel_id}")

    # ---------------------------------------------------------
    # 9. Small analysis examples
    # ---------------------------------------------------------
    print_header("SIMPLE ANALYSIS")
    print(f"Total households in {b1.building_id}: {len(b1.households)}")
    print(f"Total households in {b2.building_id}: {len(b2.households)}")

    richer_building = b1 if b1.total_household_income() > b2.total_household_income() else b2
    print(
        f"Building with higher total household income: "
        f"{richer_building.building_id} ({richer_building.total_household_income()})"
    )


if __name__ == "__main__":
    main()