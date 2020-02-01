import sys
import unittest
from unittest.mock import (
    call,
    patch
)

sys.path.append('src')
sys.path.append('lib')

import handlers


class TestStartHandler(unittest.TestCase):

    @patch('handlers.MaintenanceStatus')
    def test_happy_path(self, mock_maint_status_cls):
        # Set up
        event = object()

        # Exercise the code
        output = handlers.start(event)

        # Assertions
        assert mock_maint_status_cls.call_count == 1
        assert mock_maint_status_cls.call_args \
            == call("Great Success!")

        assert output.unit_status == mock_maint_status_cls.return_value
