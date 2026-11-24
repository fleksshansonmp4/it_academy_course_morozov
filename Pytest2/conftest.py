import os
import pytest

@pytest.fixture(scope="function", autouse=True)
def env_setup():
    os.environ["APP_MODE"] = "testing"
    yield
    del os.environ["APP_MODE"]


@pytest.fixture(scope="function", autouse=False, params=[2,4,6,8])
def number(request):
    return request.param