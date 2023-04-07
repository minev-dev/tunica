from pydantic.types import Type
from pydantic.types import errors


class StringType(str):
    length: int

    @classmethod
    def __get_validators__(cls):
        """Returns validators applied to this type"""
        yield cls.str_length_validator

    @classmethod
    def str_length_validator(
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


def _string(max_length: int) -> Type:
    # use kwargs then define conf in a dict to aid with IDE type hinting
    namespace = dict(max_length=max_length)

    return type("StringField", (StringType,), namespace)


String = _string
