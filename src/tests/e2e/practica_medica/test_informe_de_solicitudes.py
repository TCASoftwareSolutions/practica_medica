import pytest
from datetime import datetime
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.practica_medica.informe_de_solicitudes.workflow import InformeDeSolicitudesWorkflow


@pytest.mark.e2e
@pytest.mark.mp_informesolicitudes
class TestInformeDeSolicitudes:
    """Conjunto de pruebas para el programa Portal de Operadores"""

    logger_name = "TestInformeDeSolicitudes_Logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"practica_medica/informe_de_solicitudes/informe_de_solicitudes_{logger_date}/informe_de_solicitudes_{logger_datetime}"
    screenshot_dir = f"practica_medica/informe_de_solicitudes/informe_de_solicitudes_{logger_date}/informe_de_solicitudes_{logger_datetime}"

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

    def test_01_Open_Program(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de apertura del programa Agenda Medica"""
        test_name = "Test01_Open_Program"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "001", "001")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = InformeDeSolicitudesWorkflow(ui_adapter, test_config)
        informe_de_solicitudes = workflow.execute()
        informe_de_solicitudes.onClick_Cerrar()
        workflow.terminate()

    def test_02_Mostrar_medicamentos(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de mostrar medicamentos en el informe de solicitudes"""
        test_name = "Test02_Mostrar_medicamentos"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "002", "002")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = InformeDeSolicitudesWorkflow(ui_adapter, test_config)
        informe_de_solicitudes = workflow.execute()
        informe_de_solicitudes_data = informe_de_solicitudes.data.get("read", {})
        informe_de_solicitudes.set_tipo_de_informe("Medicamentos")
        informe_de_solicitudes.set_tipo_de_documento("DUI")
        informe_de_solicitudes.set_clave_de_documento(informe_de_solicitudes_data.get("dui", {}).get("clave_de_documento", ""))
        informe_de_solicitudes.onClick_Filtrar()
        assert informe_de_solicitudes.is_medicamentos_visible(), "Los medicamentos no están visibles en el informe de solicitudes"
        informe_de_solicitudes.onClick_Cerrar()
        workflow.terminate()

    def test_03_Mostrar_laboratorio(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de mostrar laboratorio en el informe de solicitudes"""
        test_name = "Test03_Mostrar_laboratorio"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "003", "003")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = InformeDeSolicitudesWorkflow(ui_adapter, test_config)
        informe_de_solicitudes = workflow.execute()
        informe_de_solicitudes_data = informe_de_solicitudes.data.get("read", {})
        informe_de_solicitudes.set_tipo_de_informe("Laboratorio")
        informe_de_solicitudes.set_tipo_de_documento("DUI")
        informe_de_solicitudes.set_clave_de_documento(informe_de_solicitudes_data.get("dui", {}).get("clave_de_documento", ""))
        informe_de_solicitudes.onClick_Filtrar()
        assert informe_de_solicitudes.is_laboratorio_visible(), "El laboratorio no está visible en el informe de solicitudes"
        informe_de_solicitudes.onClick_Cerrar()
        workflow.terminate()

    def test_04_Mostrar_imagenes(self, ui_adapter: UIPort, record_pipelines_property):
        """Prueba de mostrar imágenes en el informe de solicitudes"""
        test_name = "Test04_Mostrar_imagenes"
        self.setup_test(test_name)
        self.record_properties(record_pipelines_property, test_name, "004", "004")
        test_config = Configuration(config=ui_adapter.config, screenshot_dir=self.screenshot_dir, logger_name=self.logger_name, logger_dir=self.logger_dir, test_name=test_name)

        workflow = InformeDeSolicitudesWorkflow(ui_adapter, test_config)
        informe_de_solicitudes = workflow.execute()
        informe_de_solicitudes_data = informe_de_solicitudes.data.get("read", {})
        informe_de_solicitudes.set_tipo_de_informe("Imagenología")
        informe_de_solicitudes.set_tipo_de_documento("DUI")
        informe_de_solicitudes.set_clave_de_documento(informe_de_solicitudes_data.get("dui", {}).get("clave_de_documento", ""))
        informe_de_solicitudes.onClick_Filtrar()
        assert informe_de_solicitudes.is_imagenes_visible(), "Las imágenes no están visibles en el informe de solicitudes"
        informe_de_solicitudes.onClick_Cerrar()
        workflow.terminate()
