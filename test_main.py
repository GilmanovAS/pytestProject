import pytest
from main import ticket_price


class TestMain:
    def test_01(self):
        assert ticket_price(0) == "0", "Error for 0"

    def test_02(self):
        assert ticket_price(7) == "100", "Error for 7"

    def test_03(self):
        assert ticket_price(45) == "300", "Error for 45"

    def test_04(self):
        with pytest.raises(TypeError):
            ticket_price("45")