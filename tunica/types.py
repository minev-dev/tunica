"""Tunica ORM field types

Each field type consist of:
1) Class with pydantic validators
2) Wrapper for the class with supported named args
"""
from pydantic.types import Type
from pydantic.types import errors


class _BaseWrapper:
    """Wrapper for a custom pydantic field type"""

    def __init__(self, klass: Type):
        self._klass = klass

    def __call__(self, name: str, primary_key: bool) -> Type:
        """Defines supported params for the field

        Args:
            name: Column name
            primary_key: If this field is a primary key

        Returns:
            New type with custom namespace and base class that was set in `__init__`
        """
        namespace = dict(name=name, primary_key=primary_key)

        return type(self._klass.__name__, (self._klass,), namespace)


class Field:
    """Class-marker for fields implementations"""

    pass


class _String(str, Field):
    @classmethod
    def __get_validators__(cls):
        """Returns validators applied to this type"""
        yield cls._str_length_validator

    @classmethod
    def _str_length_validator(
        cls, v: "StrBytes", field: "ModelField", config: "BaseConfig"
    ) -> "StrBytes":
        """Custom validator for length checks

        TODO: Update typing
        """
        v_len = len(v)

        length = field.type_.max_length
        if v_len > length:
            raise errors.PydanticValueError(limit_value=length)

        return v


class _StringWrapper(_BaseWrapper):
    def __call__(self, name: str, primary_key: bool, max_length: int) -> Type:
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
