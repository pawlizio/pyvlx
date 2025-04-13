"""Module for retrieving node information from API."""
from typing import TYPE_CHECKING, Optional

from .api_event import ApiEvent
from .frames import (
    FrameBase, FrameGetSystemTableDataNotification, FrameGetSystemTableDataRequest, FrameGetSystemTableDataConfirmation)

if TYPE_CHECKING:
    from pyvlx import PyVLX


class GetSystemtableData(ApiEvent):
    """Class for retrieving node informationfrom API."""

    def __init__(self, pyvlx: "PyVLX"):
        """Initialize SceneList class."""
        super().__init__(pyvlx=pyvlx)
        self.success = False
        self.notification_frame: Optional[FrameGetSystemTableDataNotification] = None

    async def handle_frame(self, frame: FrameBase) -> bool:
        """Handle incoming API frame, return True if this was the expected frame."""
        if (
                isinstance(frame, FrameGetSystemTableDataConfirmation)
        ):
            # We are still waiting for GetNodeInformationNotification
            return False
        if (
                isinstance(frame, FrameGetSystemTableDataNotification)
        ):
            self.notification_frame = frame
            self.success = True
            return False
        return False

    def request_frame(self) -> FrameGetSystemTableDataRequest:
        """Construct initiating frame."""
        return FrameGetSystemTableDataRequest()
