#!/usr/bin/env python3.6

import sys
sys.path.append('lib')

from ops import framework
from ops.charm import CharmBase
from ops.main import main
from ops.model import (
    MaintenanceStatus,
)


class DemoCharm(CharmBase):

    def __init__(self, *args):
        super().__init__(*args)
        observer = DemoObserver(self.framework, None)
        self.framework.observe(self.on.start, observer)


class DemoObserver(framework.Object):

    def __init__(self, parent, key):
        super().__init__(parent, key)
        self.seen = []
        self.done = {}

    def on_start(self, event):
        self.framework.model.unit.status = \
            MaintenanceStatus("It's new! It's shiny! It's quite buggy!")
        return


if __name__ == "__main__":
    main(DemoCharm)
