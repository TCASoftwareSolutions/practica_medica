import time
import pytest
from datetime import datetime
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.practica_medica.agenda_medica.workflow import AgendaMedicaWorkflow


@pytest.mark.load
@pytest.mark.mp_hos930
class TestAgendaMedica:
    """Conjunto de pruebas para el programa Portal de Operadores"""

    logger_name = "TestAgendaMedica_Logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"load/practica_medica/agenda_medica/agenda_medica_{logger_date}/agenda_medica_{logger_datetime}"
    screenshot_dir = f"load/practica_medica/agenda_medica/agenda_medica_{logger_date}/agenda_medica_{logger_datetime}"

    def setup_test(self, test_name: str, session_id: str = None):
        """Configura el test con el nombre del test y el directorio de capturas de pantalla y logs

        Args:
            test_name (str): Nombre del test
        """
        self.logger_name = f"{session_id}::{self.logger_name}::{test_name}"
        self.logger_dir = f"{self.logger_dir}/{session_id}-{test_name}"
        self.screenshot_dir = f"{self.screenshot_dir}/{session_id}-{test_name}"

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

    @pytest.mark.slow
    def test01_Open_Program(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de apertura del programa Agenda Medica"""
        test_name = "Test01_Open_Program"
        self.setup_test(test_name, ui_adapter.driver.session_id)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = AgendaMedicaWorkflow(ui_adapter, test_config)
        agenda_medica = workflow.execute_as_medico()
        time.sleep(60 * 10)  # Simula un tiempo de espera largo para la prueba
        agenda_medica.onClick_Cerrar()
        workflow.terminate()
