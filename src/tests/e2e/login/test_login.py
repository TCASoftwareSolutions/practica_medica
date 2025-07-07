"""Conjunto de pruebas para la página de login"""

from datetime import datetime
import time
import pytest
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.pages.login.page import LoginPage
from framework.pages.navegacion.navegacion import NavegacionPage
from framework.utilities.configuration import Configuration


@pytest.mark.auth
# @pytest.mark.test_plan_id("300")
# @pytest.mark.test_suite_id("363")
class TestLogin:
    """Conjunto de pruebas para la página de login"""

    __test__ = True  # Evita que pytest lo considere un test
    logger_name = "TestLogin_logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"auth/login/login_{logger_date}/login_{logger_datetime}"
    screenshot_dir = f"auth/login/login_{logger_date}/login_{logger_datetime}"

    def setup_test(self, test_name: str):
        """Configura el test con el nombre del test y el directorio de capturas de pantalla y logs

        Args:
            test_name (str): Nombre del test
        """
        self.logger_name = f"{self.logger_name}::{test_name}"
        self.logger_dir = f"{self.logger_dir}/{test_name}"
        self.screenshot_dir = f"{self.screenshot_dir}/{test_name}"

    def record_properties(self, record_pipelines_property, test_name, test_suite_id, test_case_id):
        """Registra las propiedades del test en el reporte de Azure DevOps

        Args:
            record_pipelines_property (fixture): Fixture para registrar propiedades en el reporte de Azure DevOps
            test_name (str): Nombre del test
            test_suite_id (str): ID de la suite de pruebas
            test_case_id (str): ID del caso de prueba
        """
        record_pipelines_property("test_name", f"{test_name} pipeline")
        record_pipelines_property("test_suite_id", test_suite_id)
        record_pipelines_property("test_case_id", test_case_id)

    @pytest.mark.smoke
    @pytest.mark.azure_sync
    @pytest.mark.test_case_id("364")
    @pytest.mark.test_name("364-Login test")
    def test01_Login(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de login

        Args:
            driver (WebDriver): WebDriver
            config (dict): Configuración de la prueba
            record_pipelines_property (): _description_
        """
        test_name = "Test01_Login"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "363", "364")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        login_page = LoginPage(ui_adapter, test_config)
        operador = test_config.config.get("credentials").get("operador")
        login_page.login(operador)

        time.sleep(2)
        welcome_page = NavegacionPage(ui_adapter, test_config)
        assert welcome_page.is_welcome_successful()

        time.sleep(5)
        assert welcome_page.logout()
        ui_adapter.take_screenshot(test_config.screenshot_dir, "Logout")
        test_config.logger.info("Aplicación cerrada correctamente")
