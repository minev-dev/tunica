# Tunica

Light-weight Python ORM.

"Wear a Tunica on your low-level code"

## Installation

```commandline
pip install tunica
```

## Basic usage

```python
import tunica


class User(tunica.Model):
    id: tunica.UUID(primary_key=True)

    first_name: tunica.String(max_length=32)
    last_name: tunica.String(max_length=32)


# Creates table
User.create()

# Create users
user_1 = User(first_name="John", last_name="Smith", save=True)
user_2 = User(first_name="Harry", last_name="Potter", save=True)

# Get all users
users = User.all()
```

Priorities:

- Query builder:
  - How to store query structure
  - How to build sql upon the structure
- Base migration (create, alter table)

Builtin features:

- ORM
  - Use [pydantic](https://github.com/pydantic/pydantic) models
    - Native `pydantic` validation. Use models as DTO, serializers
  - Simple query builder:
    - `Model.all()`
    - `Model.filter(TODO).first()`
  - Simple db configuration. Smart and automatic session management
  - Hide all low-level sql
  - Native Python exceptions
- Migration tool
  - Fully automatic. Checks changes even if the source db doesn't support it (e.g. Enums in GCP Spanner). Compare
    state of the db with the changes history in all migrations.
    - Errors/Warnings if there are manual changes
  - Force to use migrations for data changes:
    - Move data from one table to another
    - Modify data in one table
    - ...
  - Implement in Rust?
- SQL Profiling tool (like [silk](https://github.com/jazzband/django-silk) for Django)
- FastAPI integration
- Mock for testing (like [alchemy-mock](https://github.com/miki725/alchemy-mock))

All these features should be architected as independent as possible to be able to move them into another projects

## Development

### Setup venv

```bash
poetry install
```
