import pydantic
import pytest

import tunica


class User(pydantic.BaseModel):
    name: tunica.String(length=5)


def test_string():
    string_type = tunica.String(length=10)

    assert hasattr(string_type, "length")


def test_string_length_validator_failed():
    with pytest.raises(pydantic.ValidationError):
        _ = User(name="123456")
