import dataclasses
import json
import pathlib
from pathlib import Path
from dataclasses import dataclass


@dataclass
class User:
    name: str
    password: str

    def __dict__(self):
        return dataclasses.asdict(self)


@dataclass
class State:
    path: Path
    users: list[User]

    def save(self):
        with open(self.path, "w+") as contents:
            json.dump({"users": self.users}, contents, indent=2)

    def signup(self, user: str, pw: str):
        self.users.append(User(user, pw))

    def login(self, user: str, pw: str) -> bool:
        return User(user, pw) in self.users


def load(path: Path = Path(".") / "users.json") -> State:
    if path.exists():
        with open(path, "r+") as contents:
            return State(path, users=json.load(contents)["users"])
    else:
        state = State(path, users=[])
        state.save()
        return state
