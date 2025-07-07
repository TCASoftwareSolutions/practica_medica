from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.pages.tablero_medico.locators import TableroMedicoLocators as Locators
from framework.pages.tablero_medico.page import TableroMedicoPage
from framework.pages.navegacion.navegacion import NavegacionPage
from framework.utilities.configuration import Configuration


class TableroMedicoWorkflow:
    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def execute(self) -> TableroMedicoPage:
        """Ejecutar el flujo de trabajo del Tablero Médico

        Raises:
            Exception: Error al iniciar sesión

        Returns:
            InformeDeSolicitudesPage: Página de Tablero Medico
        """
        try:
            self.logger.info("Verificando si la aplicación Tablero Medico está abierta")
            self.ui_adapter.wait_manager.wait_for_element_present(*self.locators.tab_tablero_medico)
            self.logger.info(f"Tablero Medico tab text: {self.ui_adapter.get_text(self.locators.tab_tablero_medico)}")

            self.logger.info("Aplicación Tablero Medico abierta correctamente")
            return TableroMedicoPage(self.ui_adapter, self.test_config)

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
