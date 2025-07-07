import time
import pytest
from datetime import datetime
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.menu_operadores.portal_de_operadores.workflow import PortalDeOperadoresWorkflow


@pytest.mark.load
@pytest.mark.pm_callcenter
class TestPortalDeOperadores:
    """Conjunto de pruebas para el programa Portal de Operadores"""

    logger_name = "TestPortalDeOperadores_Logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"load/menu_operadores/portal_de_operadores/portal_de_operadores_{logger_date}/portal_de_operadores_{logger_datetime}"
    screenshot_dir = f"load/menu_operadores/portal_de_operadores/portal_de_operadores_{logger_date}/portal_de_operadores_{logger_datetime}"

    def setup_test(self, test_name: str, session_id: str = None):
        """Configura el test con el nombre del test y el directorio de capturas de pantalla y logs

        Args:
            test_name (str): Nombre del test
        """
        self.logger_name = f"{session_id}::{self.logger_name}::{test_name}"
        self.logger_dir = f"{self.logger_dir}/{session_id}-{test_name}"
        self.screenshot_dir = f"{self.screenshot_dir}/{session_id}-{test_name}"

    datos_beneficiario = None

    def test01_Open_Program(self, ui_adapter: UIPort):
        """Prueba de apertura del programa Portal de Operadores"""
        test_name = "Test01_Open_Program"
        self.setup_test(test_name, ui_adapter.driver.session_id)
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores.onClick_Cerrar()
        workflow.terminate()

    def test02_Registro_de_beneficiario(self, ui_adapter: UIPort):
        # ""Prueba de registro de un beneficiario""
        test_name = "test02_Registro_de_beneficiario"
        self.setup_test(test_name)
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores_data = workflow.load_data()
        test_config.logger.info(f"Datos de prueba cargados: {portal_de_operadores_data}")

        portal_de_operadores.set_identificacion_del_beneficiario(portal_de_operadores_data.get("registro").get("identificacion"))
        codigo_OTP = portal_de_operadores.data.get("codigo_OTP")
        time.sleep(2)
        portal_de_operadores.set_verificacion_de_codigo(codigo_OTP)
        time.sleep(2)
        portal_de_operadores.set_resumen_del_registro(portal_de_operadores_data.get("registro").get("resumen"))
        time.sleep(6)
        assert portal_de_operadores.verficar_beneficiario_registrado_correctamente()
        time.sleep(5)
        portal_de_operadores.onClick_Cerrar()
        time.sleep(2)
        workflow.terminate()

    def test03_Agendar_Cita(self, ui_adapter: UIPort):
        # ""Prueba de programacion de una cita médica""
        test_name = "test03_Agendar_Cita"
        self.setup_test(test_name)
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores_data = workflow.load_data()
        test_config.logger.info(f"Datos de prueba cargados: {portal_de_operadores_data}")
        codigo_OTP = portal_de_operadores.data.get("codigo_OTP")

        portal_de_operadores.set_identificacion_del_beneficiario(portal_de_operadores_data.get("registro").get("identificacion"))
        time.sleep(2)
        portal_de_operadores.set_verificacion_de_codigo(codigo_OTP)
        time.sleep(2)
        portal_de_operadores.set_resumen_del_registro(portal_de_operadores_data.get("registro").get("resumen"))
        time.sleep(6)
        assert portal_de_operadores.verficar_beneficiario_registrado_correctamente()
        time.sleep(5)

        portal_de_operadores.agendar_cita(portal_de_operadores_data.get("gestion_de_citas"), codigo_OTP)
        time.sleep(5)
        portal_de_operadores.onClick_Cerrar()
        workflow.terminate()
