"""
# Clase: LoginPage
# Descripción: Clase para la página de login.
"""

import time
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.pages.login.locators import LoginLocators

# from framework.ports.ui_port import UIPort
# from framework.utilities.logger import setup_logger
from framework.utilities.combobox_helper import ComboBoxHelper
from framework.utilities.configuration import Configuration


class LoginPage:
    """Clase para la página de login"""

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = LoginLocators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

        self.combobox = ComboBoxHelper(self.ui_adapter, test_config)

    def set_username(self, username):
        """Ingresar usuario

        Args:
            username (_type_): Nombre de usuario

        Raises:
            Exception: Error al ingresar usuario
        """
        try:
            self.logger.info("Ingresando usuario")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtUsername)
            self.ui_adapter.send_keys(self.locators.txtUsername, username)
        except Exception as e:
            self.logger.error("Error al ingresar usuario: %s", str(e))
            raise Exception(f"Error al ingresar usuario: {str(e)}") from e

    def set_password(self, password):
        """Ingresar contraseña

        Args:
            password (str): Contraseña

        Raises:
            Exception: Error al ingresar contraseña
        """
        try:
            self.logger.info("Ingresando contraseña")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtPassword)
            self.ui_adapter.send_keys(self.locators.txtPassword, password)
        except Exception as e:
            self.logger.error("Error al ingresar contraseña: %s", str(e))
            raise Exception(f"Error al ingresar contraseña: {str(e)}")

    def set_company(self, company):
        """Seleccionar compañia

        Args:
            company (str): Nombre de la compañia

        Raises:
            Exception: Error al seleccionar compañia
        """
        try:
            self.logger.info("Seleccionando compañia")
            self.combobox.seleccionar_elemento_por_texto_open(company)
        except Exception as e:
            self.logger.error("Error al seleccionar compañia: %s", str(e))
            raise Exception(f"Error al seleccionar compañia: {str(e)}")

    def set_department(self, department):
        """Seleccionar departamento

        Args:
            department (str): Nombre del departamento

        Raises:
            Exception: Error al seleccionar departamento
        """
        try:
            self.logger.info("Seleccionando departamento")
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbDepartment, department)
        except Exception as e:
            self.logger.error("Error al seleccionar departamento: %s", str(e))
            raise Exception(f"Error al seleccionar departamento: {str(e)}")

    def set_username_confirm(self, username):
        """Confirma el usuario

        Args:
            username (str): Nombre de usuario

        Raises:
            Exception: Error al ingresar usuario de confirmación
        """
        try:
            self.logger.info("Ingresando usuario de confirmación")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtUsernameConfirm)
            self.ui_adapter.send_keys(self.locators.txtUsernameConfirm, username)
        except Exception as e:
            self.logger.error("Error al ingresar usuario de confirmación: %s", str(e))
            raise Exception(f"Error al ingresar usuario de confirmación: {str(e)}")

    def set_password_confirm(self, password):
        """Confirma la contrasena

        Args:
            password (str): Contraseña

        Raises:
            Exception: Error al ingresar contraseña de confirmación
        """
        try:
            self.logger.info("Ingresando contraseña de confirmación")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtPasswordConfirm)
            self.ui_adapter.send_keys(self.locators.txtPasswordConfirm, password)
        except Exception as e:
            self.logger.error("Error al ingresar contraseña de confirmación: %s", str(e))
            raise Exception(f"Error al ingresar contraseña de confirmación: {str(e)}")

    def onClick_aceptar_confirmacion(self):
        """Hace click en el botón de confirmación

        Raises:
            Exception: Error al hacer click en el botón de confirmación
        """
        try:
            self.logger.info("Haciendo click en el botón de confirmación")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnConfirmCredentials)
            self.ui_adapter.click(self.locators.btnConfirmCredentials)
        except Exception as e:
            self.logger.error("Error al hacer click en el botón de confirmación: %s", str(e))
            raise Exception(f"Error al hacer click en el botón de confirmación: {str(e)}")

    def onClick_cancelar_confirmacion(self):
        """Hace click en el botón de cancelación

        Raises:
            Exception: Error al hacer click en el botón de cancelación
        """
        try:
            self.logger.info("Haciendo click en el botón de cancelación")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnCancelarValidacionCredentials)
            self.ui_adapter.click(self.locators.btnCancelarValidacionCredentials)
        except Exception as e:
            self.logger.error("Error al hacer click en el botón de cancelación: %s", str(e))
            raise Exception(f"Error al hacer click en el botón de cancelación: {str(e)}")

    def onClick_aceptar_confirmacion_another_user(self):
        """Hace click en el botón de confirmación

        Raises:
            Exception: Error al hacer click en el botón de confirmación
        """
        try:
            self.logger.info("Haciendo click en el botón de confirmación")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnConfirmCredentialsAnotherUser)
            self.ui_adapter.click(self.locators.btnConfirmCredentialsAnotherUser)
        except Exception as e:
            self.logger.error("Error al hacer click en el botón de confirmación: %s", str(e))
            raise Exception(f"Error al hacer click en el botón de confirmación: {str(e)}")

    def click_loggin_button(self):
        """Hace clic en el boton de Iniciar Sesion

        Raises:
            Exception: Error al hacer clic en el boton de login
        """
        try:
            self.logger.info("Haciendo click en el botón de login")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnLogin)
            self.ui_adapter.click(self.locators.btnLogin)
        except Exception as e:
            self.logger.error("Error al hacer click en el botón de login: %s", str(e))
            raise Exception(f"Error al hacer click en el botón de login: {str(e)}")

    def enter_credentials(self, username, password, company, department):
        """Ingresar credenciales

        Args:
            username (str): Nombre de usuario
            password (str): Contraseña
            company (str): Nombre de la compañia
        """
        self.logger.info("Ingresando credenciales")

        self.set_username(username)
        time.sleep(2)

        self.set_password(password)
        time.sleep(1)

        self.ui_adapter.click(self.locators.txtUsername)
        time.sleep(1)

        self.set_company(company)
        time.sleep(2)

        self.set_department(department)
        time.sleep(1)

        self.ui_adapter.take_screenshot(self.test_config.logger_dir, "Captura de credenciales")

    def login(self, credentials):
        """Iniciar sesión

        Raises:
            Exception: Error al iniciar sesión

        Returns:
            bool: True si el login es exitoso, False en caso contrario
        """
        try:
            self.ui_adapter.navigate(self.ui_adapter.config.get("base_url"))
            self.enter_credentials(credentials.get("username"), credentials.get("password"), credentials.get("company"), credentials.get("department"))
            self.click_loggin_button()
        except Exception as e:
            self.logger.error("Error al iniciar sesión: %s", str(e))
            raise Exception(f"Error al iniciar sesión: {str(e)}")

    def do_login(self, credentials):
        """Realizar el login

        Args:
            credentials (dict): Credenciales de usuario

        Raises:
            Exception: Error al realizar el login
        """
        try:
            self.enter_credentials(credentials.get("username"), credentials.get("password"), credentials.get("company"), credentials.get("department"))
            self.click_loggin_button()
        except Exception as e:
            self.logger.error("Error al iniciar sesión: %s", str(e))
            raise Exception(f"Error al iniciar sesión: {str(e)}")

    def confirm_credentials(self, pwd):
        """Confirma las credenciales

        Args:
            pwd (str): Contraseña
        """
        self.logger.info("Confirmando credenciales")
        self.set_password_confirm(pwd)
        self.onClick_aceptar_confirmacion()

    def is_confirm_credentials_visible(self):
        """Verifica si la ventana de confirmación de credenciales es visible

        Returns:
            bool: True si la ventana de confirmación de credenciales es visible
        """
        self.logger.info("Verificando si la ventana de confirmación de credenciales es visible")
        return self.ui_adapter.find_element_is_exist(self.locators.confirmCredentials)

    def change_user_credentials(self, username, password):
        """Cambiar las credenciales de usuario

        Args:
            username (str): Nombre de usuario
            password (str): Contraseña
        """
        self.logger.info("Confirmando credenciales")
        self.set_username_confirm(username)
        self.set_password_confirm(password)
        self.onClick_aceptar_confirmacion_another_user()

    def deny_credentials(self):
        """Denegar las credenciales"""
        self.logger.info("Denegando credenciales")
        self.onClick_cancelar_confirmacion()
