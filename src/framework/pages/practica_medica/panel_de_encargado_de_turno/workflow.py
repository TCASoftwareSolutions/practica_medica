from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.pages.practica_medica.panel_de_encargado_de_turno.locators import PanelDeEncargadoDeTurnoLocators as Locators
from framework.pages.practica_medica.panel_de_encargado_de_turno.page import PanelDeEncargadoDeTurnoPage
from framework.pages.login.page import LoginPage
from framework.pages.navegacion.navegacion import NavegacionPage
from framework.utilities.configuration import Configuration


class PanelDeEncargadoDeTurnoWorkflow:
    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def execute(self) -> PanelDeEncargadoDeTurnoPage:
        """Ejecutar el flujo de Panel de Encargado de Turno

        Raises:
            Exception: Error al iniciar sesión

        Returns:
            PanelDeEncargadoDeTurnoPage: Página de Panel de Encargado de Turno
        """
        try:
            self.logger.info("Iniciando sesión")
            login_page = LoginPage(self.ui_adapter, self.test_config)
            supervisor = self.test_config.config.get("credentials").get("supervisor")
            login_page.login(supervisor)

            navegacion_page = NavegacionPage(self.ui_adapter, self.test_config)
            assert navegacion_page.is_welcome_successful()

            self.logger.info("Sesión iniciada correctamente")
            navegacion_page.go_to_app(self.locators.app_name, self.locators.app_title)

            self.logger.info("Verificando si la aplicación Panel de Encargado de Turno está abierta")
            self.ui_adapter.wait_manager.wait_for_element_present(*self.locators.tab_agenda_medica)
            self.logger.info(f"Panel de Encargado de Turno tab text: {self.ui_adapter.get_text(self.locators.tab_agenda_medica)}")

            self.logger.info("Aplicación Panel de Encargado de Turno abierta correctamente")
            return PanelDeEncargadoDeTurnoPage(self.ui_adapter, self.test_config)

        except Exception as e:
            self.logger.error(f"Error al iniciar sesión: {str(e)}")
            raise Exception(f"Error al iniciar sesión: {str(e)}")

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
