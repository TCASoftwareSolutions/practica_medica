"""
# Clase ComboBoxHelper
# Descripción: Clase que contiene métodos para interactuar con los ComboBox.
"""

import random
import time
from selenium.webdriver.common.by import By
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort

# from framework.ports.ui_port import UIPort
from framework.utilities.configuration import Configuration


class ComboBoxHelper:
    """Clase que contiene métodos para interactuar con los ComboBox."""

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def seleccionar_elemento_por_texto(self, combo_box, elemento, clase="rddlItem"):
        """
        Selecciona un elemento de un ComboBox.
        :param combo_box: ComboBox.
        :param elemento: Elemento a seleccionar.
        :param clase: Clase de la lista.
        """
        try:
            self.ui_adapter.click(combo_box)
            time.sleep(2)
            elements = self.ui_adapter.find_elements(
                (
                    By.XPATH,
                    f"//div[contains(@style,'overflow: visible')]//li[contains(@class,'{clase}')]",
                )
            )
            time.sleep(1)
            for item in elements:
                if elemento in item.get_attribute("textContent"):
                    item.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento: {e}")
            raise Exception(f"Error al seleccionar el elemento: {e}")

    def seleccionar_primer_elemento(self, combo_box):
        """
        Selecciona el primer elemento de un ComboBox.
        :param combo_box: ComboBox.
        """
        self.ui_adapter.click(combo_box)
        time.sleep(2)
        elements = self.ui_adapter.find_elements((By.XPATH, "//li[contains(@class,'rddlItem')]"))
        time.sleep(1)
        elements[0].click()

    def seleccionar_ultimo_elemento(self, combo_box, lista):
        """
        Selecciona el último elemento de un ComboBox.
        :param combo_box: ComboBox.
        """
        try:
            combo_box.click()
            elements = lista
            time.sleep(1)
            elements[-1].click()
        except Exception as e:
            self.logger.error(f"Error al seleccionar el último elemento: {e}")
            raise Exception(f"Error al seleccionar el último elemento: {e}")

    def seleccionar_elemento_aleatorio(self, combo_box, clase="rddlItem"):
        """
        Selecciona un elemento aleatorio de un ComboBox.
        :param combo_box: ComboBox.
        :param clase: Clase de la lista.
        """
        try:
            self.ui_adapter.click(combo_box)
            time.sleep(2)
            elements = self.ui_adapter.find_elements(
                (
                    By.XPATH,
                    f"//div[contains(@style,'overflow: visible')]//li[contains(@class,'{clase}')]",
                )
            )
            if len(elements) == 1:
                random_element = elements[0]
            else:
                random_element = elements[random.randint(1, len(elements) - 1)]
            self.logger.info(f'Elemento aleatorio: {random_element.get_attribute("textContent")}')

            for item in elements:
                if random_element.get_attribute("textContent") in item.get_attribute("textContent"):
                    item.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento aleatorio: {e}")
            raise Exception(f"Error al seleccionar el elemento aleatorio: {e}")

    def seleccionar_elemento_por_indice(self, combo_box, lista, indice):
        """
        Selecciona un elemento de un ComboBox por su índice.
        :param combo_box: ComboBox.
        :param lista: Lista de elementos.
        :param indice: Índice del elemento a seleccionar.
        """
        try:
            combo_box.click()
            elements = lista
            time.sleep(1)
            elements[indice].click()
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento por índice: {e}")
            raise Exception(f"Error al seleccionar el elemento por índice: {e}")

    def revisar_elementos(self, combo_box, lista):
        """
        Revisa los elementos de un ComboBox.
        :param combo_box: ComboBox.
        :param lista: Lista de elementos
        """
        try:
            combo_box.click()
            elements = lista
            time.sleep(1)
            for item in elements:
                self.logger.info(f'Elemento: {item.get_attribute("textContent")}')
        except Exception as e:
            self.logger.error(f"Error al revisar los elementos: {e}")
            raise Exception(f"Error al revisar los elementos: {e}")

    def obtener_elementos(self, combo_box):
        """
        Obtiene los elementos de un ComboBox.

        :param combo_box: ComboBox.
        """
        try:
            combo_box.click()
            elements = self.ui_adapter.find_elements((By.XPATH, "//li[contains(@class,'rddlItem')]"))
            time.sleep(1)
            return elements
        except Exception as e:
            self.logger.error(f"Error al obtener los elementos: {e}")
            raise Exception(f"Error al obtener los elementos: {e}")

    def vacio(self, combo_box):
        """
        Verifica si un ComboBox está vacío.

        :param combo_box: ComboBox.
        """
        try:
            combo_box.click()
            elements = self.ui_adapter.find_elements((By.XPATH, "//li[contains(@class,'rddlItem')]"))
            time.sleep(1)
            return len(elements) == 0
        except Exception as e:
            self.logger.error(f"Error al verificar si el ComboBox está vacío: {e}")
            raise Exception(f"Error al verificar si el ComboBox está vacío: {e}")

    def seleccionar_elemento_en_tabla(self, combo_box, elemento, id="", clase="rddlItem"):
        """
        Selecciona un elemento de un ComboBox.

        :param combo_box: ComboBox.
        :param elemento: Elemento a seleccionar.
        """
        try:
            self.ui_adapter.click(combo_box)
            time.sleep(2)
            elements = self.ui_adapter.find_elements(
                (
                    By.XPATH,
                    f"//div[contains(@id,'{id}') and contains(@style,'visibility: visible')]//li[contains(@class,'{clase}')]",
                )
            )
            self.logger.info(f"Elementos: {len(elements)}")
            self.logger.info(f"Elementos: {elements}")
            time.sleep(1)
            elemento_seleccionado = 0
            for item in elements:
                elemento_seleccionado += 1
                self.logger.info(f"Elemento: {item}")
                id = f"hot025_TKWizard1_pnlHabitacion_txtTipoHab_i{elemento_seleccionado}_Fld0"
                if elemento in self.ui_adapter.get_text((By.XPATH, "//td[contains(@id,{id})]")):
                    item.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento en la tabla: {e}")
            raise Exception(f"Error al seleccionar el elemento en la tabla: {e}")

    def seleccionar_elemento_por_texto_open(self, elemento, clase="rddlItem"):
        """
        Selecciona un elemento de un ComboBox.

        :param cmbBox: ComboBox.
        :param elemento: Elemento a seleccionar.
        """
        try:
            elements = self.ui_adapter.find_elements(
                (
                    By.XPATH,
                    f"//div[contains(@style,'overflow: visible')]//li[contains(@class,'{clase}')]",
                )
            )
            time.sleep(1)
            for item in elements:
                if elemento in item.get_attribute("textContent"):
                    item.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento: {e}")
            raise Exception(f"Error al seleccionar el elemento: {e}")

    def select_by_value(self, cmb, list_elements, value):
        """
        Selecciona un item de un ComboBox.

        :param cmb: ComboBox.
        :param list_elements: Lista de elementos.
        :param value: Valor a seleccionar.
        """
        try:
            self.ui_adapter.click(cmb)
            time.sleep(2)
            elements = self.ui_adapter.find_elements((By.XPATH, list_elements))
            time.sleep(1)

            for element in elements:
                if value in element.get_attribute("textContent"):
                    element.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el item: {e}")
            raise Exception(f"Error al seleccionar el item: {e}")

    def get_selected_text(self, combo_box):
        """
        Obtiene el texto seleccionado de un ComboBox.

        :param combo_box: ComboBox.
        """
        try:
            return combo_box.get_attribute("textContent")
        except Exception as e:
            self.logger.error(f"Error al obtener el texto seleccionado: {e}")
            raise Exception(f"Error al obtener el texto seleccionado: {e}")
