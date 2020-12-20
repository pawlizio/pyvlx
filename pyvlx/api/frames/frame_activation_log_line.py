"""Frame for getting Activation Log Line."""
from pyvlx.const import Command
from pyvlx.dataobjects import DtoActivationLogLine

from .frame import FrameBase


class FrameGetActivationLogLineRequest(FrameBase):
    """Frame for getting Activation Log Line."""

    PAYLOAD_LEN = 2

    def __init__(self, linenumber=0):
        """Init Frame."""
        super().__init__(Command.GW_GET_ACTIVATION_LOG_LINE_REQ)
        self.linenumber = linenumber

    def get_payload(self):
        """Return Payload."""
        ret = self.linenumber.to_bytes(2, byteorder='big')
        return ret

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.linenumber = int.from_bytes(payload[0:2], "big")

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} linenumber="{}"/>'.format(
                type(self).__name__, self.linenumber
            )
        )


class FrameGetActivationLogLineConfirmation(FrameBase):
    """Frame for Activation Log Line."""

    PAYLOAD_LEN = 17

    def __init__(self):
        """Init Frame."""
        super().__init__(Command.GW_GET_ACTIVATION_LOG_LINE_CFM)
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
