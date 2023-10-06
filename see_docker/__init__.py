import sys
from argparse import ArgumentParser
from itertools import count
from pathlib import Path

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
    client = docker.from_env()
    for network in client.networks.list():
        print(f"id: {network.short_id} name: {network.name}")
        containers = client.containers.list(filters={'network': network.id})
        for container in containers:
            print(f"\t{container.name}")

    return 0
