"""Module for retrieving multiple Activation Log Entries from API."""
from datetime import datetime
from pyvlx.log import PYVLXLOG
from .api_event import ApiEvent
from .frames import (
    FrameGetActivationLogLinesRequest, FrameGetActivationLogLinesConfirmation,
    FrameGetActivationLogLinesNotification)


class GetActivationLogLines(ApiEvent):
    """Class for retrieving Activation Log Entries from API."""

    def __init__(self, pyvlx, timestamp=None):
        """Initialize GetActivationLogLines class."""
        super().__init__(pyvlx=pyvlx)
        self.success = False
        self.linecount = None
        self.receive_count = 0
        self.loglines = []
        if timestamp is None:
            timestamp = datetime.fromtimestamp(0)
        self.timestamp = timestamp

    async def handle_frame(self, frame):
        """Handle incoming API frame, return True if this was the expected frame."""
        if isinstance(frame, FrameGetActivationLogLinesConfirmation):
            self.linecount = frame.linecount
            if self.linecount == self.receive_count:
                self.success = True
            else:
                PYVLXLOG.warning(
                    "Warning: number of received loglines does not match expected number"
                )
            return True

        if isinstance(frame, FrameGetActivationLogLinesNotification):
            self.receive_count += 1
            self.loglines.append(frame.logline)
            return False

    def request_frame(self):
        """Construct initiating frame."""
        return FrameGetActivationLogLinesRequest(self.timestamp)
