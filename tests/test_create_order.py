from pytest import mark
from order_utils import create_order

class TestApiCreateOrder:
    @mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ])
    def test_create_order_with_any_color(self, colors):
        response = create_order(colors)
        assert response.status_code == 201 and 'track' in response.json()

    def test_create_order_without_color(self):
        response = create_order()
        assert response.status_code == 201 and 'track' in response.json()