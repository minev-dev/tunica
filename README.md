# Skin

Light-weight Python ORM.

"Cover low-level with Skin"

Builtin features:
* ORM
  * Use [pydantic](https://github.com/pydantic/pydantic) models
  * Simple query builder:
    * `Model.all()`
    * `Model.filter(TODO).first()
  * Simple db configuration. Smart and automatic session management
  * Hide all low-level sql
* Migration tool (maybe call it `skin-care`?)
  * Fully automatic. Checks changes even if the source db doesn't support it (e.g. Enums in GCP Spanner). Compare state of the db with the changes history in all migrations.
    * Errors/Warnings if there are manual changes
  * Force to use migrations for data changes:
    * Move data from one table to another
    * Modify data in one table
    * ...
  * Implement in Rust?
* SQL Profiling tool (like [silk](https://github.com/jazzband/django-silk) for Django)

All these feature should be architected as independent as possible to be able to move them into another projects
