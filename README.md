B2B E-Commerce Platform
######

Overview

This project is a powerful B2B e-commerce platform built using Python, Django, and REST API. It is designed to streamline how shop owners list and sell machines and plastic products, providing an efficient and scalable solution for business transactions.

Features

For Shop Owners:

Easily list machines and plastic products with images, descriptions, and pricing.

Manage inventory with simple add/delete functionality.

For Buyers:

Effortlessly inquire about machines with auto-filled details.

Add multiple plastic products to orders, adjust quantities, and see the total cost before submitting.

Order & Inquiry Management:

When a user submits an inquiry or order, the system instantly sends all details to the shop owner via email.

Ensures a seamless and efficient business process.

Scalability & Performance:

Built for scalability to handle real-world business needs.

Implements RESTful APIs for a smooth user experience.

Tech Stack

Backend: Python, Django, Django REST Framework (DRF)

Database: PostgreSQL / SQLite (depending on deployment)

Frontend: HTML, CSS, JavaScript (or React if used)

Email Service: Django Email Backend (SMTP / third-party service)

Deployment: Docker, Nginx, Gunicorn (if applicable)

Installation

Clone the Repository:

git clone https://github.com/Rajat652000/GD_WEB.git
cd GD_WEB

Set up a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:

Apply Migrations:

python manage.py migrate

Create a Superuser (for admin access):

python manage.py createsuperuser

Run the Development Server:

python manage.py runserver

Access the platform at: http://127.0.0.1:8000/

API Endpoints (Sample)

GET /api/products/ - Retrieve the list of products.

POST /api/inquiries/ - Submit an inquiry.

POST /api/orders/ - Place an order.

Deployment

For production deployment:

Use Gunicorn and Nginx for server hosting.

Deploy using Docker (if containerized).

Set up environment variables for security.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

License

This project is licensed under the MIT License.

Contact

For any inquiries or suggestions, feel free to reach out!