import time
import pytest
from datetime import datetime
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.practica_medica.agenda_medica.workflow import AgendaMedicaWorkflow
from framework.pages.tablero_medico.workflow import TableroMedicoWorkflow


@pytest.mark.e2e
@pytest.mark.mp_tableromedico
class TestTableroMedico:
    """Conjunto de pruebas para el programa tablero medico"""

    logger_name = "TestTableroMedico_Logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"tablero_medico/tablero_medico_{logger_date}/tablero_medico_{logger_datetime}"
    screenshot_dir = f"tablero_medico/tablero_medico_{logger_date}/tablero_medico_{logger_datetime}"

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
        if not agenda_medica.check_nueva_cita_asignada():
            citas_programadas = agenda_medica.lista_de_citas_programadas()
            test_config.logger.info(f"Citas programadas: {citas_programadas}")
            if citas_programadas:
                agenda_medica.open_cita(citas_programadas[0])
            else:
                pytest.skip("No hay citas programadas para el médico.")
        time.sleep(5)  # Esperar a que se abra el formulario de cita

        workflow_tablero = TableroMedicoWorkflow(ui_adapter, test_config)
        tablero_medico = workflow_tablero.execute()
        tablero_medico.onClick_Nota_Medica()
        tablero_medico.set_consultar_por("data")
        tablero_medico.set_triage("1")
        tablero_medico.setup_signos_vitales({"temperatura": "36.5", "frecuencia_cardiaca": "72", "frecuencia_respiratoria": "16", "presion_arterial": "120/80", "saturacion_oxigeno": "98", "peso": "70", "talla": "1.75"})
        tablero_medico.set_presente_enfermedad("Diabetes")
        tablero_medico.set_apreciacion_diagnostica("Paciente estable, continuar con el tratamiento actual.")

        tablero_medico.set_diag_principal("Diabetes mellitus tipo 2")

        tablero_medico.onClick_generar_diagnostico_principal()

        tablero_medico.onClick_Agregar_problema_activo()
        tablero_medico.set_diagnostico_secundario("Hipertensión")
        tablero_medico.onClick_Agregar_diagnostico_secundario()
        tablero_medico.onClick_Finalizar_cita()

        workflow.terminate()
