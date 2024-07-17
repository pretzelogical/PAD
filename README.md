# PAD
Political accountability database


## Files

```
manage.py: Django's management cli
common/
  models: Common models used across the website (Politician organization)
  admin: Admin registrations for the models
```

## How to run

```shell
# Install requirements
pip install -r requirements.txt

# Initialize database
python3 manage.py migrate

# Create an admin account
python3 manage.py createsuperuser

# Run server
python3 manage.py runserver

# Login to admin in your browser at localhost:8000/admin

# Profit!
```
