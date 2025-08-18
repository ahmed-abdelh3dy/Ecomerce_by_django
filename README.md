# 🛒 E-commerce API with Django REST Framework

A full-featured **E-commerce RESTful API** built with Django & Django REST Framework, implementing authentication, product management, cart system, and order handling.  
The project uses **Simple JWT** for authentication and **role-based access control** for Admin and Customers.

---

## 🚀 Features

### 🔐 Authentication
- JWT-based authentication (login, register, profile).  
- Role-based access control (Admin / Customer).  

### 📂 Categories
- **Admin**: Full CRUD (Create, Read, Update, Delete).  
- **Customers/Public**: View categories.  

### 🛍️ Products
- **Admin**: Full CRUD operations.  
- **Customers**:  
  - Browse all products.  
  - Search products by name.  
  - Filter products by category and tags.  
  - View product details.  

### 🛒 Cart
- **Customers**:  
  - Add products to cart.  
  - Update quantity.  
  - Remove items.  
  - Full cart management.  

### 📦 Orders
- **Customers**:  
  - Place orders.  
  - View order history.  
  - Track order status (pending, shipped, delivered).  
- **Admin**:  
  - View all orders.  
  - Update order statuses.  

### 👥 Roles
- **Admin**:  
  - Manage categories.  
  - Manage products.  
  - Manage orders & update statuses.  
  - Manage customers.  
- **Customer**:  
  - Register & login.  
  - Manage cart.  
  - Place & view orders.  
  - Track orders.  
  - View personal profile & order history.  

---

## 🗄️ Database Schema (ERD)

| Users             | Categories        | Products          | Cart              | Orders                     | OrderItems           |
|-------------------|------------------|------------------|------------------|----------------------------|----------------------|
| id (pk)           | id (pk)          | id (pk)          | id (pk)          | id (pk)                    | id (pk)              |
| name              | name             | name             | user_id (fk)     | user_id (fk)               | order_id (fk)        |
| username          | description      | description      | product_id (fk)  | total_price                | product_id (fk)      |
| email             | image (many)     | image (many)     | quantity         | created_at                 | quantity             |
| password          | status           | status           | created_at       | payment_method             | price                |
| phone             |                  | category_id (fk) |                   | status (pending/shipped/…) |                      |
| role              |                  | stock            |                   |                            |                      |
| status            |                  | tags             |                   |                            |                      |
| city              |                  | price            |                   |                            |                      |
| address           |                  |                  |                   |                            |                      |

---

## 📌 API Endpoints


## 🔐 Authentication (Simple JWT)

- **POST** `/auth/register`: Register a new user.  
- **POST** `/auth/profile`: Get logged-in user's profile (personal info + order history).  
- **POST** `/auth/token/`: Obtain JWT token (login).  
- **POST** `/auth/token/refresh/`: Refresh access token.  
- **POST** `/auth/token/verify/`: Verify token validity.  

---

## 📂 Categories

- **GET** `   /api/categories`: Retrieve all categories.  
- **GET** `   /api/categories/<id>`: Retrieve a specific category.  
- **POST** `  /api/categories`: Create a new category (Admin only).  
- **PUT** `   /api/categories/<id>`: Update a category (Admin only).  
- **DELETE** `/api/categories/<id>`: Delete a category (Admin only).  

---

## 🛍️ Products

- **GET** `   /products`: Retrieve all products (supports search & filters).  
- **GET** `   /products/<id>`: Retrieve a specific product.  
- **POST** `  /products`: Create a new product (Admin only).  
- **PUT** `   /products/<id>`: Update an existing product (Admin only).  
- **PATCH** ` /products/<id>`: Update product status (active/inactive).  
- **DELETE** `/products/<id>`: Delete a product (Admin only).  

---

## 🛒 Cart

- **GET** `   /api/cart`: Retrieve all cart items (for logged-in customer).  
- **GET** `   /api/cart/<id>`: Retrieve a specific cart item.  
- **POST** `  /api/cart`: Add product to cart.  
- **PUT** `   /api/cart/<id>`: Update quantity of product in cart.  
- **DELETE** `/api/cart/<id>`: Remove product from cart.  

---

## 📦 Orders

- **GET** `   /api/orders`:  
  - Customers → Retrieve their orders.  
  - Admins → Retrieve all orders.  
- **GET** `   /api/orders/<id>`: Retrieve a specific order.  
- **POST** `  /api/orders`: Place a new order.  
- **PUT** `   /api/orders/<id>`: Update an order (Admin only).  
- **DELETE** `/api/orders/<id>`: Delete an order.  

---
