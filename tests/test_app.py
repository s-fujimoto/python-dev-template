import app


def test_home():
    expect = "Hello, Flask!"
    actual = app.home()

    assert expect == actual


def test_hello():
    name = "abc"
    expect = "Hello, abc"

    actual = app.hello_there(name)

    assert expect == actual
