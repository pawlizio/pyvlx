"""Frame for getting Activation Log Header."""
from pyvlx.const import Command

from .frame import FrameBase


class FrameGetActivationLogHeaderRequest(FrameBase):
    """Frame for getting Activation Log Header."""

    PAYLOAD_LEN = 0

    def __init__(self):
        """Init Frame."""
        super().__init__(Command.GW_GET_ACTIVATION_LOG_HEADER_REQ)


class FrameGetActivationLogHeaderConfirmation(FrameBase):
    """Frame for Activation Log Header."""

    PAYLOAD_LEN = 4

    def __init__(self, maxlinecount=0, linecount=0):
        """Init Frame."""
        super().__init__(Command.GW_GET_ACTIVATION_LOG_HEADER_CFM)
        self.maxlinecount = maxlinecount
        self.linecount = linecount

    def get_payload(self):
        """Return Payload."""
        ret = self.maxlinecount.to_bytes(2, byteorder='big')
        ret += self.linecount.to_bytes(2, byteorder='big')
        return ret

    def from_payload(self, payload):
        """Init frame from binary data."""
        self.maxlinecount = int.from_bytes(payload[0:2], "big")
        self.linecount = int.from_bytes(payload[2:4], "big")

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} maxlinecount="{}" linecount="{}" />'.format(
                type(self).__name__, self.maxlinecount, self.linecount
            )
        )
