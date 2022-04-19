from src.fake import fake


def test_fake():
    result = fake()
    assert result == 1
