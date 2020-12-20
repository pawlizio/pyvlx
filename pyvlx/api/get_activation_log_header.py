"""Module for retrieving activation log headers from API."""
from .api_event import ApiEvent
from .frames import (
    FrameGetActivationLogHeaderConfirmation, FrameGetActivationLogHeaderRequest)


class GetActivationLogHeader(ApiEvent):
    """Class for retrieving scene list from API."""

    def __init__(self, pyvlx):
        """Initialize SceneList class."""
        super().__init__(pyvlx=pyvlx)
        self.success = False
        self.maxlinecount = 0
        self.linecount = 0

    async def handle_frame(self, frame):
        """Handle incoming API frame, return True if this was the expected frame."""
        if isinstance(frame, FrameGetActivationLogHeaderConfirmation):
            self.maxlinecount = frame.maxlinecount
            self.linecount = frame.linecount
            self.success = True
            return True
        return False

    def request_frame(self):
        """Construct initiating frame."""
        return FrameGetActivationLogHeaderRequest()
