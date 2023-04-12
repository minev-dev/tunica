import pydantic
import pytest

import tunica


class User(pydantic.BaseModel):
    name: tunica.String(name="", primary_key=False, max_length=5)


def test_string():
    string_type = tunica.String(name="", primary_key=False, max_length=5)

    assert hasattr(string_type, "max_length")


def test_string_length_validator_failed():
    with pytest.raises(pydantic.ValidationError):
        _ = User(name="123456")
