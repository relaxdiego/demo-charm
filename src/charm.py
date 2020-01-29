#!/usr/bin/env python3.6

import os
cwd = os.getcwd()
print(cwd)

import sys
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
        self.framework.model.unit.status = \
            MaintenanceStatus('Configuring container')
        return


if __name__ == "__main__":
    main(DemoCharm)
