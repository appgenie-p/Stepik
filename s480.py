from typing import List, Optional, Tuple

Vertexes = List["Vertex"]
Links = List["Link"]
Route = Tuple[Vertexes, Links]


class Vertex:
    counter = 0

    def __init__(self) -> None:
        self._links: Links = []
        Vertex.counter += 1
        self._id = Vertex.counter

    @property
    def links(self) -> Links:
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
        self._links: Links = []
        self._vertex: Vertexes = []

    @property
    def links(self):
        return self._links

    @property
    def vertexes(self):
        return self._vertex

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

    def find_path(self, start: Vertex, stop: Vertex) -> Route:
        self._stop = stop
        self._visited_links: Optional[Links] = None
        links_with_start_v = [link for link in self._links if start in link]
        route_from_links = self._find_route_recursive(links_with_start_v)
        route_from_vertexes = self._get_vertexes_from_links(route_from_links)
        return (route_from_vertexes, route_from_links)

    def _find_route_recursive(self, current_links: Links) -> Links:
        route: Links = []
        for link in current_links:
            if self._stop in link:
                return [link]
            next_links = self._get_next_links(link)
            shortest_route_from_link = self._find_route_recursive(next_links)
            if len(route) == 0:
                route = [link] + shortest_route_from_link
            else:
                route_candidate = [link] + shortest_route_from_link
                route = (
                    route_candidate
                    if self._route_distance(route_candidate)
                    < self._route_distance(route)
                    else route
                )
        return route

    def _route_distance(self, route: Links):
        return sum(link.dist for link in route)

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

    @staticmethod
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
