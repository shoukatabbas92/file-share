# file-share

This completes the implementation of the file sharing project using Django and Django Rest Framework. Here's a summary of what we've created:

1. User authentication (login and register) using Django's built-in User model and custom views.
2. File upload functionality with automatic ZIP file creation.
3. File download functionality with download counting.
4. API endpoints for user registration, login, file upload, and file download.
5. Basic frontend templates for user interaction.
6. Styling with CSS for a clean and responsive design.


To run this project:

1. Install the required packages: `pip install django djangorestframework`
2. Run migrations: `python manage.py makemigrations core` and `python manage.py migrate`
3. Create a superuser: `python manage.py createsuperuser`
4. Start the development server: `python manage.py runserver`


This implementation showcases advanced Django and DRF features, including:

- Custom user authentication
- File handling and ZIP creation
- RESTful API design
- Integration of frontend and backend
- Use of Django's ORM for database operations
- Proper separation of concerns (models, views, serializers, utils)


You can further enhance this project by adding features like:

- Email verification for user registration
- Password reset functionality
- File sharing with specific users
- Expiring download links
- Advanced file management (rename, delete, etc.)
