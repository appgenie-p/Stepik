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


Vertexes = List[Vertex]
Links = List[Link]
Path = Tuple[Vertexes, Links]


class LinkedGraph:
    def __init__(self) -> None:
        self._links: Links = []
        self._vertex: Vertexes = []

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
        self._visited_links: Optional[Links] = None
        links_with_vertex = self._get_links_with_vertex(start)
        route_with_links = self._find_route_recursive(links_with_vertex)
        route_with_vertexes = _get_vertexes_from_links(route_with_links)
        return (route_with_vertexes, route_with_links)

    def _find_route_recursive(self, current_links: Links) -> Links:
        # Make iteration over graph with iter
        shortest: Links = []
        for link in current_links:
            if self._stop in link:
                return [link]
            next_links = self._get_next_links(link)
            latest_link = self._find_route_recursive(next_links)
            if len(shortest) == 0:
                shortest = [link] + latest_link
            else:
                new_way = [link] + latest_link
                new_way_len = sum(link.dist for link in new_way)
                shortest_len = sum(link.dist for link in shortest)
                shortest = new_way if new_way_len < shortest_len else shortest
        return shortest

    def _get_links_with_vertex(self, start: Vertex) -> Links:
        return [link for link in self._links if start in link]

    def _get_next_links(self, initial_link: Link) -> Links:
        if self._visited_links is None:
            self._visited_links = []
        self._visited_links.append(initial_link)
        return [
            link
            for link in self._links
            if (initial_link.v1 in link or initial_link.v2 in link)
            and link not in self._visited_links
        ]


def _get_vertexes_from_links(links: Links) -> Vertexes:
    vertexes: Vertexes = []
    for link in links:
        if link.v1 not in vertexes:
            vertexes.append(link.v1)
        if link.v2 not in vertexes:
            vertexes.append(link.v2)
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
