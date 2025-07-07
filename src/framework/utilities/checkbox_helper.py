"""
# Clase: CheckBoxHelper
# Descripción: Clase que contiene métodos para interactuar con checkboxes.
"""

import time
from selenium.webdriver.common.by import By
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort

# from framework.ports.ui_port import UIPort
from framework.utilities.configuration import Configuration


class CheckBoxHelper:
    """Clase que contiene métodos para interactuar con checkboxes."""

    logger_name = "CheckBoxHelper_logger"

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def set_checkbox(self, checkbox, status):
        """
        Selecciona un checkbox.
        :param checkbox: Checkbox.
        :param status: Estado del checkbox.
        """
        try:
            if status:
                if not checkbox.is_selected():
                    checkbox.click()
            else:
                if checkbox.is_selected():
                    checkbox.click()
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Error al seleccionar el checkbox: {e}")
            raise Exception(f"Error al seleccionar el checkbox: {e}")

    def set_checkboxes(self, checkboxes, status):
        """
        Selecciona varios checkboxes.
        :param checkboxes: Lista de checkboxes.
        :param status: Estado del checkbox.
        """
        try:
            for checkbox in checkboxes:
                self.set_checkbox(checkbox, status)
        except Exception as e:
            self.logger.error(f"Error al seleccionar los checkboxes: {e}")
            raise Exception(f"Error al seleccionar los checkboxes: {e}")

    def checked_lista(self, checkbox, elemento, status=True, clase="rddlItem"):
        """
        Selecciona varios checkboxes.
        :param checkbox: checkbox.
        :param elemento: Elemento a seleccionar.
        :param status: Estado del checkbox.
        :param clase: Clase de la lista.
        """
        try:
            self.ui_adapter.click(checkbox)
            time.sleep(2)
            elements = self.ui_adapter.find_elements((By.XPATH, f"//div[contains(@style,'overflow: visible')]//li[contains(@class,'{clase}')]"))
            time.sleep(1)
            for item in elements:
                if elemento in item.get_attribute("textContent").strip():
                    if status:
                        if not item.is_selected():
                            item.click()
                    else:
                        if item.is_selected():
                            item.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el checkbox: {e}")
            raise Exception(f"Error al seleccionar el checkbox: {e}")
