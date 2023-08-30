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
        return f"Link({self.v1}, {self.v2}, {self.dist})"


class LinkedGraph:
    def __init__(self) -> None:
        self._links: List[Link] = []
        self._vertex: List[Vertex] = []

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
        self, start_v: Vertex, stop_v: Vertex
    ) -> Tuple[List[Vertex], List[Link]]:
        self._original_links = self._links.copy()
        return self._find_path_main(start_v, stop_v)

    def _find_path_main(
        self, start_v: Vertex, stop_v: Vertex
    ) -> Tuple[List[Vertex], List[Link]]:
        start_links: List[Link] = self._get_links(start_v)

        if self._check_vertex_in_links(stop_v, start_links):
            final_link = self._get_link_with_vertex(stop_v, start_links)
            return [start_v, stop_v], [final_link]

        self._remove_links_from_original_list(start_links)

        for link in start_links:
            other_vertex = self._get_other_vertex(link, start_v)
            if path := self._find_path_main(other_vertex, stop_v):
                return [start_v] + path[0], [link] + path[1]

        # link_with_vertex = self._get_link_with_vertex(start_v, start_links)
        # other_vertex = self._get_other_vertex(link_with_vertex, start_v)
        # return [start_v, other_vertex], [link_with_vertex]

    def _remove_links_from_original_list(self, start_links: List[Link]):
        [self._original_links.remove(link) for link in start_links]

    def _get_links(self, start_v: Vertex) -> List[Link]:
        return [link for link in self._original_links if start_v in link]

    def _check_vertex_in_links(self, vertex: Vertex, links: List[Link]) -> bool:
        return any(vertex in link for link in links)

    def _get_link_with_vertex(self, vertex: Vertex, links: List[Link]) -> Link:
        return next(link for link in links if vertex in link)

    def _get_other_vertex(self, link: Link, vertex: Vertex) -> Vertex:
        return link.v1 if link.v2 == vertex else link.v2
