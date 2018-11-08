"""Unit tests for FramePasswordEnterConfirmation."""
import unittest
from pyvlx.frame_creation import frame_from_raw
from pyvlx.frame_password_enter import FramePasswordEnterConfirmation, PasswordEnterConfirmationStatus


class TestFramePasswordEnterConfirmation(unittest.TestCase):
    """Test class for FramePasswordEnterConfirmation."""

    # pylint: disable=too-many-public-methods,invalid-name

    def test_discover_node_request(self):
        """Test FramePasswordEnterConfirmation."""
        frame = FramePasswordEnterConfirmation()
        self.assertEqual(bytes(frame), b'\x00\x040\x01\x005')

    def test_discover_node_request_error(self):
        """Test failed FramePasswordEnterConfirmation."""
        frame = FramePasswordEnterConfirmation(status=PasswordEnterConfirmationStatus.FAILED)
        self.assertEqual(bytes(frame), b'\x00\x040\x01\x014')

    def test_discover_node_request_from_raw(self):
        """Test parse FramePasswordEnterConfirmation from raw."""
        frame = frame_from_raw(b'\x00\x040\x01\x014')
        self.assertTrue(isinstance(frame, FramePasswordEnterConfirmation))
        self.assertEqual(frame.status, PasswordEnterConfirmationStatus.FAILED)

    def test_str(self):
        """Test string representation of FramePasswordEnterConfirmation."""
        frame = FramePasswordEnterConfirmation()
        self.assertEqual(
            str(frame),
            '<FramePasswordEnterConfirmation status=\'PasswordEnterConfirmationStatus.SUCCESSFUL\'/>')
