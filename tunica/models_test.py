import tunica


class User(tunica.Model):
    name: tunica.String(name="", primary_key=False, max_length=5)


def test_filter():
    query = User.filter()

    assert isinstance(query, tunica.Query)
