import copy

from fastapi.testclient import TestClient
import pytest

from src.app import activities, app


@pytest.fixture(autouse=True)
def preserve_activities():
    """Restore the in-memory activities state after each test."""
    original_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)


@pytest.fixture
def client():
    return TestClient(app)
