# littlelemon
## **Overview**

This is a capstone project in Django, specifically building an API for the Little Lemon restaurant using the Django REST Framework. 

This project has the following functions:
- Using Django to serve static HTML content.

- The application connects the backend to a MySQL database. Database is not available in Github.

- Menu and Table booking APIs are implemented.

- The application sets up with user registration and authentication.

- The application contains unit tests.

- The API be tested with the Insomnia REST client.

### Test
- Test customer-facing web functions by navigating through url *http://127.0.0.1:8000/*
    - **Home** page: shows static home page.
    - **About** page: shows static About page.
    - **Menu** page: shows all menu items.
    - **Book** page: accepts new reservations and returns confirmation.
- You may use the following credentials to test out the API.
    - Superuser
        - username: **admin** password: **admin**
    - Staff
        - usernmae: **Bob** password: **Pass123!**
    - To test Djoser, use the following:
        - GET *http://127.0.0.1:8000/auth/users* Embed with a valid credential -> Show all users. You can also use this endpoint to register a new user. 
        - POST *http://127.0.0.1:8000/auth/token/login/* Embed with a valid credential -> returns a token for the user. 
        - POST *http://127.0.0.1:8000/auth/token/logout/* Use this endpoint to logout user (remove user authentication token)
        - Test out Djoser API endpoints as shown in the [document](https://djoser.readthedocs.io/en/latest/getting_started.html). 
    - To test Menu APIs, use the following:
        - GET *http://127.0.0.1:8000/menu* -> Shows all Menu with no authentication needed. 
        - GET *http://127.0.0.1:8000/api/menu-items/\<int:pk>* Embed with a valid credential -> shows details of individual Menu items.
    - To test Booking API, use the following:
        - POST *http://127.0.0.1:8000/api/booking/tables* Embed with a valid credential-> Show all the bookings under the login user's name. If the login user is admin, then show all the bookings.
