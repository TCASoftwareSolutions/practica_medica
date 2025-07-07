import pytest
from datetime import datetime
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.practica_medica.agenda_medica.workflow import AgendaMedicaWorkflow


@pytest.mark.e2e
@pytest.mark.mp_hos930
class TestAgendaMedica:
    """Conjunto de pruebas para el programa Portal de Operadores"""

    logger_name = "TestAgendaMedica_Logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"practica_medica/agenda_medica/agenda_medica_{logger_date}/agenda_medica_{logger_datetime}"
    screenshot_dir = f"practica_medica/agenda_medica/agenda_medica_{logger_date}/agenda_medica_{logger_datetime}"

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

    def test01_Open_Program_Medico(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de apertura del programa Agenda Medica como médico"""
        test_name = "Test01_Open_Program_Medico"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = AgendaMedicaWorkflow(ui_adapter, test_config)
        agenda_medica = workflow.execute_as_medico()
        agenda_medica.onClick_Cerrar()
        workflow.terminate()

    def test02_Open_Program_Supervisor(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de apertura del programa Agenda Medica como supervisor"""
        test_name = "Test02_Open_Program_Supervisor"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "002")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = AgendaMedicaWorkflow(ui_adapter, test_config)
        agenda_medica = workflow.execute_as_supervisor()
        agenda_medica.onClick_Cerrar()
        workflow.terminate()

    def test03_Atender_Cita(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de atención de cita en el programa Agenda Medica"""
        test_name = "Test03_Atender_Cita"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "003")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = AgendaMedicaWorkflow(ui_adapter, test_config)
        agenda_medica = workflow.execute_as_medico()
        agenda_medica.atender_cita()
        agenda_medica.onClick_Cerrar()
        workflow.terminate()
