import pytest
import yaml
import os
from adapter.selenium.selenium_adapter import SeleniumAdapter
from config.driver_manager import DriverManager
from datetime import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/environments.yaml")
DEFAULT_SCREENSHOTS_DIR = "reports/screenshots/failure"


def load_config(env):
    """Carga la configuración de la prueba desde un archivo YAML.

    Args:
        env (str): El ambiente de la prueba (qa, dev, prod).

    Returns:
        dict: Diccionario con la configuración de la prueba.
    """
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f).get(env, {})


@pytest.fixture(scope="session")
def config(pytestconfig):
    """Fixture de Pytest para cargar la configuración de la prueba.

    Args:
        pytestconfig: Configuración de pytest.

    Returns:
        dict: Diccionario con la configuración de la prueba.
    """
    env = pytestconfig.getoption("env")
    return load_config(env)


@pytest.fixture(scope="session")
def driver(config):
    """Fixture de Pytest para inicializar el WebDriver."""
    driver_manager = DriverManager(config)
    type_test = config.get("type_test")
    if type_test not in ("e2e", "load"):
        pytest.fail(f"Tipo de prueba no soportado: {type_test}")

    driver = driver_manager.get_driver()
    if not driver:
        pytest.fail("No se pudo inicializar el WebDriver.")

    driver.implicitly_wait(config.get("timeouts", {}).get("implicit_wait", 20))
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope="session")
def ui_adapter(driver, config):
    """Fixture de Pytest para inicializar el adaptador de la interfaz de usuario.

    Args:
        driver (_type_): WebDriver.
        config (_type_): Configuración de la prueba.

    Returns:
        _type_: Adaptador de la interfaz de usuario.
    """
    return SeleniumAdapter(driver, config)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Hook de pytest para configurar las opciones de reporte HTML y JUnit XML.

    Args:
        config (_type_): Configuración de pytest.
    """
    datenow = datetime.now().date()
    timestamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    html_report = f"reports/html/{datenow}/report_{timestamp}.html"
    junit_report = f"reports/xml/junit/{datenow}/report_{timestamp}.xml"
    # nunit_report = f"reports/xml/nunit/{datenow}/report_{timestamp}.xml"

    # Añadir las opciones de reporte HTML y JUnit XML dinámicamente
    config.option.htmlpath = html_report
    config.option.self_contained_html = True

    config.option.xmlpath = junit_report
    config.option.junit_family = "junit4"
    config.option.junit_logging = "all"
    config.option.junit_log_passing_tests = True
    config.option.junit_log_skipped_tests = True
    config.option.junit_log_deselected_tests = True
    config.option.junit_log_failed_tests = True
    config.option.junit_log_error_tests = True
    config.option.junit_log_crashed_tests = True
    config.option.junit_log_inactive_tests = True


def pytest_collection_modifyitems(config, items):
    """Hook de pytest para modificar los items de las pruebas.
    Args:
        config (_type_): Configuración de pytest.
        items (_type_): Items de las pruebas.
    """
    for item in items:
        for marker in item.iter_markers(name="test_plan_id"):
            test_plan_id = marker.args[0]
            item.user_properties.append(("test_plan_id", test_plan_id))

        for marker in item.iter_markers(name="test_suite_id"):
            test_suite_id = marker.args[0]
            item.user_properties.append(("test_suite_id", test_suite_id))

        for marker in item.iter_markers(name="test_case_id"):
            test_case_id = marker.args[0]
            item.user_properties.append(("test_case_id", test_case_id))

        for marker in item.iter_markers(name="test_name"):
            test_name = marker.args[0]
            item.user_properties.append(("test_name", test_name))


def pytest_html_report_title(report):
    """Hook de pytest-html para establecer el título del reporte HTML.

    Args:
        report (_type_): Reporte de pytest.
    """
    report.title = "Pytest HTML Report"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook de pytest para capturar el estado de las pruebas y ejecutar acciones en caso de fallo.

    Args:
        item (_type_): Item de la prueba.
        call (_type_): Llamada a la prueba.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Hook de pytest para generar un resumen al final de la ejecución de las pruebas.
    Args:
        terminalreporter (_type_): Reportero de terminal de pytest.
        exitstatus (int): Estado de salida de pytest.
        config (_type_): Configuración de pytest.
    """
    reports = []
    for replist in terminalreporter.stats.values():
        for rep in replist:
            if hasattr(rep, "duration"):
                reports.append(rep)

    if not reports:
        return

    # Ordenar los reportes por duración
    # (mayor a menor duración)
    reports.sort(key=lambda x: x.duration)
    reports.reverse()

    # Escribir el resumen de duración
    terminalreporter.write_sep("=", "Duración de las pruebas:")
    for rep in reports:
        # Filtrar solo los reportes de tipo 'call'
        # (es decir, las pruebas que se ejecutaron)
        if rep.when != "call":
            continue
        nodeid = rep.nodeid.replace("::()::", "::")
        terminalreporter.write_line("%02.2fs %s" % (rep.duration, nodeid))
    # Escribir la duración total
    # terminalreporter.write_sep("=", "Total duration: %02.2fs" % sum(rep.duration for rep in reports))


@pytest.fixture(scope="function", autouse=True)
def capture_screenshot_on_failure(request, driver, config):
    """Fixture de Pytest para capturar una captura de pantalla en caso de fallo.

    Args:
        request (_type_): Request de la prueba.
        driver (_type_): WebDriver.
        config (_type_): Configuración de la prueba.
    """
    yield
    if request.node.rep_call.failed:
        # Obtener la ruta para guardar las capturas de pantalla
        failed_date = datetime.now().date()
        failed_time = datetime.now().strftime("%Y-%m-%d %H.%M.%S")

        screenshots_dir = f"{config.get('reports', {}).get('failures', DEFAULT_SCREENSHOTS_DIR)}/{failed_date}/{failed_time}"
        os.makedirs(screenshots_dir, exist_ok=True)

        # Generar el nombre del archivo de la captura
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

        # Guardar la captura de pantalla
        try:
            driver.save_screenshot(screenshot_path)
            print(f"Captura de pantalla guardada: {screenshot_path}")
        except Exception as e:
            print(f"Error al guardar la captura de pantalla: {e}")


def pytest_addoption(parser):
    """Hook de pytest para añadir opciones de línea de comandos.

    Args:
        parser: Parser de pytest.
    """
    parser.addoption("--env", action="store", default="default", help="Enviroment")
