from app.calculator import add


def test_add():
    result = add(2, 3)

    assert result == 5
