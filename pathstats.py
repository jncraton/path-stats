from dataclasses import dataclass
from typing import List


@dataclass
class Device:
    name: str
    bandwidth: float
    latency: float


corporate = [
    Device("Router", 1000, 10.0),
    Device("10G Ethernet Switch", 10000, 0.5),
    Device("Gigabit Ethernet Switch", 10000, 0.5),
    Device("802.11 AP", 450, 2.0),
]

home = [
    Device("Cable Modem", 50, 20.0),
    Device("Wireless Router", 450, 10.0),
]


def get_max_bandwidth(path: List[Device]) -> int:
    """
    Returns the maximum bandwidth for a given `path`.

    A path can only deliver as much bandwidth as the lowest bandwidth link,
    so this effectively returns the Device with the lowest bandwidth

    >>> get_max_bandwidth(corporate)
    450

    >>> get_max_bandwidth(home)
    50

    Note: This function can be implemented in as few as 43 characters
    """

    return 0


def get_min_latency(path: List[Device]) -> int:
    """
    Returns the minimum latency for a given `path`.

    In order to calculate the path minimum latency, we must sum the
    latencies along the path.

    >>> get_min_latency(corporate)
    13.0

    >>> get_min_latency(home)
    30.0

    Note: This function can be implemented in as few as 41 characters
    """

    return 0


def get_bandwidth_bottleneck(path: List[Device]) -> str:
    """
    Returns the name of the device that limits the path bandwidth. This is
    the device on the path with the lowest bandwidth.

    >>> get_bandwidth_bottleneck(corporate)
    '802.11 AP'

    >>> get_bandwidth_bottleneck(home)
    'Cable Modem'

    Note: This function can be implemented in as few as 52 characters
    """

    return ""
