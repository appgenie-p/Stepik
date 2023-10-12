from typing import List, Optional, Tuple


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
        return f"V:{self._id}"


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
        link.v1.links.append(link)
        link.v2.links.append(link)

    def __repr__(self) -> str:
        return f"LinkedGraph({repr(self._vertex)}, {repr(self._links)})"

    Path = Tuple[List[Vertex], List[Link]]
    PathSimple = Optional[List[Vertex]]

    def find_path(self, start: Vertex, stop: Vertex) -> PathSimple:
        self._links_copy = self._links.copy()
        return self._find_path_recursive(start, stop)

    def _find_path_recursive(
        self,
        start: Vertex,
        stop: Vertex,
        visited: Optional[List[Vertex]] = None,
        path: PathSimple = None,
        shortest: PathSimple = None,
    ) -> List[Vertex]:
        links_with_start = self._get_links_with_start(start)

        if visited is None:
            visited = []
        if path is None:
            path = []
        if shortest is None:
            shortest = []

        path += [start]
        visited += [start]

        if start == stop:
            return path

        for link in links_with_start:
            other_vertex = self._get_other_vertex(link, start)
            if other_vertex not in visited:
                if new_path := self._find_path_recursive(
                    start=other_vertex,
                    stop=stop,
                    visited=visited[:],
                    path=path[:],
                    shortest=shortest[:],
                ):
                    shortest = (
                        shortest
                        if stop not in new_path
                        and len(new_path) > len(shortest)
                        else new_path
                    )
        return shortest

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
