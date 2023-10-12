import pydantic
import pytest

import tunica


class User(tunica.Model):
    name: tunica.String(name="", primary_key=False, max_length=5)


def test_string():
    string_type = tunica.String(name="Some name", primary_key=False, max_length=5)

    assert hasattr(string_type, "name")
    assert hasattr(string_type, "primary_key")
    assert hasattr(string_type, "max_length")


def test_string_length_validator_failed():
    with pytest.raises(pydantic.ValidationError):
        _ = User(name="123456")


# Failing
def test_dict():
    user = User(name="1234")

    print(user.model_dump(mode="json"))
