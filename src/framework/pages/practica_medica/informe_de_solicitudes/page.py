from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.practica_medica.informe_de_solicitudes.locators import InformeDeSolicitudesLocators as Locators
from framework.utilities.combobox_helper import ComboBoxHelper


class InformeDeSolicitudesPage:
    """Clase que contiene los metodos de la pagina Informe de Solicitudes.
    Esta clase permite interactuar con los elementos de la pagina Informe de Solicitudes
    """

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

        self.data = self.ui_adapter.load_data("informe_de_solicitudes")

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

    def onClick_Limpiar(self):
        """Hacer click en Limpiar
        Raises:
            Exception: Error al hacer click en Limpiar
        """
        try:
            self.logger.info("Haciendo click en el botón Limpiar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Limpiar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_limpiar)
            self.ui_adapter.click(self.locators.btn_limpiar)
            self.logger.info("Se hizo click en el botón Limpiar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Limpiar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Limpiar: {e}")
            raise Exception(f"Error al hacer click en Limpiar: {e}")

    def set_tipo_de_informe(self, tipo_de_informe_data: str):
        """Seleccionar un tipo de informe en el combobox de Tipo de Informe
        Args:
            tipo_de_informe_data (str): Nombre del tipo de informe a seleccionar
        Raises:
            Exception: Error al seleccionar el tipo de informe
        """
        try:
            tipo_de_informe = tipo_de_informe_data if not tipo_de_informe_data else "Medicamentos"
            self.logger.info(f"Seleccionando el tipo de informe: {tipo_de_informe}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Seleccionando el tipo de informe: {tipo_de_informe}")
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmb_tipo_de_informe, tipo_de_informe)
            self.logger.info(f"Se seleccionó el tipo de informe: {tipo_de_informe}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se seleccionó el tipo de informe: {tipo_de_informe}")
        except Exception as e:
            self.logger.error(f"Error al seleccionar el tipo de informe '{tipo_de_informe}': {e}")
            raise Exception(f"Error al seleccionar el tipo de informe '{tipo_de_informe}': {e}")

    def set_id(self, id_data: str):
        """Ingresar el ID en el campo de texto ID
        Args:
            id_data (str): ID a ingresar
        Raises:
            Exception: Error al ingresar el ID
        """
        try:
            self.logger.info(f"Ingresando el ID: {id_data}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Ingresando el ID: {id_data}")
            self.ui_adapter.wait_manager.wait_for_element_visible(*self.locators.txt_id)
            self.ui_adapter.send_keys(self.locators.txt_id, id_data)
            self.logger.info(f"Se ingresó el ID: {id_data}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se ingresó el ID: {id_data}")
        except Exception as e:
            self.logger.error(f"Error al ingresar el ID '{id_data}': {e}")
            raise Exception(f"Error al ingresar el ID '{id_data}': {e}")

    def set_tipo_de_documento(self, tipo_de_documento_data: str):
        """Seleccionar un tipo de documento en el combobox de Tipo de Documento
        Args:
            tipo_de_documento_data (str): Nombre del tipo de documento a seleccionar
        Raises:
            Exception: Error al seleccionar el tipo de documento
        """
        try:
            tipo_de_documento = tipo_de_documento_data if not tipo_de_documento_data else "Cédula"
            self.logger.info(f"Seleccionando el tipo de documento: {tipo_de_documento}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Seleccionando el tipo de documento: {tipo_de_documento}")
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmb_tipo_de_documento, tipo_de_documento)
            self.logger.info(f"Se seleccionó el tipo de documento: {tipo_de_documento}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se seleccionó el tipo de documento: {tipo_de_documento}")
        except Exception as e:
            self.logger.error(f"Error al seleccionar el tipo de documento '{tipo_de_documento}': {e}")
            raise Exception(f"Error al seleccionar el tipo de documento '{tipo_de_documento}': {e}")

    def set_clave_de_documento(self, clave_de_documento_data: str):
        """Ingresar la clave de documento en el campo de texto Clave de Documento
        Args:
            clave_de_documento_data (str): Clave de documento a ingresar
        Raises:
            Exception: Error al ingresar la clave de documento
        """
        try:
            clave_de_documento = clave_de_documento_data if clave_de_documento_data else "1234567890"
            self.logger.info(f"Ingresando la clave de documento: {clave_de_documento}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Ingresando la clave de documento: {clave_de_documento}")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txt_clave_de_documento)
            self.ui_adapter.send_keys(self.locators.txt_clave_de_documento, clave_de_documento)
            self.logger.info(f"Se ingresó la clave de documento: {clave_de_documento}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se ingresó la clave de documento: {clave_de_documento}")
        except Exception as e:
            self.logger.error(f"Error al ingresar la clave de documento '{clave_de_documento}': {e}")
            raise Exception(f"Error al ingresar la clave de documento '{clave_de_documento}': {e}")

    def onClick_Filtrar(self):
        """Hacer click en Filtrar
        Raises:
            Exception: Error al hacer click en Filtrar
        """
        try:
            self.logger.info("Haciendo click en el botón Filtrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Filtrar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_filtrar)
            self.ui_adapter.click(self.locators.btn_filtrar)
            self.logger.info("Se hizo click en el botón Filtrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Filtrar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Filtrar: {e}")
            raise Exception(f"Error al hacer click en Filtrar: {e}")

    def onClick_Medicamentos(self):
        """Hacer click en Medicamentos
        Raises:
            Exception: Error al hacer click en Medicamentos
        """
        try:
            self.logger.info("Haciendo click en el botón Medicamentos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Medicamentos")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_medicamentos)
            self.ui_adapter.click(self.locators.btn_medicamentos)
            self.logger.info("Se hizo click en el botón Medicamentos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Medicamentos")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Medicamentos: {e}")
            raise Exception(f"Error al hacer click en Medicamentos: {e}")

    def onClick_Laboratorio(self):
        """Hacer click en Laboratorio
        Raises:
            Exception: Error al hacer click en Laboratorio
        """
        try:
            self.logger.info("Haciendo click en el botón Laboratorio")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Laboratorio")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_laboratorio)
            self.ui_adapter.click(self.locators.btn_laboratorio)
            self.logger.info("Se hizo click en el botón Laboratorio")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Laboratorio")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Laboratorio: {e}")
            raise Exception(f"Error al hacer click en Laboratorio: {e}")

    def onClick_Imagenes(self):
        """Hacer click en Imágenes
        Raises:
            Exception: Error al hacer click en Imágenes
        """
        try:
            self.logger.info("Haciendo click en el botón Imágenes")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Imágenes")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_imagenes)
            self.ui_adapter.click(self.locators.btn_imagenes)
            self.logger.info("Se hizo click en el botón Imágenes")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Imágenes")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Imágenes: {e}")
            raise Exception(f"Error al hacer click en Imágenes: {e}")

    def onClick_Exportar_PDF(self):
        """Hacer click en Exportar PDF
        Raises:
            Exception: Error al hacer click en Exportar PDF
        """
        try:
            self.logger.info("Haciendo click en el botón Exportar PDF")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Exportar PDF")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_exportar_pdf)
            self.ui_adapter.click(self.locators.btn_exportar_pdf)
            self.logger.info("Se hizo click en el botón Exportar PDF")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Exportar PDF")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Exportar PDF: {e}")
            raise Exception(f"Error al hacer click en Exportar PDF: {e}")

    def onClick_Exportar_Excel(self):
        """Hacer click en Exportar Excel
        Raises:
            Exception: Error al hacer click en Exportar Excel
        """
        try:
            self.logger.info("Haciendo click en el botón Exportar Excel")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Exportar Excel")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_exportar_excel)
            self.ui_adapter.click(self.locators.btn_exportar_excel)
            self.logger.info("Se hizo click en el botón Exportar Excel")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Exportar Excel")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Exportar Excel: {e}")
            raise Exception(f"Error al hacer click en Exportar Excel: {e}")

    def onClick_Exportar_CSV(self):
        """Hacer click en Exportar CSV
        Raises:
            Exception: Error al hacer click en Exportar CSV
        """
        try:
            self.logger.info("Haciendo click en el botón Exportar CSV")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Exportar CSV")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btn_exportar_csv)
            self.ui_adapter.click(self.locators.btn_exportar_csv)
            self.logger.info("Se hizo click en el botón Exportar CSV")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Exportar CSV")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Exportar CSV: {e}")
            raise Exception(f"Error al hacer click en Exportar CSV: {e}")

    def is_medicamentos_visible(self) -> bool:
        """Verifica si los medicamentos están visibles en el informe de solicitudes
        Returns:
            bool: True si los medicamentos están visibles, False en caso contrario
        """
        try:
            self.logger.info("Verificando si los medicamentos están visibles")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando si los medicamentos están visibles")
            is_visible = self.ui_adapter.wait_manager.wait_for_element_not_visible(*self.locators.lbl_no_data)
            self.logger.info(f"Los medicamentos {'están' if is_visible else 'no están'} visibles")
            return is_visible
        except Exception as e:
            self.logger.error(f"Error al verificar la visibilidad de los medicamentos: {e}")
            raise Exception(f"Error al verificar la visibilidad de los medicamentos: {e}")

    def is_laboratorio_visible(self) -> bool:
        """Verifica si el laboratorio está visible en el informe de solicitudes
        Returns:
            bool: True si el laboratorio está visible, False en caso contrario
        """
        try:
            self.logger.info("Verificando si el laboratorio está visible")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando si el laboratorio está visible")
            is_visible = self.ui_adapter.wait_manager.wait_for_element_not_visible(*self.locators.lbl_no_data)
            self.logger.info(f"El laboratorio {'está' if is_visible else 'no está'} visible")
            return is_visible
        except Exception as e:
            self.logger.error(f"Error al verificar la visibilidad del laboratorio: {e}")
            raise Exception(f"Error al verificar la visibilidad del laboratorio: {e}")

    def is_imagenes_visible(self) -> bool:
        """Verifica si las imágenes están visibles en el informe de solicitudes
        Returns:
            bool: True si las imágenes están visibles, False en caso contrario
        """
        try:
            self.logger.info("Verificando si las imágenes están visibles")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando si las imágenes están visibles")
            is_visible = self.ui_adapter.wait_manager.wait_for_element_not_visible(*self.locators.lbl_no_data)
            self.logger.info(f"Las imágenes {'están' if is_visible else 'no están'} visibles")
            return is_visible
        except Exception as e:
            self.logger.error(f"Error al verificar la visibilidad de las imágenes: {e}")
            raise Exception(f"Error al verificar la visibilidad de las imágenes: {e}")
