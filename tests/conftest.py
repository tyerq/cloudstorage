import os

from tempfile import NamedTemporaryFile
from pathlib import Path

import pytest

from tests import settings


PWD_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = PWD_PATH / "data"


@pytest.fixture(scope="session")
def text_filename():
    return str(DATA_PATH / settings.TEXT_FILENAME)


@pytest.fixture(scope="function")
def text_stream(text_filename):
    with open(text_filename, "rb") as text_stream:
        yield text_stream


@pytest.fixture(scope="session")
def binary_filename():
    return str(DATA_PATH / Path(settings.BINARY_FILENAME))


@pytest.fixture(scope="function")
def binary_stream(binary_filename):
    with open(binary_filename, "rb") as binary_stream:
        yield binary_stream


@pytest.fixture(scope="function")
def temp_file():
    with NamedTemporaryFile(prefix=settings.CONTAINER_PREFIX) as temp_file:
        yield temp_file.name