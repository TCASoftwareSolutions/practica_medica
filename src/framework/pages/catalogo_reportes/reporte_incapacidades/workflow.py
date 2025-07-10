from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.pages.navegacion.navegacion import NavegacionPage
from framework.utilities.configuration import Configuration
from framework.pages.catalogo_reportes.reporte_incapacidades.locators import ReporteIncapacidadesLocators as Locators
from framework.pages.catalogo_reportes.reporte_incapacidades.page import ReporteIncapacidadesPage
from framework.pages.login.page import LoginPage


class IncapacidadesWorkflow:
    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def execute(self) -> ReporteIncapacidadesPage:
        """Ejecutar el flujo de Reporte de incapacidades
        Raises:
            Exception: Error al iniciar sesión

        Returns:
            AgendaMedicaPage: Reporte de incapacidades
        """
        try:
            self.logger.info("Iniciando sesión")
            login_page = LoginPage(self.ui_adapter, self.test_config)
            medico = self.test_config.config.get("credentials").get("medico")
            login_page.login(medico)

            navegacion_page = NavegacionPage(self.ui_adapter, self.test_config)
            assert navegacion_page.is_welcome_successful()

            self.logger.info("Sesión iniciada correctamente")
            navegacion_page.go_to_app(self.locators.app_name, self.locators.app_title)

            self.ui_adapter.wait_manager.wait_for_element_present(*self.locators.tab_reporte_incapacidades)
            self.logger.info(f"Reporte de incapacidades tab text: {self.ui_adapter.get_text(self.locators.tab_reporte_incapacidades)}")

            self.logger.info("Aplicación Reporte de incapacidades abierta correctamente")
            return ReporteIncapacidadesPage(self.ui_adapter, self.test_config)

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
