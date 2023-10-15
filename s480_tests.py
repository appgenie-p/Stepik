from typing import Tuple

import pytest

from s480 import Link, LinkedGraph, Vertex


def test_vertex_creation():
    assert Vertex()


@pytest.fixture
def v1() -> Vertex:
    return Vertex()


@pytest.fixture
def v2() -> Vertex:
    return Vertex()


@pytest.fixture
def l1(v1: Vertex, v2: Vertex) -> Link:
    return Link(v1, v2)


def test_vertex_links(v1: Vertex):
    assert v1.links == []


def test_link_creation(v1: Vertex, v2: Vertex):
    assert Link(v1, v2)


def test_link_v1(v1: Vertex, v2: Vertex):
    link = Link(v1, v2)
    assert link.v1 == v1
    assert link.v2 == v2
    assert link.dist == 1
    link.dist = 2
    assert link.dist == 2


def test_linked_graph_creation():
    assert LinkedGraph()


def test_add_vertex_to_graph_if_absent(v1: Vertex):
    graph = LinkedGraph()
    graph.add_vertex(v1)
    assert graph._vertex == [v1]


def test_add_vertex_to_graph_if_present(v1: Vertex):
    graph = LinkedGraph()
    graph.add_vertex(v1)
    graph.add_vertex(v1)
    assert graph._vertex == [v1]


def test_add_link_to_graph_if_present(l1: Link):
    graph = LinkedGraph()
    graph.add_link(l1)
    graph.add_link(l1)
    assert graph._links == [l1]


Graph = Tuple[LinkedGraph, Vertex, Vertex, Vertex, Vertex, Vertex]


@pytest.fixture
def graph() -> Graph:
    map2 = LinkedGraph()
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()

    map2.add_link(Link(v1, v2))
    map2.add_link(Link(v2, v3))
    map2.add_link(Link(v2, v4))
    map2.add_link(Link(v3, v4))
    map2.add_link(Link(v4, v5))

    return map2, v1, v2, v3, v4, v5


def test_graph_attrs_len(graph: Graph):
    gr, *_ = graph
    assert len(gr._links) == 5
    assert len(gr._vertex) == 5


def test_links_equality(v1: Vertex, v2: Vertex):
    l1 = Link(v1, v2)
    l2 = Link(v2, v1)
    assert l1 == l2


def test_graph_add_existing_link(graph: Graph):
    gr, v1, v2, *_ = graph
    gr.add_link(Link(v2, v1))
    assert len(gr._links) == 5, (
        "метод add_link() добавил связь Link(v2, v1), "
        "хотя уже имеется связь Link(v1, v2)"
    )


@pytest.fixture
def vs():
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    v6 = Vertex()
    return v1, v2, v3, v4, v5, v6


Vs = tuple[Vertex, ...]


def test_graph_find_path_2_vertexes(vs: Vs):
    v1, v2, *_ = vs
    sut = LinkedGraph()
    sut.add_link(l1 := Link(v1, v2))

    path = sut.find_path(v1, v2)

    assert path == ([v1, v2], [l1])


def test_graph_find_path_3_vertexes(vs: Vs):
    v1, v2, v3, *_ = vs
    sut = LinkedGraph()
    sut.add_link(l1 := Link(v1, v2))
    sut.add_link(l2 := Link(v2, v3))

    path = sut.find_path(v1, v3)

    assert path == ([v1, v2, v3], [l1, l2])


def test_graph_find_path_4_vertexes(vs: Vs):
    v1, v2, v3, v4, *_ = vs
    sut = LinkedGraph()
    sut.add_link(l1 := Link(v1, v2))
    sut.add_link(l2 := Link(v2, v3))
    sut.add_link(l3 := Link(v3, v4))

    path = sut.find_path(v1, v4)

    assert path == ([v1, v2, v3, v4], [l1, l2, l3])


def test_graph_find_path_6_vertexes(vs: Vs):
    v1, v2, v3, v4, v5, v6 = vs
    gr = LinkedGraph()
    gr.add_link(l1 := Link(v1, v2))
    gr.add_link(_ := Link(v2, v3))
    gr.add_link(_ := Link(v4, v3))
    gr.add_link(_ := Link(v4, v6))
    gr.add_link(l5 := Link(v2, v5))
    gr.add_link(l6 := Link(v6, v5))

    path = gr.find_path(v1, v6)

    assert path == ([v1, v2, v5, v6], [l1, l5, l6])


def test_graph_find_path_6_vertexes_opposite(vs: Vs):
    v1, v2, v3, v4, v5, v6 = vs
    sut = LinkedGraph()
    sut.add_link(l1 := Link(v1, v2))
    sut.add_link(_ := Link(v2, v5))
    sut.add_link(_ := Link(v5, v4))
    sut.add_link(_ := Link(v4, v6))
    sut.add_link(l5 := Link(v2, v3))
    sut.add_link(l6 := Link(v3, v6))

    path = sut.find_path(v1, v6)

    assert path == ([v1, v2, v3, v6], [l1, l5, l6])


def test_graph_find_path_5_vertexes_with_circuit(vs: Vs):
    v1, v2, v3, v4, v5, *_ = vs
    sut = LinkedGraph()
    sut.add_link(l1 := Link(v1, v2))
    sut.add_link(l3 := Link(v2, v4))
    sut.add_link(l5 := Link(v4, v5))
    sut.add_link(_ := Link(v3, v4))
    sut.add_link(_ := Link(v2, v3))

    path = sut.find_path(v1, v5)

    assert path == ([v1, v2, v4, v5], [l1, l3, l5])


def test_author_tests():
    map2 = LinkedGraph()
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()

    map2.add_link(Link(v1, v2))
    map2.add_link(Link(v2, v3))
    map2.add_link(Link(v2, v4))
    map2.add_link(Link(v3, v4))
    map2.add_link(Link(v4, v5))

    assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
    assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

    map2.add_link(Link(v2, v1))
    assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

    path = map2.find_path(v1, v5)
    s = sum([x.dist for x in path[1]])
    assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"