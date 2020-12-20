"""Module for retrieving activation Log Line from API."""

from .api_event import ApiEvent
from .frames import (
    FrameGetActivationLogLineRequest, FrameGetActivationLogLineConfirmation)


class GetActivationLogLine(ApiEvent):
    """Class for retrieving scene list from API."""

    def __init__(self, pyvlx, linenumber=0):
        """Initialize SceneList class."""
        super().__init__(pyvlx=pyvlx)
        self.success = False
        self.linenumber = linenumber
        self.logline = None

    async def handle_frame(self, frame):
        """Handle incoming API frame, return True if this was the expected frame."""
        if isinstance(frame, FrameGetActivationLogLineConfirmation):
            self.logline = frame.logline
            self.success = True
            return True
        return False

    def request_frame(self):
        """Construct initiating frame."""
        return FrameGetActivationLogLineRequest(self.linenumber)
