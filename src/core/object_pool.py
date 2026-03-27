from collections import deque
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class ObjectPool(Generic[T]):
    def __init__(self, factory: Callable[[], T], initial_size: int = 0) -> None:
        self._factory = factory
        self._items: deque[T] = deque(factory() for _ in range(initial_size))

    def acquire(self) -> T:
        return self._items.popleft() if self._items else self._factory()

    def release(self, item: T) -> None:
        self._items.append(item)
