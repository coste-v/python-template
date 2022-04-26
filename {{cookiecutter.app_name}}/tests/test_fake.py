from {{cookiecutter.app_name}}.fake import fake


def test_fake():
    result = fake()
    assert result == 1
