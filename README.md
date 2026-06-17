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

# Reflection - Part B. Step-by-Step Guide Using the Starter Kit
1. SpatialObject owns the geometry because geometry is a common property shared by all its subclasses. By placing geometric data and behavior in the SpatialObject base class, subclasses such as Parcel, Road, and Building can focus on their own specific attributes and functions. This reduces code duplication and makes the design simpler and easier to maintain.
2. There is no need to rewrite distance_to() in every subclass because distance calculation is a geometric function that is common to all spatial objects. Since geometric behavior is handled by the SpatialObject base class, Parcel, Road, and Building can inherit and use the same distance_to() method without duplicating code.
3. This supports abstraction by placing common geometric properties and behaviors in the SpatialObject base class, hiding those details from the subclasses. It supports reuse because subclasses such as Parcel, Road, and Building can inherit and use the same geometry-related methods instead of implementing them repeatedly, reducing code duplication and making the system easier to maintain.
