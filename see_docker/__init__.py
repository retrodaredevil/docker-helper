import sys
from argparse import ArgumentParser
from itertools import count
from pathlib import Path
import dateutil.parser

import datetime

from typing import Callable, List, Optional, Iterator, Tuple

import docker


def __do_func(func: Callable[[List[str]], int]) -> None:
    try:
        sys.exit(func(sys.argv[1:]))
    except KeyboardInterrupt:
        print("\nExiting")


def do_see_docker():
    __do_func(see_docker_main)


def see_docker_main(args: List[str]) -> int:
    current_timezone: datetime.tzinfo = datetime.datetime.now().astimezone().tzinfo

    client = docker.from_env()
    for network in client.networks.list():
        network.reload()  # This is necessary because client.networks.list() does not fully populated the attributes
        creation_time_string = network.attrs["Created"]
        created_time: datetime.datetime = dateutil.parser.isoparse(creation_time_string)
        created_time_display = created_time.astimezone(current_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")
        print(f"id: {network.short_id}  name: {network.name:<30}  created: {created_time_display}")
        for container_id, container_attrs in network.attrs["Containers"].items():
            container_short_id = container_id[:12]
            container_name = container_attrs["Name"]
            mac_address = container_attrs["MacAddress"]
            ipv4_address = container_attrs["IPv4Address"]
            ipv6_address = container_attrs["IPv6Address"]
            ip_address = f"(IPv4) {ipv4_address}" if ipv4_address else f"(IPv6) {ipv6_address}"

            print(f"\t{container_name:<16} ({container_short_id})  {ip_address:<35}  mac: {mac_address}")

    return 0
