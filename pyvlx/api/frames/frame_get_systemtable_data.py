"""Module for get system table data from gateway."""
from dataclasses import dataclass
from pyvlx.const import Command, NodeType, PowerMode
from pyvlx.log import PYVLXLOG

from .frame import FrameBase


class FrameGetSystemTableDataRequest(FrameBase):
    """Frame for get system table data request."""

    PAYLOAD_LEN = 0

    def __init__(self) -> None:
        """Init Frame."""
        super().__init__(Command.GW_CS_GET_SYSTEMTABLE_DATA_REQ)


class FrameGetSystemTableDataConfirmation(FrameBase):
    """Frame for confirmation for get system table data request."""

    PAYLOAD_LEN = 0

    def __init__(self) -> None:
        """Init Frame."""
        super().__init__(Command.GW_CS_GET_SYSTEMTABLE_DATA_CFM)


class FrameGetSystemTableDataNotification(FrameBase):
    """Frame for notification of all nodes information request."""

    def __init__(self) -> None:
        """Init Frame."""
        super().__init__(Command.GW_GET_ALL_NODES_INFORMATION_NTF)
        self.payload: bytes = bytes()
        self.number_of_objects: int = 0
        self.system_table_object: list[SystemTableObject] = []
        self.remaining_number_of_entry: int = 0

    def from_payload(self, payload: bytes) -> None:
        self.payload = payload
        self.number_of_objects = payload[0]
        for obj in range(self.number_of_objects):
            data: bytes = payload[obj*11+1:obj*11+12]
            PYVLXLOG.debug("SystemTableObject: " + ":".join("{:02x}".format(c) for c in data))
            sys_obj = SystemTableObject(
                index=data[0],
                actuator_address=":".join("{:02x}".format(c) for c in data[1:4]),
                actuator_type=NodeType(int.from_bytes(data[4:6], byteorder='big') >> 6),
                actuator_subtype=str(data[5] & 0x3F),
                power_save_mode=PowerMode(bool(data[6] & (1 << 1))),
                io_membership=bool(data[6] & (1 << 2)),
                rf_support=bool(data[6] & (1 << 3)),
                actuator_turnaround_time=(data[6] >> 6),
                io_manufacturer_id=data[7],
                backbone_reference=":".join("{:02x}".format(c) for c in data[8:11])
            )
            self.system_table_object.append(sys_obj)

        if self.number_of_objects > 0:
            self.remaining_number_of_entry = payload[self.number_of_objects*11+1]
        else:
            self.remaining_number_of_entry = 0

    def __str__(self) -> str:
        """Return human readable string."""
        return '<{} number_of_objects="{}" remaining_number_of_entry="{}" system_table_objects="{}"/>'.format(
            type(self).__name__, self.number_of_objects, self.remaining_number_of_entry, self.system_table_object
        )


@dataclass
class SystemTableObject:
    """Class for System Table Objects."""
    index: int
    actuator_address: str
    actuator_type: NodeType
    actuator_subtype: str
    power_save_mode: PowerMode
    io_membership: int
    rf_support: int
    actuator_turnaround_time: int
    io_manufacturer_id: int
    backbone_reference: str
