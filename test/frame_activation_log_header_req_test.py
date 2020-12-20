"""Unit tests for FrameGetActivationHeader."""
import unittest

from pyvlx.api.frame_creation import frame_from_raw
from pyvlx.api.frames import FrameGetActivationLogHeaderRequest


class FrameGetActivationHeaderRequest(unittest.TestCase):
    """Test class FrameGetActivationHeaderRequest."""

    # pylint: disable=too-many-public-methods,invalid-name

    EXAMPLE_FRAME = b"\x00\x03\x05\x00\x06"

    def test_bytes(self):
        """Test FrameActivationHeader."""
        frame = FrameGetActivationLogHeaderRequest()
        self.assertEqual(bytes(frame), self.EXAMPLE_FRAME)

    def test_frame_from_raw(self):
        """Test parse FrameActivationHeader from raw."""
        frame = frame_from_raw(self.EXAMPLE_FRAME)
        self.assertTrue(isinstance(frame, FrameGetActivationLogHeaderRequest))

    def test_str(self):
        """Test string representation of FrameGetActivationLogHeaderRequest."""
        frame = FrameGetActivationLogHeaderRequest()
        self.assertEqual(str(frame), "<FrameGetActivationLogHeaderRequest/>")
