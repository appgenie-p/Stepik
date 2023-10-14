from functools import cache
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
        path_with_vertexes = self._find_path_recursive(start)
        path_with_links = _create_links_from_vertexes(path_with_vertexes)
        return (path_with_vertexes, path_with_links)

    # @cache
    def _find_path_recursive(
        self,
        start: Vertex,
        visited: Optional[PathSimple] = None,
    ) -> List[Vertex]:
        links_with_start = self._get_links_with_start(start)

        path: PathSimple = []
        if visited is None:
            visited = []
        visited += [start]

        if start == self._stop:
            return visited

        shortest: PathSimple = []
        for link in links_with_start:
            other_vertex = self._get_other_vertex(link, start)
            if other_vertex not in visited:
                path = self._find_path_recursive(
                    start=other_vertex, visited=visited[:]
                )
                if len(shortest) == 0:
                    shortest = path
                else:
                    shortest = (
                        path
                        if self._stop in path and len(path) < len(shortest)
                        else shortest
                    )
        return shortest

    def _get_links_with_start(self, start: Vertex) -> List[Link]:
        return [link for link in self._links if start in link]

    def _get_other_vertex(self, link: Link, vertex: Vertex) -> Vertex:
        return link.v1 if link.v2 == vertex else link.v2


def _create_links_from_vertexes(vertexes: List[Vertex]) -> List[Link]:
    links: List[Link] = []
    for i in range(len(vertexes) - 1):
        link = Link(vertexes[i], vertexes[i + 1])
        links.append(link)
    return links


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



map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7