import pytest
import time
from datetime import datetime
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.menu_operadores.portal_de_operadores.workflow import PortalDeOperadoresWorkflow


@pytest.mark.pm_callcenter
class TestPortalDeOperadores:
    """Conjunto de pruebas para el programa Portal de Operadores"""

    logger_name = "TestPortalDeOperadores_Logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"menu_operadores/portal_de_operadores/portal_de_operadores_{logger_date}/portal_de_operadores_{logger_datetime}"
    screenshot_dir = f"menu_operadores/portal_de_operadores/portal_de_operadores_{logger_date}/portal_de_operadores_{logger_datetime}"

    def setup_test(self, test_name: str):
        """Configura el test con el nombre del test y el directorio de capturas de pantalla y logs

        Args:
            test_name (str): Nombre del test
        """
        self.logger_name = f"{self.logger_name}::{test_name}"
        self.logger_dir = f"{self.logger_dir}/{test_name}"
        self.screenshot_dir = f"{self.screenshot_dir}/{test_name}"

    def record_properties(self, record_pipelines_property, test_name, test_suite_id, test_case_id):
        """Registra las propiedades del test en el reporte de Azure DevOps

        Args:
            record_pipelines_property (fixture): Fixture para registrar propiedades en el reporte de Azure DevOps
            test_name (str): Nombre del test
            test_suite_id (str): ID de la suite de pruebas
            test_case_id (str): ID del caso de prueba
        """
        record_pipelines_property("test_name", f"{test_name} pipeline")
        record_pipelines_property("test_suite_id", test_suite_id)
        record_pipelines_property("test_case_id", test_case_id)

    def test01_Open_Program(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de apertura del programa Portal de Operadores"""
        test_name = "Test01_Open_Program"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores.onClick_Cerrar()
        workflow.terminate()

    def test02_Registro_de_beneficiario(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de registro de un beneficiario"""
        test_name = "test02_Registro_de_beneficiario"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores_data = portal_de_operadores.data.get("create").get("registro")
        portal_de_operadores.set_identificacion_del_beneficiario(portal_de_operadores_data.get("identificacion"))
        codigo_OTP = portal_de_operadores.data.get("codigo_OTP")
        time.sleep(2)
        portal_de_operadores.set_verificacion_de_codigo(codigo_OTP)
        time.sleep(2)
        portal_de_operadores.set_resumen_del_registro(portal_de_operadores_data.get("resumen"))
        time.sleep(6)
        assert portal_de_operadores.verficar_beneficiario_registrado_correctamente()
        time.sleep(5)
        portal_de_operadores.onClick_Cerrar()
        time.sleep(2)
        workflow.terminate()

    def test03_Agendar_Cita(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de programacion de una cita médica"""
        test_name = "test03_Agendar_Cita"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores_data = portal_de_operadores.data.get("create")
        codigo_OTP = portal_de_operadores.data.get("codigo_OTP")
        portal_de_operadores.agendar_cita(portal_de_operadores_data.get("gestion_de_citas"), codigo_OTP)
        time.sleep(5)
        portal_de_operadores.onClick_Cerrar()
        workflow.terminate()

    def test04_Reprogramar_Cita(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de reprogramacion de una cita médica"""
        test_name = "test04_Reprogramar_Cita"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores_data = portal_de_operadores.data.get("update")
        codigo_OTP = portal_de_operadores.data.get("codigo_OTP")
        portal_de_operadores.reprogramar_cita(portal_de_operadores_data.get("gestion_de_citas"), codigo_OTP, portal_de_operadores.numero_de_cita)
        time.sleep(5)
        portal_de_operadores.onClick_Cerrar()
        workflow.terminate()

    def test05_Cancelar_Cita(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de cancelacion de una cita médica"""
        test_name = "test05_Cancelar_Cita"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = PortalDeOperadoresWorkflow(ui_adapter, test_config)
        portal_de_operadores = workflow.execute()
        portal_de_operadores_data = portal_de_operadores.data.get("delete")
        codigo_OTP = portal_de_operadores.data.get("codigo_OTP")
        portal_de_operadores.cancelar_cita(portal_de_operadores_data.get("gestion_de_citas"), codigo_OTP)
        time.sleep(5)
        portal_de_operadores.onClick_Cerrar()
        workflow.terminate()
