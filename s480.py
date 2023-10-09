from reprlib import repr
from typing import Any, List, Tuple


class Vertex:
    counter = 0

    def __init__(self) -> None:
        self._links: List["Link"] = []
        Vertex.counter += 1
        self._id = Vertex.counter

    @property
    def links(self) -> List["Link"]:
        return self._links

    def __repr__(self) -> str:
        return f"Vertex({self._id})"


class Link:
    def __init__(self, v1: Vertex, v2: Vertex) -> None:
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self) -> Vertex:
        return self._v1

    @property
    def v2(self) -> Vertex:
        return self._v2

    @property
    def dist(self) -> int:
        return self._dist

    @dist.setter
    def dist(self, value: int) -> None:
        self._dist = value

    def __eq__(self, other: object) -> bool:
        if not other:
            return False
        if not isinstance(other, Link):
            raise NotImplementedError
        return (self.v1 == other.v1 and self.v2 == other.v2) or (
            self.v1 == other.v2 and self.v2 == other.v1
        )

    def __contains__(self, vertex: Vertex) -> bool:
        return vertex in [self.v1, self.v2]

    def __iter__(self):
        return iter([self.v1, self.v2])

    def __repr__(self) -> str:
        return f"Link({self.v1}, {self.v2})"


class LinkedGraph:
    def __init__(self) -> None:
        self._links: List[Link] = []
        self._vertex: List[Vertex] = []
        self._links_copy: List[Link]

    def add_vertex(self, vertex: Vertex) -> None:
        if vertex in self._vertex:
            return
        self._vertex.append(vertex)

    def add_link(self, link: Link) -> None:
        if link in self._links:
            return
        self._links.append(link)
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)

    def __repr__(self) -> str:
        return f"LinkedGraph({repr(self._vertex)}, {repr(self._links)})"

    def find_path(
        self, start: Vertex, stop: Vertex
    ) -> Tuple[List[Vertex], List[Link]]:
        self._links_copy = self._links.copy()
        return self._find_path_main(start, stop)

    def _find_path_main(
        self, start: Vertex, stop: Vertex
    ) -> Tuple[List[Vertex], List[Link]]:
        links_with_start: List[Link] = self._get_links_with_start(start)

        if self._is_stop_in_links_with_start(stop, links_with_start):
            final_link = self._get_link_with_vertex(stop, links_with_start)
            return [start, stop], [final_link]

        # self._remove_links_from_links_copy(links_with_start)

        for link in links_with_start:
            self._links_copy.remove(link)
            other_vertex = self._get_other_vertex(link, start)
            if path := self._find_path_main(other_vertex, stop):
                return [start] + path[0], [link] + path[1]

        raise ValueError("No links provided")

    def _remove_links_from_links_copy(
        self, links_with_start: List[Link]
    ) -> None:
        for link in links_with_start:
            self._links_copy.remove(link)

    def _get_links_with_start(self, start: Vertex) -> List[Link]:
        return [link for link in self._links_copy if start in link]

    def _is_stop_in_links_with_start(
        self, vertex: Vertex, links: List[Link]
    ) -> bool:
        return any(vertex in link for link in links)

    def _get_link_with_vertex(self, vertex: Vertex, links: List[Link]) -> Link:
        return next(link for link in links if vertex in link)

    def _get_other_vertex(self, link: Link, vertex: Vertex) -> Vertex:
        return link.v1 if link.v2 == vertex else link.v2
