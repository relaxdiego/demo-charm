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

        # Ensure that this charm keeps a reference to the observer so that
        # it doesn't get garbage collected when initialization is done.
        self.observer = DemoObserver(self)

        # This call makes the framework call an `on_start` method on the
        # observer when the `start` event is emmitted.
        self.framework.observe(self.on.start, self.observer)


class DemoObserver(framework.Object):

    def __init__(self, charm):
        # As of operator framework 90b9bb13, the second argument is required.
        super().__init__(charm, None)

    def on_start(self, event):
        self.framework.model.unit.status = \
            MaintenanceStatus("It's new! It's shiny! It's quite buggy!")
        return


if __name__ == "__main__":
    main(DemoCharm)
