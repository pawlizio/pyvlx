"""Unit tests for FrameGetActivationLogHeaderConfirmation."""
import unittest

from pyvlx.api.frame_creation import frame_from_raw
from pyvlx.api.frames import FrameGetActivationLogHeaderConfirmation


class FrameGetActivationHeaderConfirmation(unittest.TestCase):
    """Test class FrameGetActivationLogHeaderConfirmation."""

    # pylint: disable=too-many-public-methods,invalid-name

    EXAMPLE_FRAME = b"\x00\x07\x05\x01\x00\xc8\x00J\x81"

    def test_bytes(self):
        """Test FrameActivationHeader."""
        frame = FrameGetActivationLogHeaderConfirmation()
        frame.maxlinecount = 200
        frame.linecount = 74
        self.assertEqual(bytes(frame), self.EXAMPLE_FRAME)

    def test_frame_from_raw(self):
        """Test parse FrameActivationHeader from raw."""
        frame = frame_from_raw(self.EXAMPLE_FRAME)
        self.assertTrue(isinstance(frame, FrameGetActivationLogHeaderConfirmation))

    def test_str(self):
        """Test string representation of FrameGetActivationLogHeaderConfirmation."""
        frame = FrameGetActivationLogHeaderConfirmation()
        frame.maxlinecount = 200
        frame.linecount = 74
        self.assertEqual(str(frame), '<FrameGetActivationLogHeaderConfirmation maxlinecount="200" linecount="74" />')
