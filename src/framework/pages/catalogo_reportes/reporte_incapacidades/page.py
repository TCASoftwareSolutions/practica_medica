import time
import pytest
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.catalogo_reportes.reporte_incapacidades.locators import ReporteDeIncapacidadesLocators as Locators
from framework.utilities.datagridview_helper import DataGridViewHelper
from framework.utilities.combobox_helper import ComboBoxHelper


class ReporteDeIncapacidadesPage:
    """Clase que contiene los metodos de la pagina reporte de incapacidades.
    Esta clase permite interactuar con sus elementos
    """

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

        self.data = self.ui_adapter.load_data("informe_de_solicitudes")

        self.datagrid = DataGridViewHelper(self.ui_adapter, self.test_config)
        self.combobox = ComboBoxHelper(self.ui_adapter, self.test_config)

    def onClick_Cerrar(self):
        """Hacer click en Cerrar
        Raises:
            Exception: Error al hacer click en Cerrar
        """
        try:
            self.logger.info("Haciendo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Cerrar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.app_close)
            self.ui_adapter.click(self.locators.app_close)
            self.logger.info("Se hizo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Cerrar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Cerrar: {e}")
            raise Exception(f"Error al hacer click en Cerrar: {e}")

    def onClick_Modificar_Parametros(self):
        """Hacer click en Modificar los Parametros
        Raises:
            Exception: Error al hacer click en Modificar los Parametros
        """
        try:
            self.logger.info("Haciendo click en Modificar los Parametros")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Modificar los Parametros")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnModificarParam)
            self.ui_adapter.click(self.locators.btnModificarParam)
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Modificar los Parametros")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Modificar los Parametros: {e}")
            raise Exception(f"Error al hacer click en Modificar los Parametros: {e}")

    def set_Campos_Fecha(self, fch_inicial: str, fch_final: str):
        """Insertar datos en campos de fecha
        Raises:
            Exception: Error al insertar datos en campos de fecha
        """
        try:
            self.logger.info("Insertando datos en campos de fecha")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Insertando datos en campos de fecha")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.fchInicail)
            self.ui_adapter.clear(self.locators.fchInicail)
            self.ui_adapter.send_keys(self.locators.fchInicail, fch_inicial)

            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.fchFinal)
            self.ui_adapter.clear(self.locators.fchFinal)
            self.ui_adapter.send_keys(self.locators.fchFinal, fch_final)
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se insertaron datos en campos de fecha")

        except Exception as e:
            self.logger.error(f"Error al hacer click al Insertar datos en campos de fecha: {e}")
            raise Exception(f"Error al hacer click al Insertar datos en campos de fecha: {e}")

    def onClick_Actualizar(self):
        """Hacer click en Actualizar
        Raises:
            Exception: Error al hacer click en Actualizar
        """
        try:
            self.logger.info("Haciendo click en Actualizar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Actualizar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnActualizar)
            self.ui_adapter.double_click(self.locators.btnActualizar)
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Actualizar")
            self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.tableRow)

        except Exception as e:
            self.logger.error(f"Error al hacer click en Actualizar: {e}")
            raise Exception(f"Error al hacer click en Actualizar: {e}")

    def get_Total_Rows(self):
        try:
            num = ""
            tableInfo = self.ui_adapter.get_text(self.locators.tableInfo)
            Totalrows = tableInfo[-3:]

            for char in Totalrows:
                if char.isnumeric():
                    num = num + char
            if num is not None:
                return num
            else:
                return 0
        except Exception as e:
            self.logger.error(f"Error al obtener el numero de filas: {e}")
            raise Exception(f"Error al obtener el numero de filas: {e}")

    def compare_Total_Rows(self, rows_ini: int, rows_fin: int):
        try:

            if rows_ini != 400 and rows_fin != 0:
                if rows_ini != rows_fin:
                    self.logger.info("El programa hizo la busqueda exitosamente")
            else:
                pytest.skip("No fue posible determinar si el programa encontro o no mas filas")

        except Exception as e:
            self.logger.error(f"Error al comparar los totales: {e}")
            raise Exception(f"Error al comparar los totales: {e}")
