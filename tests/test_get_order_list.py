from order_utils import get_order_list


class TestGetOrderList:

    def test_get_order_list(self):
        response = get_order_list()
        order_data = response.json()
        assert response.status_code == 200 and isinstance(order_data['orders'], list)
