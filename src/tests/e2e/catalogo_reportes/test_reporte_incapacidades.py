from datetime import datetime
import pytest
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.catalogo_reportes.reporte_incapacidades.workflow import ReporteDeIncapacidadesWorkflow


@pytest.mark.e2e
@pytest.mark.mp_tableromedico
class TestReporteDeIncapacidades:
    """Conjunto de pruebas para el programa reporte de incapacidades"""

    logger_name = "TestReporteDeIncapacidades_Logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"reporte_incapacidades/reporte_incapacidades{logger_date}/reporte_incapacidades{logger_datetime}"
    screenshot_dir = f"reporte_incapacidades/reporte_incapacidades{logger_date}/reporte_incapacidades{logger_datetime}"

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

    def test01_Open_Reporte_Incapacidades(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de apertura del programa Reporte de incapacidades como médico"""
        test_name = "test01_Open_Reporte_Incapacidades"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = ReporteDeIncapacidadesWorkflow(ui_adapter, test_config)
        reporte_incapacidades = workflow.execute()

        reporte_incapacidades.onClick_Modificar_Parametros()
        rows_ini = reporte_incapacidades.get_Total_Rows()
        reporte_incapacidades.set_Campos_Fecha("2024/07/10", "2025/07/10")
        reporte_incapacidades.onClick_Actualizar()
        rows_fin = reporte_incapacidades.get_Total_Rows()
        reporte_incapacidades.compare_Total_Rows(rows_ini, rows_fin)

        workflow.terminate()
