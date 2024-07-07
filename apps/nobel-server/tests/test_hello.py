"""Hello unit test module."""

from nobel_server.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello nobel-server"
