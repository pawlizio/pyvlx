"""Unit tests for FrameGetActivationLogLines."""
import unittest
from datetime import datetime

from pyvlx.api.frame_creation import frame_from_raw
from pyvlx.api.frames import FrameGetActivationLogLinesRequest


class FrameGetActivationLogLinesRequestTest(unittest.TestCase):
    """Test class FrameGetActivationLogLinesRequestTest."""

    # pylint: disable=too-many-public-methods,invalid-name

    EXAMPLE_FRAME = b"\x00\x07\x05\x07\x00\x00\x00\x00\x05"

    def test_bytes(self):
        """Test FrameActivationLogLines."""
        frame = FrameGetActivationLogLinesRequest()
        frame.timestamp = datetime.fromtimestamp(0)
        self.assertEqual(bytes(frame), self.EXAMPLE_FRAME)

    def test_frame_from_raw(self):
        """Test parse FrameActivationLogLine from raw."""
        frame = frame_from_raw(self.EXAMPLE_FRAME)
        self.assertTrue(isinstance(frame, FrameGetActivationLogLinesRequest))

    def test_str(self):
        """Test string representation of FrameGetActivationLogLinesRequest."""
        frame = FrameGetActivationLogLinesRequest()
        frame.linenumber = 1
        self.assertEqual(str(frame), '<FrameGetActivationLogLinesRequest timestamp="1970-01-01 01:00:00"/>')
