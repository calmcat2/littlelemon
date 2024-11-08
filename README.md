This version includes slight feature differences compared to the original version. This version will be used for container image in the further development. 

This Django-based web application provides essential features, including:

1. **Table Reservation**
   - Customers can book reservations online. The reservation form displays available time slots starting today.

2. **Menu and Reservation Management**
   - Admin users can manage (add, edit, delete) the menu through the Django admin portal.

3. **API Access for Both Customers and Administrators**
   - Admin users have full rights to manage menus and reservations via the API.
   - Anyone can use the API to register an account.
   - Users can view menus and reservations under their name and modify or delete their reservations via the API.

This is a simple version of the project using an SQLite database (included) for demonstration purposes. You can download all files from the repository and follow these steps:

1. Run `pip install -r requirements.txt` in a virtual environment.
   - To create a virtual environment, run `python -m venv env` and then `source env/bin/activate` (or `env\Scripts\activate` on Windows).

2. Navigate to the **littlelemon** directory where `manage.py` is located. Run `python manage.py makemigrations` and then `python manage.py migrate`.

3. If everything is set up correctly, run `python manage.py runserver`.

4. The server should start on localhost at port 8000. In your browser, go to `http://127.0.0.1:8000/`.
   
5. To access the Django admin portal, use url `http://127.0.0.1:8000/admin`. An admin user is already created with username `admin` and password `Admin`.
   
### Available API Endpoints

- **Authentication**
  - `GET http://127.0.0.1:8000/auth/users`: Embed with valid credentials to show all users.
  - `POST http://127.0.0.1:8000/auth/users`: Register a new user by embedding a username and password in the body.
  - `POST http://127.0.0.1:8000/auth/token/login/`: Embed with valid credentials to receive a token for the user.
  - `POST http://127.0.0.1:8000/auth/token/logout/`: Use this endpoint to log out a user (remove user authentication token).
  - Test Djoser API endpoints as shown in the [documentation](https://djoser.readthedocs.io/en/latest/getting_started.html).

- **Menu**
  - `GET http://127.0.0.1:8000/menu`: Shows all menu items with no authentication needed.
  - `GET http://127.0.0.1:8000/api/menu-items/<int:pk>`: Embed with valid credentials to show details of individual menu items.

- **Reservation**
  - `GET http://127.0.0.1:8000/api/reservations/`
    - Embed with admin credentials to show all reservations.
    - Embed with user credentials to show all reservations under the logged-in user's name.
  - `POST http://127.0.0.1:8000/api/reservations/`: All authenticated users can create a reservation.
  - `PATCH http://127.0.0.1:8000/api/reservations/<int:pk>`
    - Embed with admin credentials to modify any reservation.
    - Embed with user credentials to modify a reservation only if it is under the user's name.
  - `DELETE http://127.0.0.1:8000/api/reservations/<int:pk>`
    - Embed with admin credentials to delete any reservation.
    - Embed with user credentials to delete a reservation only if it is under the user's name.