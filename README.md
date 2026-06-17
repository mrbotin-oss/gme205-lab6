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
