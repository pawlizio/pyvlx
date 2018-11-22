"""Unit tests for FrameGetNodeInformationConfirmation."""
import unittest
from pyvlx.frame_creation import frame_from_raw
from pyvlx.frame_get_node_information import FrameGetNodeInformationConfirmation


class TestFrameGetNodeInformationConfirmation(unittest.TestCase):
    """Test class for FrameGetNodeInformationConfirmation."""

    # pylint: disable=too-many-public-methods,invalid-name

    def test_discover_node_request(self):
        """Test FrameGetNodeInformationConfirmation."""
        frame = FrameGetNodeInformationConfirmation(node_id=23)
        self.assertEqual(bytes(frame), b'\x00\x05\x02\x01\x00\x17\x11')

    def test_discover_node_request_from_raw(self):
        """Test parse FrameGetNodeInformationConfirmation from raw."""
        frame = frame_from_raw(b'\x00\x05\x02\x01\x00\x17\x11')
        self.assertTrue(isinstance(frame, FrameGetNodeInformationConfirmation))
        self.assertEqual(frame.node_id, 23)

    def test_str(self):
        """Test string representation of FrameGetNodeInformationConfirmation."""
        frame = FrameGetNodeInformationConfirmation(node_id=23)
        self.assertEqual(
            str(frame),
            '<FrameGetNodeInformationConfirmation node_id=23 status=\'NodeInformationStatus.OK\'/>')