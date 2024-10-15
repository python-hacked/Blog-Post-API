Django Blog
This project is a Django-based REST API application that supports user authentication, a blogging platform, product inventory management, and payment processing. It leverages the Django REST Framework (DRF), JSON Web Tokens (JWT) for authentication, and integrates a third-party payment gateway (e.g., Stripe or PayPal). The database is managed with either MySQL or PostgreSQL, and the entire application is dockerized for easy setup and deployment.

Features
User Authentication with Role-Based Access Control
Implemented using Django REST Framework and JWT.
Supports user roles: Admin and Regular User.
Secure user sessions with JWT.
Blog API
Users can create, read, update, and delete blog posts.
Categorization of posts with support for categories and comments.
Pagination and filtering options (e.g., by category or author).
Product Inventory Management
Manage products with attributes like name, category, price, and stock.
Search functionality on product names and descriptions.
Filtering options by price, availability, or category.
Third-Party Payment Gateway Integration
Integrate with Stripe or PayPal for payment processing.
Complete checkout flow with secure API communication.
Payment status updates and error handling.
Models
1. User Model
Fields: role, author, name, email, password, created_at, updated_at.
Roles: Admin and User.
2. Category Model
Fields: name, description, created_at, updated_at.
Represents categories of blog posts and products.
3. Post Model
Fields: title, content, user, category, created_at, updated_at.
Represents blog posts with an association to users and categories.
4. Comment Model
Fields: content, post, user, created_at, updated_at.
Represents comments on blog posts.
5. Product Model
Fields: name, category, price, stock.
Represents a product with pricing and stock information.
6. Payment Model
Fields: order, payment_method, payment_id, payment_status, created_at, updated_at.
Represents payment transactions with status options (Success/Failed).
Tasks
Task 1: User Authentication with JWT
Create user registration and login endpoints.
Implement JWT for secure user sessions.
Add role-based access control for Admin and Regular Users.
Task 2: Blog API Development
Design models for Post, Category, and Comment.
Implement CRUD operations for blog posts.
Include pagination and filtering options for posts.
Task 3: Product Inventory Search and Filtering
Develop the Product model with fields like name, category, price, and stock.
Implement search functionality on product names and descriptions.
Add filtering options by price range, availability, or category.
Task 4: Payment Gateway Integration
Integrate Stripe or PayPal for payment processing.
Create a checkout flow and handle payment callbacks.
Ensure secure communication and error handling for transactions.
Technologies Used
Backend: Django, Django REST Framework
Authentication: JSON Web Tokens (JWT)
Database: MySQL or PostgreSQL
Payment Gateway: Stripe or PayPal
Containerization: Docker
Testing and Documentation: Postman

docker-compose up --build

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

