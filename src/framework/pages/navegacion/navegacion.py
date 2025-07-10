"""
# Clase: NavegacionPage
# Descripción: Clase que contiene los elementos y métodos de la página de navegación de la aplicación.
"""

import time
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.pages.navegacion.locators import NavegacionLocators

# from framework.ports.ui_port import UIPort
from framework.utilities.configuration import Configuration


class NavegacionPage:
    """Clase para la navegación de la aplicación"""

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.locators = NavegacionLocators()
        self.test_config = test_config
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def onClick_search_button(self):
        """Hace click en el botón de búsqueda

        Raises:
            Exception: Error al hacer click en el botón de búsqueda
        """
        try:
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnSearch)
            self.ui_adapter.click(self.locators.btnSearch)
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón de búsqueda: {str(e)}")
            raise Exception(f"Error al hacer click en el botón de búsqueda: {str(e)}")

    def onClick_ImageProfile(self):
        """Hace click en la imagen de perfil

        Raises:
            Exception: Error al hacer click en la imagen de perfil
        """
        try:
            self.logger.info("Haciendo click en la imagen de perfil")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnImageProfile)
            self.ui_adapter.click(self.locators.btnImageProfile)
        except Exception as e:
            self.logger.error(f"Error al hacer click en la imagen de perfil: {str(e)}")
            raise Exception(f"Error al hacer click en la imagen de perfil: {str(e)}")

    def onClick_Logout(self):
        """Hace click en el botón de cerrar sesión

        Raises:
            Exception: Error al hacer click en el botón de cerrar sesión
        """
        try:
            self.logger.info("Haciendo click en el botón de cerrar sesión")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnLogout)
            self.ui_adapter.click(self.locators.btnLogout)
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón de cerrar sesión: {str(e)}")
            raise Exception(f"Error al hacer click en el botón de cerrar sesión: {str(e)}")

    def onClick_Confirmar(self):
        """Hace click en el botón de confirmar

        Raises:
            Exception: Error al hacer click en el botón de confirmar
        """
        try:
            self.logger.info("Haciendo click en el botón de confirmar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnConfirmar)
            self.ui_adapter.click(self.locators.btnConfirmar)
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón de confirmar: {str(e)}")
            raise Exception(f"Error al hacer click en el botón de confirmar: {str(e)}")

    def verify_logout(self) -> bool:
        """Verifica si se cerró sesión correctamente"""
        try:
            self.logger.info("Verificando si se cerró sesión correctamente")
            self.ui_adapter.wait_manager.wait_for_element_visible(*self.locators.lblLogoutSuccess)
            return self.ui_adapter.get_text(self.locators.lblLogoutSuccess) == "Tú sesión ha sido cerrada exitosamente."
        except Exception as e:
            self.logger.error(f"Error al verificar si se cerró sesión correctamente: {str(e)}")
            raise Exception(f"Error al verificar si se cerró sesión correctamente: {str(e)}")

    def logout(self) -> bool:
        """Cierra la sesión de la aplicación

        Raises:
            Exception: Error al cerrar sesión

        Returns:
            bool: True si se cerró sesión correctamente, False en caso contrario
        """
        try:
            self.logger.info("Cerrando sesión")
            self.onClick_ImageProfile()
            time.sleep(2)

            self.onClick_Logout()
            time.sleep(2)

            self.onClick_Confirmar()
            time.sleep(2)

            return self.verify_logout()
        except Exception as e:
            self.logger.error(f"Error al cerrar sesión: {str(e)}")
            raise Exception(f"Error al cerrar sesión: {str(e)}")

    def set_search(self, app_name: str):
        """Escribe en el campo de búsqueda

        Args:
            app_name (str): Nombre de la aplicación a buscar

        Raises:
            Exception: _description_
        """
        try:
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtSearch)
            self.ui_adapter.send_keys(self.locators.txtSearch, app_name)
        except Exception as e:
            self.logger.error(f"Error al escribir en el campo de búsqueda: {str(e)}")
            raise Exception(f"Error al escribir en el campo de búsqueda: {str(e)}")

    def search_button(self, app_name: str):
        """Busca una aplicación en la barra de búsqueda

        Args:
            app_name (str): Nombre de la aplicación a buscar
        """
        self.logger.info(f"Buscando la aplicación: [{app_name}]")
        self.onClick_search_button()
        time.sleep(3)

        self.logger.info("Escribiendo en el campo de búsqueda")
        self.set_search(app_name)
        time.sleep(2)

    def go_to_app(self, app_name: str, app_title: str):
        """Navega a una aplicación

        Args:
            app_name (str): Nombre de la aplicación
            app_title (str): Título de la aplicación

        Raises:
            Exception: Error al navegar a la aplicación
        """
        try:
            self.logger.info(f"Navegando a la aplicación: [{app_name}]")
            self.search_button(app_name)
            time.sleep(2)

            self.logger.info("Haciendo click en la aplicación")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*app_title)
            self.ui_adapter.click(app_title)
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Error al navegar a la aplicación: {str(e)}")
            raise Exception(f"Error al navegar a la aplicación: {str(e)}")

    def is_welcome_successful(self):
        """Verifica si se cargó la página de bienvenida

        Raises:
            Exception: Error al verificar si se cargó la página de bienvenida
        """
        try:
            self.ui_adapter.wait_manager.wait_for_page_load()
            self.logger.info("Verificando si se cargó la página de bienvenida")
            self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.app_system_date)
            self.logger.info(f"Fecha del sistema: {self.ui_adapter.get_text(self.locators.app_system_date)}")
            self.logger.info(f"UUID: {self.ui_adapter.get_text(self.locators.app_uuid)}")
            self.ui_adapter.wait_manager.wait_for_element_not_visible(*self.locators.app_loading)
            self.ui_adapter.wait_manager.wait_for_element_visible(*self.locators.divMenu)
            self.ui_adapter.wait_manager.wait_for_element_visible(*self.locators.divModulos)
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "is_welcome_successful")
            return True
        except Exception as e:
            self.logger.error(f"Error al verificar si se cargó la página de bienvenida: {str(e)}")
            raise Exception(f"Error al verificar si se cargó la página de bienvenida: {str(e)}")

    def is_app_loading(self) -> bool:
        """Verifica si la aplicación está cargando

        Raises:
            Exception: Error al verificar si la aplicación está cargando

        Returns:
            bool: True si la aplicación está cargando
        """
        try:
            self.ui_adapter.wait_manager.wait_for_attribute_not_value(*self.locators.app_loading, "class", "line-loader")
            return True
        except Exception as e:
            self.logger.error(f"Error al verificar si la aplicación está cargando: {str(e)}")
            raise Exception(f"Error al verificar si la aplicación está cargando: {str(e)}")
