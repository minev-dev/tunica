"""Tunica ORM field types

Each field type consist of:
1) Class with pydantic validators
2) Wrapper for the class with supported named args
"""
from typing import Any

import pydantic
import pydantic_core
from pydantic_core import core_schema


class _BaseWrapper:
    """Wrapper for a custom pydantic field type"""

    def __init__(self, class_):
        self._class = class_

    def __call__(self, name: str, primary_key: bool):
        """Defines supported params for the field

        Args:
            name: Column name
            primary_key: If this field is a primary key

        Returns:
            New type with custom namespace and base class that was set in `__init__`
        """
        namespace = dict(name=name, primary_key=primary_key)

        return type(self._class.__name__, (self._class,), namespace)


class Field:
    """Class-marker for fields implementations"""

    pass


class _String:
    """Custom type that stores the field it was used in."""

    def __init__(self, value: str, field_name: str):
        self.value = value
        self.field_name = field_name

    def __repr__(self):
        return f"String<{self.value} {self.field_name!r}>"

    @classmethod
    def validate(cls, value: str, info: pydantic.ValidationInfo):
        value_len = len(value)

        if value_len > cls.max_length:
            # TODO: Raise correct error
            raise pydantic_core.PydanticCustomError("length", "Wrong length")

        return cls(value, info.field_name)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: pydantic.GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.with_info_after_validator_function(
            cls.validate, handler(str), field_name=handler.field_name
        )


class _StringWrapper(_BaseWrapper):
    def __call__(self, name: str, primary_key: bool, max_length: int):
        """Overrides base method to add extra String-specific args

        Args:
            max_length: Max length of the string in a db

        Returns:
            Modified type returned from the parent
        """
        type_ = super().__call__(name, primary_key)

        namespace = dict(max_length=max_length)

        for k, v in namespace.items():
            setattr(type_, k, v)

        return type_


# Put all public types here
String = _StringWrapper(_String)
