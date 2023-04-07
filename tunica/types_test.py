import pydantic
import pytest

import tunica


class User(pydantic.BaseModel):
    name: tunica.String(max_length=5)


def test_string():
    string_type = tunica.String(max_length=10)

    assert hasattr(string_type, "max_length")


def test_string_length_validator_failed():
    with pytest.raises(pydantic.ValidationError):
        _ = User(name="123456")
