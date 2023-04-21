from __future__ import annotations

from typing import Self, Type

import pydantic


class Model(pydantic.BaseModel):
    """Base table model

    Supported methods:
    - Create - `Model(..fields..).save()`
    - Read:
        1) All:
            ```
            Model.all()
            ```
        2) One:
            ```
            Model.get(id=123)
            or
            Model.filter(id=123).first()
            ```
    - Update:
        1) Get and update:
            ```
            instance = Model.get()
            instance.name = "new name"
            instance.save()
            ```
        2) Update statement:
            ```
            Model.filter(..conditions..).update(name="new name")
            ```
    - Delete:
        1) Should be filtered first:
            ```
            Model.filter(..conditions..).delete()
            ```
        2) One:
            ```
            instance = Model.get(id=123)
            instance.delete()
            ```



    TODO:
        How to allow at the same time:
        - Model creation for validation
            `Model(..fields..)`
        - Query definition using static methods
            `Model.filter().order_by().first()`

        Possible solutions:
        - (Preferable) Duplicate interim methods (static in the Model and object-level in Query)
            that initially create Query instance
        - Use manager approach as Django does - `Model.objects.filter()`
            - Use shorter version - `Model.q.filter()`
            - Use another field for model-level actions
                `Model.t.create()` (creates table)

            Issues:
            - `q` has to be valid field of Pydantic model
            - Class properties are not natively supported since 3.11
                (https://docs.python.org/3.11/library/functions.html#classmethod)
    """

    @classmethod
    def filter(cls, **kwargs):
        return cls._create_query().filter(**kwargs)

    @classmethod
    def _create_query(cls) -> Query:
        return Query(model=cls)


class Query:
    """TODO: Define data structure and sql builder"""

    _model: Type[Model]

    def __init__(self, model: Type[Model]):
        self._model = model

    # Interim methods
    def filter(self, **kwargs) -> Self:
        return self

    def order_by(self, **kwargs) -> Self:
        return self

    # Finishing methods
    def create(self):
        pass

    def get(self):
        pass

    def all(self):
        pass

    def first(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def count(self) -> int:
        pass

    def exists(self) -> bool:
        pass
