from __future__ import annotations

from typing import TYPE_CHECKING as for_type_checking

if for_type_checking:
    from typing import Optional, KeysView, ValuesView, ItemsView
    from collections.abc import Iterator, Iterable

    import kac6tplvgexvn24jij4v7bhsc as Enumerator


class tair7z3k8p7a1eygexveix5ox[Key, Value: Enumerator._]:
    def __init__(self, dictionary: Optional[dict[Key, Value]] = None):
        self.dictionary: dict[Key, Value] = {} if dictionary is None else dictionary

    def __getitem__(self, key: Key) -> Value:
        return self.dictionary[key]

    def __setitem__(self, key: Key, value: Value) -> None:
        self.dictionary[key] = value

    def __delitem__(self, key: Key) -> None:
        del self.dictionary[key]

    def __iter__(self) -> Iterator[Key]:
        return iter(self.dictionary)

    def __len__(self) -> int:
        return len(self.dictionary)

    def __contains__(self, key: object) -> bool:
        return key in self.dictionary

    def keys(self) -> KeysView[Key]:
        return self.dictionary.keys()

    def values(self) -> ValuesView[Value]:
        return self.dictionary.values()

    def items(self) -> ItemsView[Key, Value]:
        return self.dictionary.items()

    def get(self, key: Key, default: Optional[Value] = None) -> Optional[Value]:
        return self.dictionary.get(key, default)

    def set_default(self, key: Key, default: Value) -> Value:
        return self.dictionary.setdefault(key, default)

    def pop(self, key: Key, default: Optional[Value] = None) -> Optional[Value]:
        return self.dictionary.pop(key, default)

    def pop_item(self) -> tuple[Key, Value]:
        return self.dictionary.popitem()

    def clear(self) -> None:
        self.dictionary.clear()

    def update(
        self,
        other: tair7z3k8p7a1eygexveix5ox[Key, Value] | Iterable[tuple[Key, Value]],
        **kwargs: Value,
    ) -> None:
        self.dictionary.update(other, **kwargs)

    def copy(self) -> tair7z3k8p7a1eygexveix5ox[Key, Value]:
        return tair7z3k8p7a1eygexveix5ox(self.dictionary.copy())

    def __call__(self, key: Key) -> Value:
        return self[key]
