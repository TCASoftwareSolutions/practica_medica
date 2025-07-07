from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.pages.menu_operadores.portal_de_operadores.locators import PortalOperadoresLocators as Locators
from framework.pages.menu_operadores.portal_de_operadores.page import PortalDeOperadoresPage
from framework.pages.menu_operadores.portal_de_operadores.load_data import PortalDeOperadoresLoadData
from framework.pages.login.page import LoginPage
from framework.pages.navegacion.navegacion import NavegacionPage
from framework.utilities.configuration import Configuration


class PortalDeOperadoresWorkflow:
    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)
        self.loadtesting = PortalDeOperadoresLoadData(self.ui_adapter, self.test_config)

    def execute(self) -> PortalDeOperadoresPage:
        """Ejecutar el flujo de Portal de Operadores

        Raises:
            Exception: Error al iniciar sesión

        Returns:
            PortalDeOperadoresPage: Página de Portal de Operadores
        """
        try:
            self.logger.info("Iniciando sesión")
            login_page = LoginPage(self.ui_adapter, self.test_config)
            operador = self.test_config.config.get("credentials").get("operador")
            login_page.login(operador)

            navegacion_page = NavegacionPage(self.ui_adapter, self.test_config)
            assert navegacion_page.is_welcome_successful()

            self.logger.info("Sesión iniciada correctamente")
            navegacion_page.go_to_app(self.locators.app_name, self.locators.app_title)

            self.logger.info("Verificando si la aplicación Portal de Operadores está abierta")
            self.ui_adapter.wait_manager.wait_for_element_present(*self.locators.tab_portal_de_operadores)
            self.logger.info(f"Portal de Operadores tab text: {self.ui_adapter.get_text(self.locators.tab_portal_de_operadores)}")

            self.logger.info("Aplicación Portal de Operadores abierta correctamente")
            return PortalDeOperadoresPage(self.ui_adapter, self.test_config)

        except Exception as e:
            self.logger.error(f"Error al iniciar sesión: {str(e)}")
            raise Exception(f"Error al iniciar sesión: {str(e)}")

    def load_data(self) -> dict:
        """Cargar datos de prueba para el Portal de Operadores"""
        return self.loadtesting.get_next_user_data()

    def terminate(self) -> bool:
        """Cerrar la aplicación

        Returns:
            bool: True si la aplicación se cerró correctamente
        """
        self.logger.info("Cerrando la aplicación")
        welcome_page = NavegacionPage(self.ui_adapter, self.test_config)
        assert welcome_page.logout()
        self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Logout")
        self.logger.info("Aplicación cerrada correctamente")
        return True
