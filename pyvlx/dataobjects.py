"""Module for Dataobjects."""
from datetime import datetime
import time
from .const import (StatusId, NodeParameter, RunStatus, StatusReply)


class DtoLocalTime:
    """Dataobject to hold KLF200 Time Data."""

    def __init__(self, utctime=None, localtime=None):
        """Initialize DtoLocalTime class."""
        if utctime is None:
            utctime = datetime.fromtimestamp(0)
        if localtime is None:
            localtime = datetime.fromtimestamp(0)
        self.utctime = utctime
        self.localtime = localtime

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} utctime="{}" localtime="{}"/>'.format(
                type(self).__name__, self.utctime, self.localtime)
        )

    def from_payload(self, payload):
        """Build the Dto From Data."""
        self.utctime = datetime.fromtimestamp(int.from_bytes(payload[0:4], "big"))
        weekday = payload[11] - 1
        if weekday == -1:
            weekday = 6

        self.localtime = datetime.fromtimestamp(time.mktime(
            (int.from_bytes(payload[9:11], byteorder='big') + 1900,  # Year
             payload[8],  # month
             payload[7],  # day
             payload[6],  # hour
             payload[5],  # minute
             payload[4],  # second
             weekday,
             int.from_bytes(payload[12:14], byteorder='big'),  # day of year
             int.from_bytes(payload[14:15], byteorder='big', signed=True))))

    def to_payload(self):
        """Build the Dto From Data."""
        payload = b''
        payload = int(self.utctime.timestamp()).to_bytes(4, byteorder='big')
        payload += self.localtime.second.to_bytes(1, "big")
        payload += self.localtime.minute.to_bytes(1, "big")
        payload += self.localtime.hour.to_bytes(1, "big")
        payload += self.localtime.day.to_bytes(1, "big")
        payload += self.localtime.month.to_bytes(1, "big")
        payload += (self.localtime.year - 1900).to_bytes(2, "big")
        if self.localtime.weekday == 6:
            payload += (0).to_bytes(1, "big")
        else:
            payload += (self.localtime.weekday() + 1).to_bytes(1, "big")
        payload += self.localtime.timetuple().tm_yday.to_bytes(2, "big")
        payload += (self.localtime.timetuple().tm_isdst).to_bytes(1, "big", signed=True)
        return payload


class DtoNetworkSetup:
    """Dataobject to hold KLF200 Network Setup."""

    def __init__(self, ipaddress=None, gateway=None, netmask=None, dhcp=None):
        """Initialize DtoNetworkSetup class."""
        self.ipaddress = ipaddress
        self.gateway = gateway
        self.netmask = netmask
        self.dhcp = dhcp

    def __str__(self):
        """Return human readable string."""
        return '<{} ipaddress="{}" gateway="{}" gateway="{}"  dhcp="{}"/>'.format(
            type(self).__name__, self.ipaddress, self.gateway,
            self.gateway, self.dhcp
        )


class DtoProtocolVersion:
    """KLF 200 Dataobject for Protocol version."""

    def __init__(self, majorversion=None, minorversion=None):
        """Initialize DtoProtocolVersion class."""
        self.majorversion = majorversion
        self.minorversion = minorversion

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} majorversion="{}" minorversion="{}"/>'.format(
                type(self).__name__, self.majorversion, self.minorversion
            )
        )


class DtoState:
    """Data Object for Gateway State."""

    def __init__(self, gateway_state=None, gateway_sub_state=None):
        """Initialize DtoState class."""
        self.gateway_state = gateway_state
        self.gateway_sub_state = gateway_sub_state

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} gateway_state="{}" gateway_sub_state="{}"/>'.format(
                type(self).__name__, self.gateway_state, self.gateway_sub_state
            )
        )


class DtoVersion:
    """Object for KLF200 Version Information."""

    def __init__(self,
                 softwareversion=None, hardwareversion=None, productgroup=None, producttype=None):
        """Initialize DtoVersion class."""
        self.softwareversion = softwareversion
        self.hardwareversion = hardwareversion
        self.productgroup = productgroup
        self.producttype = producttype

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} softwareversion="{}" hardwareversion="{}" '
            'productgroup="{}" producttype="{}"/>'.format(
                type(self).__name__,
                self.softwareversion, self.hardwareversion, self.productgroup, self.producttype
            )
        )


class DtoLeaveLearnState:
    """Dataobject to hold KLF200 Data."""

    def __init__(self, status=None):
        """Initialize DtoLeaveLearnState class."""
        self.status = status

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} status="{}"/>'.format(
                type(self).__name__, self.status
            )
        )


class DtoActivationLogLine:
    """Dataobject an Line from Activation Log."""

    def __init__(self):
        """Initialize DtoLocalTime class."""
        self.timestamp = datetime.fromtimestamp(0)
        self.sessionid = 0
        self.statusid = StatusId(0xFF)
        self.index = 0
        self.nodeparameter = NodeParameter(0xFF)
        self.parametervalue = 0
        self.runstatus = RunStatus(0)
        self.statusreply = StatusReply(0x00)
        self.informationcode = 0

    def __str__(self):
        """Return human readable string."""
        return (
            '<{} timestamp="{}" sessionid="{}" statusid="{}" index="{}" nodeparameter="{}" '
            'parametervalue="{}" runstatus="{}" statusreply="{}" informationcode="{}"/>'.format(
                type(self).__name__, self.timestamp, self.sessionid, self.statusid,
                self.index, self.nodeparameter, self.parametervalue, self.runstatus,
                self.statusreply, self.informationcode)
        )

    def from_payload(self, payload):
        """Build the Dto From Data."""
        self.timestamp = datetime.fromtimestamp(int.from_bytes(payload[0:4], "big"))
        self.sessionid = int.from_bytes(payload[4:6], "big")
        self.statusid = StatusId(payload[6])
        self.index = payload[7]
        self.nodeparameter = NodeParameter(payload[8])
        self.parametervalue = int.from_bytes(payload[9:11], "big")
        self.runstatus = RunStatus(payload[11])
        self.statusreply = StatusReply(payload[12])
        self.informationcode = int.from_bytes(payload[13:], "big")

    def to_payload(self):
        """Build the Dto From Data."""
        payload = b''
        payload = int(self.timestamp.timestamp()).to_bytes(4, byteorder='big')
        payload += self.sessionid.to_bytes(2, "big")
        payload += self.statusid.value.to_bytes(1, "big")
        payload += self.index.to_bytes(1, "big")
        payload += self.nodeparameter.value.to_bytes(1, "big")
        payload += self.parametervalue.to_bytes(2, "big")
        payload += self.runstatus.value.to_bytes(1, "big")
        payload += self.statusreply.value.to_bytes(1, "big")
        payload += self.informationcode.to_bytes(4, "big")
        return payload
