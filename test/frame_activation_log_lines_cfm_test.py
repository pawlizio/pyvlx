"""Unit tests for FrameGetActivationLogLinesConfirmation."""
import unittest

from pyvlx.api.frame_creation import frame_from_raw
from pyvlx.api.frames import FrameGetActivationLogLinesConfirmation


class FrameGetActivationHeaderConfirmation(unittest.TestCase):
    """Test class FrameGetActivationLogLinesConfirmation."""

    # pylint: disable=too-many-public-methods,invalid-name

    EXAMPLE_FRAME = b"\x00\x06\x05\t\x00\x00\x01\x0b"

    def test_bytes(self):
        """Test FrameActivationHeader."""
        frame = FrameGetActivationLogLinesConfirmation()
        self.assertEqual(bytes(frame), self.EXAMPLE_FRAME)

    def test_frame_from_raw(self):
        """Test parse FrameActivationHeader from raw."""
        frame = frame_from_raw(self.EXAMPLE_FRAME)
        self.assertTrue(isinstance(frame, FrameGetActivationLogLinesConfirmation))

    def test_str(self):
        """Test string representation of FrameGetActivationLogLinesConfirmation."""
        frame = FrameGetActivationLogLinesConfirmation()
        self.assertEqual(str(frame), '<FrameGetActivationLogLinesConfirmation linecount="0" '
                                     'status="GetActivationLogLinesConfirmationStatus.SUCCESSFUL"/>')
