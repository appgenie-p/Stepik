from typing import Any, List, Optional, Tuple


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


PathSimple = List[Vertex]
Path = Tuple[PathSimple, List[Link]]


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
        link.v1.links.append(link)
        link.v2.links.append(link)

    def __repr__(self) -> str:
        return f"LinkedGraph({repr(self._vertex)}, {repr(self._links)})"

    def find_path(self, start: Vertex, stop: Vertex) -> Path:
        self._stop = stop
        links_with_vertex = self._get_links_with_vertex(start)
        path_with_links = self._find_path_recursive(links_with_vertex)
        path_with_vertexes = _get_list_of_vertexes_from_links(path_with_links)
        return (path_with_vertexes, path_with_links)

    def _find_path_recursive(
        self, links_with_vertex: List[Link], path: Optional[List[Link]] = None
    ) -> List[Link]:
        if path is None:
            path = []
        shortest: List[Link] = []
        for link in links_with_vertex:
            if link in path:
                continue
            path += [link]
            if self._stop in link:
                return path
            links_with_other_vertex = self._get_links_with_vertex(link.v2)
            new_path = self._find_path_recursive(
                links_with_other_vertex, path[:]
            )
            if (
                len(shortest) == 0
                or len(new_path) < len(shortest)
                and self._stop in path[-1]
            ):
                shortest = new_path
        return shortest

    def _get_links_with_vertex(self, start: Vertex) -> List[Link]:
        return [link for link in self._links if start in link]

    def _get_other_vertex(self, link: Link, vertex: Vertex) -> Vertex:
        return link.v1 if link.v2 == vertex else link.v2


def _get_list_of_vertexes_from_links(links: List[Link]) -> List[Vertex]:
    vertexes: List[Vertex] = [link.v1 for link in links]
    vertexes.append(links[-1].v2)
    return vertexes


class Station(Vertex):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return str(self.name)


class LinkMetro(Link):
    def __init__(self, v1: Vertex, v2: Vertex, dist: int):
        super().__init__(v1, v2)
        self._dist = dist
