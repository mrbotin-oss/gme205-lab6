# GmE 205 - Laboratory 6: From UML Class Diagram to Python Code

# Overview
- This Laboratory  identifies the core objects Parcel, Building, Road, and Household. Separates attributes from classes, assigns behaviors to the correct objects, and defines relationships between them. Implement our own UML-based system that emphasizes that OOAD is about structuring a system 
before coding, and that relationships are what make the system meaningful.

# Environment Setup
- Python 3.x    
- GitHub
- draw.io for UML diagram 

# How to run
1. Activate the virutal environment

# Reflection - Part B2. Spatial Object
1. SpatialObject owns the geometry because geometry is a common property shared by all its subclasses. By placing geometric data and behavior in the SpatialObject base class, subclasses such as Parcel, Road, and Building can focus on their own specific attributes and functions. This reduces code duplication and makes the design simpler and easier to maintain.
2. There is no need to rewrite distance_to() in every subclass because distance calculation is a geometric function that is common to all spatial objects. Since geometric behavior is handled by the SpatialObject base class, Parcel, Road, and Building can inherit and use the same distance_to() method without duplicating code.
3. This supports abstraction by placing common geometric properties and behaviors in the SpatialObject base class, hiding those details from the subclasses. It supports reuse because subclasses such as Parcel, Road, and Building can inherit and use the same geometry-related methods instead of implementing them repeatedly, reducing code duplication and making the system easier to maintain.

# Reflection - Part B4
1. Based on the requirements needed, the important attributes should be:
- SpatialObject (base class)
    geometry
- Parcel
    id
    area
    zone
- Building
    id
    height
    usage
- Road
    id
    length
    type
- Household
    id
    household-level information (population, income, num_of_people)
2. Each class contains methods that match its specific responsibilities: compute_area() is in Parcel, get_height() is in Building, get_length() is in Road, and calculate_total_income() is in Household.
3. Yes. Each object only contains data and behaviors that are relevant to its role. Parcel-specific information is kept in Parcel, building-related data is stored in Building, road properties belong to Road, and household information is contained in Household. This helps maintain clear responsibilities and avoids placing unrelated data in the wrong class.

# Reflection - Part B6
1. Yes. The spatial classes Parcel, Building, and Road correctly inherit from SpatialObject. Their class definitions explicitly show this relationship.
2. Yes. Each spatial class (Parcel, Building, and Road) calls super().__init__(geometry) in its constructor to ensure the shared geometric properties from SpatialObject are properly initialized.
3. Yes. Shared methods defined in SpatialObject, such as geometric operations, are inherited by Parcel, Building, and Road instead of being rewritten in each class. This ensures consistent behavior and avoids code duplication.

# Reflection - Part B Summary
1. Parent class: SpatialObject became the parent class.
2. Inherited classes: Parcel, Building, and Road inherit from SpatialObject.
3. Shared methods: Geometric methods (such as distance_to() and describe()) are shared through SpatialObject and reused by all spatial subclasses instead of being rewritten.
4. Relationships implemented: Inheritance is used for the spatial hierarchy (Parcel, Building, Road → SpatialObject), and object relationships are also modeled, such as a Building belonging to a Parcel and a Household belonging to a Building.

# Reflection - Part C Summary
1. The classes in my own model are:
- SpatialObject (abstract base class): 
    Defines shared attributes like:
        unique_id
        geometry
    Defines abstract method:
        get_info()  
- PointOfInterest (POI): represents facilities or amenities in the city (e.g., hospital, market, school)
    attributes:
        name
        category (from SocialFunction)
        weight (importance score)
    method:
        get_info()
- RoadSegment: represents a road or pathway in the network
    attributes:
        length
        connected_pois (relationships to POIs)
    methods:
        add_poi_connection()
        get_info()
- CatchmentIsochrone: represents the 15-minute accessibility zone
    attributes:
        time_limit
        pois (list of POIs within reach)
        roads (list of connected road segments)
    methods:
        add_poi()
        add_road()
        calculate_completeness()
        get_info()
- SocialFunction (Enum class): defines categories of human activity
    Values include:
        LIVING
        WORKING
        SUPPLYING
        CARING
        LEARNING
        ENJOYING
2. The attributes that became object state are unique_id, geometry, name, category, weight, length, time_limit, and the relationship lists such as pois, roads, and connected_pois, because these are all stored in each object’s __init__ and define its current data and relationships.
3. The methods that became behaviors are get_info(), add_poi(), add_road(), add_poi_connection(), and calculate_completeness(), because they define what the objects can do such as describing themselves, managing relationships, and computing accessibility scores.
4. The hardest relationships to implement were the many-to-many associations between CatchmentIsochrone, PointOfInterest, and RoadSegment, because they require careful management of object references through lists to correctly model how multiple POIs and roads connect within a single catchment and across road networks.

# Final Reflection 
1. Attributes were the easiest to translate into code because they are just variables placed in __init__, while methods were a bit harder since they need logic, and inheritance was the hardest because I had to make sure the classes were correctly connected and structured.
2. The hardest relationship to implement was the many-to-many relationship between CatchmentIsochrone, PointOfInterest, and RoadSegment, because it required carefully managing lists of object references to correctly represent how multiple POIs and road segments are shared within a single catchment.
3. The code did not exactly match the UML at first, and I had to revise some parts during implementation, especially the relationships between classes and how POIs and road segments were stored and connected using lists of object references.
4. From this exercise, I learned that Object-Oriented Analysis and Design (OOAD) is important because it helps break a complex system into clear classes with defined responsibilities, and it makes it easier to translate a model like a UML diagram into working code by organizing attributes, methods, and relationships in a structured way.