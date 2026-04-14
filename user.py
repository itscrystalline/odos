import dataclasses
import json
import pathlib
from pathlib import Path
from dataclasses import dataclass


@dataclass
class User:
    name: str
    password: str


@dataclass
class State:
    users: list[User]


def load(path: Path = Path(".") / "users.json") -> State:
    if path.exists():
        with open(path, "r+") as contents:
            return State(users=json.load(contents)["users"])
    else:
        state = State(users=[])
        save(state)
        return state


def save(state: State, path: Path = Path(".") / "users.json"):
    with open(path, "w+") as contents:
        json.dump(dataclasses.asdict(state), contents, indent=2)
