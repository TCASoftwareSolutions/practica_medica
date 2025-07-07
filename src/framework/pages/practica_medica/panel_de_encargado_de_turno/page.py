import time
from selenium.webdriver.common.by import By
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.practica_medica.agenda_medica.locators import AgendaMedicaLocators as Locators
from framework.utilities.combobox_helper import ComboBoxHelper
from framework.utilities.datagridview_helper import DataGridViewHelper


class PanelDeEncargadoDeTurnoPage:
    """Clase que contiene los metodos de la pagina Portal de Operadores"""

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

        self.data = self.ui_adapter.load_data("agenda_medica")

        self.combobox = ComboBoxHelper(self.ui_adapter, self.test_config)
        self.datagrid = DataGridViewHelper(self.ui_adapter, self.test_config)
        self.numero_de_cita = None

    def onClick_Cerrar(self):
        """Hacer click en Cerrar
        Raises:
            Exception: Error al hacer click en Cerrar
        """
        try:
            self.logger.info("Haciendo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Cerrar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipCerrar)
            self.ui_adapter.click(self.locators.tipCerrar)
            self.logger.info("Se hizo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Cerrar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Cerrar: {e}")
            raise Exception(f"Error al hacer click en Cerrar: {e}")

    def onClick_Actualizar(self):
        """Hacer click en Actualizar
        Raises:
            Exception: Error al hacer click en Actualizar
        """
        try:
            self.logger.info("Haciendo click en el botón Actualizar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Actualizar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipActualizar)
            self.ui_adapter.click(self.locators.tipActualizar)
            self.logger.info("Se hizo click en el botón Actualizar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Actualizar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Actualizar: {e}")
            raise Exception(f"Error al hacer click en Actualizar: {e}")

    def onClick_Limpiar(self):
        """Hacer click en Limpiar
        Raises:
            Exception: Error al hacer click en Limpiar
        """
        try:
            self.logger.info("Haciendo click en el botón Limpiar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Limpiar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipLimpiar)
            self.ui_adapter.click(self.locators.tipLimpiar)
            self.logger.info("Se hizo click en el botón Limpiar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Limpiar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Limpiar: {e}")
            raise Exception(f"Error al hacer click en Limpiar: {e}")

    def set_especialidad(self, especialidad_data: str):
        """Seleccionar una especialidad en el combobox de Especialidad
        Args:
            especialidad (str): Nombre de la especialidad a seleccionar
        Raises:
            Exception: Error al seleccionar la especialidad
        """
        try:
            especialidad = especialidad_data if not especialidad_data else "MEDICINA GENERAL"
            self.logger.info(f"Seleccionando la especialidad: {especialidad}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Seleccionando la especialidad: {especialidad}")
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbEspecialidad, especialidad)
            self.logger.info(f"Se seleccionó la especialidad: {especialidad}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se seleccionó la especialidad: {especialidad}")
        except Exception as e:
            self.logger.error(f"Error al seleccionar la especialidad '{especialidad}': {e}")
            raise Exception(f"Error al seleccionar la especialidad '{especialidad}': {e}")

    def onClick_Filtrar(self):
        """Hacer click en Filtrar
        Raises:
            Exception: Error al hacer click en Filtrar
        """
        try:
            self.logger.info("Haciendo click en el botón Filtrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Filtrar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnFiltrar)
            self.ui_adapter.click(self.locators.btnFiltrar)
            self.logger.info("Se hizo click en el botón Filtrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Filtrar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Filtrar: {e}")
            raise Exception(f"Error al hacer click en Filtrar: {e}")

    def set_escalas(self, escala_data: str):
        """Seleccionar una escala en el combobox de Escalas
        Args:
            escala_data (str): Nombre de la escala a seleccionar
        Raises:
            Exception: Error al seleccionar la escala
        """
        try:
            escala = escala_data if not escala_data else "Default"
            self.logger.info(f"Seleccionando la escala: {escala}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Seleccionando la escala: {escala}")
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbEscalas, escala)
            self.logger.info(f"Se seleccionó la escala: {escala}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se seleccionó la escala: {escala}")
        except Exception as e:
            self.logger.error(f"Error al seleccionar la escala '{escala}': {e}")
            raise Exception(f"Error al seleccionar la escala '{escala}': {e}")

    def find_horario(self, horario_data: dict):
        """Buscar un horario por fecha y hora
        Args:
            horario_data (dict): Diccionario con la fecha y hora a buscar
        Raises:
            Exception: Error al buscar el horario
        """
        try:
            hora = horario_data.get("hora", "Default")
            periodo = horario_data.get("periodo", "AM")
            self.logger.info(f"Buscando el horario: {hora} {periodo}")
            horario = self.ui_adapter.find_elements(self.locators.lblHorario)
            cita = 0
            for h in horario:
                cita += 1
                self.logger.info(f"Verificando horario {cita}: {h.text}")
                if h.text == f"{hora} {periodo}":
                    self.logger.info(f"Horario encontrado: {h.text}")
                    return cita
        except Exception as e:
            self.logger.error(f"Error al buscar el horario '{hora}': {e}")
            raise Exception(f"Error al buscar el horario '{hora}': {e}")

    def create_appointment(self, appointment_data: dict):
        """Crear una cita médica
        Args:
            appointment_data (dict): Diccionario con los datos de la cita
        Raises:
            Exception: Error al crear la cita
        """
        try:
            self.logger.info(f"Creando cita médica con los datos: {appointment_data}")
            horario = appointment_data.get("horario", "Default")
            cita = (By.XPATH, f"//div[@class='k-scheduler-content']//tr[{horario}]/td[@class='k-today' and @role='gridcell']")
            self.ui_adapter.double_click(cita)
            time.sleep(5)  # Esperar a que se abra el formulario de cita
        except Exception as e:
            self.logger.error(f"Error al crear la cita médica: {e}")
            raise Exception(f"Error al crear la cita médica: {e}")

    def enter_appointment(self, appointment_data: dict):
        """Ingresar los detalles de la cita médica
        Args:
            appointment_details (dict): Diccionario con los detalles de la cita
        Raises:
            Exception: Error al ingresar los detalles de la cita
        """
        try:
            self.logger.info(f"Creando cita médica con los datos: {appointment_data}")
            horario = appointment_data.get("horario", "Default")
            cita = (By.XPATH, f"//div[@class='k-scheduler-content']//tr[{horario}]/td[@class='k-today' and @role='gridcell']")
            self.ui_adapter.hover(cita)
            time.sleep(2)  # Esperar a que se abra el formulario de cita
            self.ui_adapter.click(self.locators.btnModulo)
            time.sleep(20)  # Esperar a que se abra el formulario de cita
        except Exception as e:
            self.logger.error(f"Error al crear la cita médica: {e}")
            raise Exception(f"Error al crear la cita médica: {e}")

    def find_cita(self, numero_de_cita: str):
        """Buscar una cita por número de cita
        Args:
            numero_de_cita (str): Número de cita a buscar
        Raises:
            Exception: Error al buscar la cita
        """
        try:
            self.logger.info(f"Buscando la cita con número: {numero_de_cita}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Buscando la cita con número: {numero_de_cita}")
            self.numero_de_cita = numero_de_cita
            self.datagrid.buscar_elemento_por_texto(self.locators.dgvCitas, numero_de_cita)
            self.logger.info(f"Cita encontrada con número: {numero_de_cita}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Cita encontrada con número: {numero_de_cita}")
        except Exception as e:
            self.logger.error(f"Error al buscar la cita con número '{numero_de_cita}': {e}")
            raise Exception(f"Error al buscar la cita con número '{numero_de_cita}': {e}")
