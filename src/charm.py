#!/usr/bin/env python3.6

import logging
logger = logging.getLogger(__name__)

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
        logger.debug("Initializing charm")
        super().__init__(*args)
        observer = DemoObserver(self)
        self.framework.observe(self.on.start, observer.on_start)


class DemoObserver(framework.Object):

    def __init__(self, charm):
        super().__init__(charm, "1")

    def on_start(self, event):
        self.framework.model.unit.status = \
            MaintenanceStatus("It's new! It's shiny! It's quite buggy!")
        return


if __name__ == "__main__":
    main(DemoCharm)
