import sys
import unittest

sys.path.append('lib')
from ops.model import (
    MaintenanceStatus,
)

sys.path.append('src')
import handlers


class TestStartHandler(unittest.TestCase):

    def test_happy_path(self):
        # Set up
        event = object()

        # Exercise the code
        output = handlers.start(event)

        # Assertions
        assert type(output.unit_status) == MaintenanceStatus
        assert output.unit_status.message == "Great Success!"
