"""Unit tests for FrameGetActivationLogLine."""
import unittest

from pyvlx.api.frame_creation import frame_from_raw
from pyvlx.api.frames import FrameGetActivationLogLineRequest


class FrameGetActivationLogLineRequestTest(unittest.TestCase):
    """Test class FrameGetActivationLogLineRequestTest."""

    # pylint: disable=too-many-public-methods,invalid-name

    EXAMPLE_FRAME = b"\x00\x05\x05\x04\x00\x01\x05"

    def test_bytes(self):
        """Test FrameActivationLogLine."""
        frame = FrameGetActivationLogLineRequest()
        frame.linenumber = 1
        self.assertEqual(bytes(frame), self.EXAMPLE_FRAME)

    def test_frame_from_raw(self):
        """Test parse FrameActivationLogLine from raw."""
        frame = frame_from_raw(self.EXAMPLE_FRAME)
        self.assertTrue(isinstance(frame, FrameGetActivationLogLineRequest))

    def test_str(self):
        """Test string representation of FrameGetActivationLogLineRequest."""
        frame = FrameGetActivationLogLineRequest()
        frame.linenumber = 1
        self.assertEqual(str(frame), '<FrameGetActivationLogLineRequest linenumber="1"/>')
