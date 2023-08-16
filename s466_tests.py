from s466 import DetailView


def test_detail_view():
    view = DetailView()
    html = view.render_request(
        {"url": "https://stepik.org/course/116336/", "method": "GET"}
    )
    assert html == "GET: https://stepik.org/course/116336/"
