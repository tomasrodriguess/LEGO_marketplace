# **Lego Marketplace Backend (Django REST Framework)**

## **Project Overview**

Lego Marketplace is a backend system built using Django and Django REST Framework (DRF). It serves as the foundation for a marketplace where users can browse, trade, and manage Lego sets. The project includes various user roles with different permissions for tasks like creating, listing, filtering, and trading Lego sets. 

## **Main Features**

1. **User Authentication and Authorization**:
   - Users can register, log in, and manage their profiles.
   - Token-based authentication using JWT.
   - Permissions and privileges are assigned based on user roles (e.g., normal users vs. staff users).

2. **Lego Sets Management**: 
   - Users can browse and filter available Lego sets.
   - Staff users can create, update, and delete Lego sets.
   - Normal users can add Lego sets to their personal collection.

3. **Search and Filter Functionality**:
   - Users can search for Lego sets by name or set number.
   - Lists of Lego sets can be filtered using query parameters (e.g., name, set number).

4. **Transactions**: (IN PROGRESS)
   - Users can perform transactions, such as trading Lego sets with one another.
   - Staff can oversee and manage these transactions.

5. **Role-Based Permissions**:
   - Normal users have restricted access to certain features (e.g., listing Lego sets).
   - Staff users (via `is_noderator`) can create, update, and delete Lego sets, as well as manage transactions.

6. **Collection Management**: 
   - Users can manage their personal Lego collections (add, remove, view).

## **Requirements**

- Python 3.9+
- Django 4.x
- Django REST Framework
- Simple JWT for token-based authentication
