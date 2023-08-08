from s436 import Callback, Router


def test_router_get():
    route = Router.get('/nonexistent')
    assert (
        route is None
    ), "Router.get() should return None for nonexistent routes"


def test_router_add_callback():
    @Callback('/test', Router)
    def test_callback():
        return 'test'

    route = Router.get('/test')
    assert route is not None, "Callback should add a route to the Router"
    assert route() == 'test', "Callback should return the correct response"


def test_router_add_multiple_callbacks():
    @Callback('/test1', Router)
    def test_callback1():
        return 'test1'

    @Callback('/test2', Router)
    def test_callback2():
        return 'test2'

    route1 = Router.get('/test1')
    assert route1 is not None, "Callback should add a route to the Router"
    assert route1() == 'test1', "Callback should return the correct response"

    route2 = Router.get('/test2')
    assert route2 is not None, "Callback should add a route to the Router"
    assert route2() == 'test2', "Callback should return the correct response"
