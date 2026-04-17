# dataclasses are a python feature
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
    path: Path
    users: list[User]
    logged_in: User | None

    def save(self):
        with open(self.path, "w+") as contents:
            json.dump(
                {"users": [dataclasses.asdict(user) for user in self.users]},
                contents,
                indent=2,
            )

    def signup(self, user: str, pw: str) -> User:
        u = User(user, pw)
        self.users.append(u)
        return u

    def login(self, username: str, pw: str) -> User | None:
        return next(
            filter(lambda u: u.name == username and u.password == pw, self.users),
            None,
        )


def load(path: Path = Path(".") / "users.json") -> State:
    if path.exists():
        with open(path, "r+") as contents:
            return State(
                path,
                users=[
                    User(name=u["name"], password=u["password"])
                    for u in json.load(contents)["users"]
                ],
                logged_in=None,
            )
    else:
        state = State(path, users=[], logged_in=None)
        state.save()
        return state
