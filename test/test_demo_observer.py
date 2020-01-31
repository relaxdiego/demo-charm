from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import (
    call,
    MagicMock,
    Mock,
    patch
)

sys.path.append('src')
sys.path.append('lib')

from ops.framework import (
    EventBase,
    Framework
)
from charm import DemoObserver


class TestDemoObserver(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmpdir)

    def create_framework(self):
        framework = Framework(self.tmpdir / "framework.data",
                              self.tmpdir, None, None)
        self.addCleanup(framework.close)
        framework.model = Mock()
        framework.model.unit = Mock()
        return framework

    @patch('charm.MaintenanceStatus')
    def test__on_start__happy_path(self, mock_status_cls):
        mock_framework = self.create_framework()
        mock_event = MagicMock(EventBase)
        observer = DemoObserver(mock_framework)

        observer.on_start(mock_event)

        assert mock_status_cls.call_count == 1
        assert mock_status_cls.call_args \
            == call("It's new! It's shiny! It's quite buggy!")

        assert mock_framework.model.unit.status \
            == mock_status_cls.return_value
