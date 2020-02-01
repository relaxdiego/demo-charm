#!/usr/bin/env python3.6

import sys
from types import SimpleNamespace
sys.path.append('lib')

from ops.charm import CharmBase
from ops.main import main
from ops.model import (
    MaintenanceStatus,
)


class DemoCharm(CharmBase):

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.start, self)

    def on_start(self, event):
        output = OnStartHandler().handle(event)
        self.framework.model.unit.status = output.unit_status


class OnStartHandler:

    def handle(self, event):
        output = {
            'unit_status': MaintenanceStatus("Great Success!")
        }
        return SimpleNamespace(**output)


if __name__ == "__main__":
    main(DemoCharm)
