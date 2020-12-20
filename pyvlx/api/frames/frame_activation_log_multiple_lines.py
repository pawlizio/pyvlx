"""Frame for getting Multple Activation Log Lines."""
from datetime import datetime
from enum import Enum
from pyvlx.const import Command
from pyvlx.dataobjects import DtoActivationLogLine
from .frame import FrameBase


class FrameGetActivationLogLinesRequest(FrameBase):
    """Frame for getting Activation Log Line."""

    PAYLOAD_LEN = 4

    def __init__(self, timestamp=None):
        """Init Frame."""
        super().__init__(Command.GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_REQ)
        if timestamp is None:
            timestamp = datetime.fromtimestamp(0)
        self.timestamp = timestamp

    def get_payload(self):
        """Return Payload."""
        ret = int(self.timestamp.timestamp()).to_bytes(4, byteorder='big')
        return ret

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.timestamp = datetime.fromtimestamp(int.from_bytes(payload, "big"))

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} timestamp="{}"/>'.format(
                type(self).__name__, self.timestamp
            )
        )


class FrameGetActivationLogLinesNotification(FrameBase):
    """Frame for Activation Log Line."""

    PAYLOAD_LEN = 17

    def __init__(self):
        """Init Frame."""
        super().__init__(Command.GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_NTF)
        self.logline = None

    def get_payload(self):
        """Return Payload."""
        if self.logline is None:
            self.logline = DtoActivationLogLine()
        ret = self.logline.to_payload()
        return ret

    def from_payload(self, payload):
        """Init frame from binary data."""
        # KLF Returns 0x00 Log Entry if nothing is available
        if payload != b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00':
            self.logline = DtoActivationLogLine()
            self.logline.from_payload(payload)

    def __str__(self):
        """Return human readable string."""
        return (
            '<{0}>{1}</{0}>'.format(
                type(self).__name__, self.logline
            )
        )


class GetActivationLogLinesConfirmationStatus(Enum):
    """Enum class for status of get multiple loglines confirmation."""

    FAILED = 0
    SUCCESSFUL = 1


class FrameGetActivationLogLinesConfirmation(FrameBase):
    """Frame for Activation Log Line."""

    PAYLOAD_LEN = 3

    def __init__(self, linecount=0, status=GetActivationLogLinesConfirmationStatus.SUCCESSFUL):
        """Init Frame."""
        super().__init__(Command.GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_CFM)
        self.linecount = linecount
        self.status = status

    def get_payload(self):
        """Return Payload."""
        ret = b''
        ret = self.linecount.to_bytes(2, byteorder='big')
        ret += self.status.value.to_bytes(1, byteorder='big')
        return ret

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.linecount = int.from_bytes(payload[0:2], "big")
        self.status = GetActivationLogLinesConfirmationStatus(payload[2])

    def __str__(self):
        """Return human readable string."""
        return (
            '<{0} linecount="{1}" status="{2}"/>'.format(
                type(self).__name__, self.linecount, self.status
            )
        )
