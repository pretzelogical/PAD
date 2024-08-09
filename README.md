# SAFED

State And Federal Entity Database

## Overview

SAFED (State And Federal Entity Database) is a Django-based project aimed at managing and displaying information about state and federal entities, such as politicians and organizations.
<!---
Will update structure later.
-->
```
## Project Structure

SAFED/
├── manage.py        # Django's management CLI
├── PAD/
│   └── settings.py  # Configuration for the entire project
└── common/
    ├── models.py    # Common models used across the website (e.g., Politician, Organization)
    └── admin.py     # Admin registrations for the models
```

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.x
- Django
- Node.js and npm

### Installation

1. **Clone the repository:**

   ```shell
   git clone <repository_url>
   cd SAFED
   ```

2. **Install Python dependencies:**

   ```shell
   pip install -r requirements.txt
   ```

   #### requirements.txt
   ```
   beautifulsoup4==4.12.3
   Django==5.0.7
   Requests==2.32.3
   pillow==10.4.0
   django-htmx==1.18.0
   ```

3. **Initialize the database:**

   ```shell
   python3 manage.py migrate
   ```

4. **Create an admin account:**

   ```shell
   python3 manage.py createsuperuser
   ```

5. **Install Node.js dependencies:**

   ```shell
   npm install
   ```

### Running the Application

1. **Start the Django development server:**

   ```shell
   npm run dev
   ```

2. **Access the admin interface:**

   Open your web browser and navigate to `http://localhost:8000/admin`. Log in with the admin account you created earlier.

### Profit!

You are now ready to use SAFED to manage and display information about state and federal entities.