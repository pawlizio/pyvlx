"""Unit tests for FrameGetActivationLogLineConfirmation."""
import unittest

from pyvlx.api.frame_creation import frame_from_raw
from pyvlx.api.frames import FrameGetActivationLogLineConfirmation
from pyvlx.dataobjects import DtoActivationLogLine


class FrameGetActivationLogLineConfirmationTest(unittest.TestCase):
    """Test class FrameGetActivationLogLineConfirmationTest."""

    # pylint: disable=too-many-public-methods,invalid-name

    EXAMPLE_FRAME = b"\x00\x14\x05\x05\x00\x00\x00\x00\x00\x00\xff\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x14"

    def test_bytes(self):
        """Test FrameActivationLogLine."""
        frame = FrameGetActivationLogLineConfirmation()
        frame.logline = DtoActivationLogLine()
        self.assertEqual(bytes(frame), self.EXAMPLE_FRAME)

    def test_frame_from_raw(self):
        """Test parse FrameActivationLogLine from raw."""
        frame = frame_from_raw(self.EXAMPLE_FRAME)
        self.assertTrue(isinstance(frame, FrameGetActivationLogLineConfirmation))

    def test_str(self):
        """Test string representation of FrameGetActivationLogLineConfirmation."""
        frame = FrameGetActivationLogLineConfirmation()
        frame.logline = DtoActivationLogLine()
        self.assertEqual(str(frame), '<FrameGetActivationLogLineConfirmation><DtoActivationLogLine timestamp="1970-01-01 01:00:00" '
                                     'sessionid="0" statusid="StatusId.STATUS_UNKNOWN" index="0" nodeparameter="NodeParameter.NOT_USED" '
                                     'parametervalue="0" runstatus="RunStatus.EXECUTION_COMPLETED" statusreply="StatusReply.UNKNOWN_STATUS_REPLY" '
                                     'informationcode="0"/></FrameGetActivationLogLineConfirmation>')
