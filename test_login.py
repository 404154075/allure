import allure
import pytest


class Test_l:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_01(self):
        assert 0
    @allure.step(title='测试2')
    def test_02(self):
        assert 1
    def test_03(self):
        assert 0

