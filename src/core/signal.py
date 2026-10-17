from collections import abc
from typing import Generic, ParamSpec

P = ParamSpec("P")


class Signal(Generic[P]):
    def __init__(self) -> None:
        self._handlers: list[abc.Callable[P, object]] = []

    def connect(self, fn: abc.Callable[P, object]) -> abc.Callable[[], None]:
        self._handlers.append(fn)
        return lambda: self._handlers.remove(fn)

    def fire(self, *args: P.args, **kwargs: P.kwargs) -> None:
        for fn in self._handlers[:]:
            fn(*args, **kwargs)
