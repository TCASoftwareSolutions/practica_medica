"""
# Clase: DataGridViewHelper
# Definición: Clase que contiene métodos para interactuar con DataGridViews.
"""

import time
from selenium.webdriver.common.by import By
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort

# from framework.ports.ui_port import UIPort
from framework.utilities.configuration import Configuration


class DataGridViewHelper:
    """Clase que contiene métodos para interactuar con DataGridViews." """

    txtSearchZone = (By.ID, "gridGlobalCatalog_SearchZone_Input")
    colSeleccionada = (By.XPATH, "//td[contains(@id,'gridGlobalCatalog_active_cell')]")
    btnSeleccionar = (By.XPATH, "//td[contains(@id,'gridGlobalCatalog_active_cell')]/child::a")
    grid = (By.XPATH, "//div[@class='alertify  ajs-movable ajs-closable ajs-pinnable ajs-zoom']//td[contains(@role,'gridcell')]")

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def set_search_zone(self, filtro):
        """Establece el filtro en la zona de búsqueda.

        Args:
            filtro (str): Filtro a establecer en la zona de búsqueda

        Raises:
            Exception: Error al establecer el filtro en la zona de búsqueda
        """
        try:
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.txtSearchZone)
            self.ui_adapter.send_keys_enter(self.txtSearchZone, filtro)
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Error al establecer el filtro en la zona de búsqueda: {e}")
            raise Exception(f"Error al establecer el filtro en la zona de búsqueda: {e}")

    def seleccionar(self, filtro):
        try:
            self.set_search_zone(filtro)
            dgv = self.ui_adapter.find_elements((By.XPATH, "//td[contains(@role,'gridcell')]"))
            for cell in dgv:
                if filtro in cell.text:
                    cell.click()
                    time.sleep(1)
                    break

            self.ui_adapter.click(self.colSeleccionada)
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento: {e}")
            raise Exception(f"Error al seleccionar el elemento: {e}")

    def seleccionar_en_grid_modal(self, filtro):
        try:
            self.set_search_zone(filtro)
            dgv = self.ui_adapter.find_elements((By.XPATH, "//td[contains(@role,'gridcell') and not(ancestor::div[contains(@class,'k-grid-content k-auto-scrollable')])]"))

            for cell in dgv:
                if filtro in cell.text:
                    cell.click()
                    time.sleep(1)
                    break

            self.ui_adapter.click(self.colSeleccionada)
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento: {e}")
            raise Exception(f"Error al seleccionar el elemento: {e}")

    def seleccionar_datagrid(self, dgv, filtro):
        try:
            self.ui_adapter.wait_manager.wait_for_element_clickable(*dgv)
            self.ui_adapter.click(dgv)
            time.sleep(2)
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.txtSearchZone)
            self.ui_adapter.send_keys_enter(self.txtSearchZone, filtro)
            time.sleep(2)
            datagridview = self.ui_adapter.find_elements(self.grid)
            for cell in datagridview:
                if filtro in cell.text:
                    cell.click()
                    break
            self.ui_adapter.click(self.colSeleccionada)
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento: {e}")
            raise Exception(f"Error al seleccionar el elemento: {e}")

    def selec_data(self, filtro):
        try:
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.txtSearchZone)
            datagridview = self.ui_adapter.find_elements(self.grid)
            for cell in datagridview:
                if filtro in cell.text:
                    # cell.click()
                    self.ui_adapter.click(self.colSeleccionada)
                    break
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento: {e}")
            raise Exception(f"Error al seleccionar el elemento: {e}")

    def seleccionar_datagrid_primer_elemento(self, dgv):
        try:
            self.ui_adapter.click(dgv)
            time.sleep(2)
            elementos = self.ui_adapter.find_elements((By.XPATH, "//td[contains(@role,'gridcell')]"))
            elementos[0].click()
        except Exception as e:
            self.logger.error(f"Error al seleccionar el primer elemento: {e}")
            raise Exception(f"Error al seleccionar el primer elemento: {e}")

    def seleccionar_vacio(self):
        try:
            dgv = self.ui_adapter.find_elements(
                (
                    By.CSS_SELECTOR,
                    "table:nth-child(1) > tbody:nth-child(2) > tr > td:nth-child(6)",
                )
            )
            for cell in dgv:
                if cell.text == "":
                    cell.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento vacío: {e}")
            raise Exception(f"Error al seleccionar el elemento vacío: {e}")

    def seleccionar_combobox(self, filtro):
        try:
            dgv = self.ui_adapter.find_elements((By.XPATH, "//td[contains(@id,'TKWizard1_pnlHabitacion_txtTipoHab')]"))
            for cell in dgv:
                if filtro in cell.get_attribute("textContent").strip():
                    cell.click()
                    break
        except Exception as e:
            self.logger.error(f"Error al seleccionar el elemento del ComboBox: {e}")
            raise Exception(f"Error al seleccionar el elemento del ComboBox: {e}")
