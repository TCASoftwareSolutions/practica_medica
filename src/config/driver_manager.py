"""
# Clase: DriverManager
# Descripción: Clase que inicializa el WebDriver según la configuración.
"""

import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.utilities.logger import setup_logger


class DriverManager:
    """Clase que inicializa el WebDriver según la configuración."""

    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"
    DRIVER_PATHS = {
        CHROME: "chromedriver.exe",
        FIREFOX: "geckodriver.exe",
        EDGE: "msedgedriver.exe",
    }

    logger_name = "driver_manager_logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"driver/driver_{logger_date}/driver_{logger_datetime}"

    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.logger_name, self.logger_dir)
        self.logger.info("Inicializando DriverManager")
        self.logger.info("Configuración del WebDriver: %s", self.config)

    def get_driver(self):
        """Inicializa el WebDriver según la configuración.

        Raises:
            ValueError: Navegador no soportado
            Exception: Error al inicializar el WebDriver

        Returns:
            _type_: _description_
        """
        browser = self.config.get("browser", self.CHROME).lower()
        headless = self.config.get("headless", False)
        use_remote = self.config.get("use_remote", False)
        remote_url = self.config.get("remote_url", "http://localhost:4444/wd/hub")

        try:
            if use_remote:
                return self.get_remote_driver(remote_url)
            elif browser == self.CHROME:
                return self._get_chrome_driver(headless)
            elif browser == self.FIREFOX:
                return self._get_firefox_driver(headless)
            elif browser == self.EDGE:
                return self._get_edge_driver(headless)
            else:
                raise ValueError(f"Navegador '{browser}' no está soportado.")
        except Exception as e:
            self.logger.error("Error al inicializar el WebDriver: %s", str(e))
            raise Exception("Error al inicializar el WebDriver")

    def get_remote_driver(self, remote_url):
        """Inicializa el WebDriver remoto según la configuración.

        Args:
            remote_url (str): URL del servidor remoto de Selenium Grid.

        Raises:
            ValueError: Navegador no soportado
            Exception: Error al inicializar el WebDriver remoto

        Returns:
            _type_: _description_
        """
        browser = self.config.get("browser", self.CHROME).lower()
        headless = self.config.get("headless", False)

        try:
            if browser == self.CHROME:
                options = self._get_chrome_options(headless)
                return webdriver.Remote(command_executor=remote_url, options=options)
            elif browser == self.FIREFOX:
                options = self._get_firefox_options(headless)
                return webdriver.Remote(command_executor=remote_url, options=options)
            elif browser == self.EDGE:
                options = self._get_edge_options(headless)
                return webdriver.Remote(command_executor=remote_url, options=options)
            else:
                raise ValueError(f"Navegador '{browser}' no está soportado.")
        except Exception as e:
            self.logger.error("Error al inicializar el WebDriver remoto: %s", str(e))
            raise Exception("Error al inicializar el WebDriver remoto")

    def _get_chrome_options(self, headless):
        options = ChromeOptions()
        if headless:
            options.add_argument("window-size=1920,1080")
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": self._get_download_path(),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
                "plugins.always_open_pdf_externally": True,
            },
        )
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options

    def _get_chrome_driver(self, headless) -> webdriver.Chrome:
        options = self._get_chrome_options(headless)
        # service = ChromeService(executable_path=self._get_driver_path(self.DRIVER_PATHS[self.CHROME]))
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def _get_chrome_driver_with_remote(self, remote_url, headless):
        options = self._get_chrome_options(headless)
        return webdriver.Remote(command_executor=remote_url, options=options)

    def _get_firefox_options(self, headless):
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.set_preference("browser.download.dir", self._get_download_path())
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        options.set_preference("pdfjs.disabled", True)
        return options

    def _get_firefox_driver(self, headless):
        options = self._get_firefox_options(headless)
        # service = FirefoxService(executable_path=self._get_driver_path(self.DRIVER_PATHS[self.FIREFOX]))
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    def _get_firefox_driver_with_remote(self, remote_url, headless):
        options = self._get_firefox_options(headless)
        return webdriver.Remote(command_executor=remote_url, options=options)

    def _get_edge_options(self, headless):
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options

    def _get_edge_driver(self, headless):
        options = self._get_edge_options(headless)
        # service = EdgeService(executable_path=self._get_driver_path(self.DRIVER_PATHS[self.EDGE]))
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

    def _get_edge_driver_with_remote(self, remote_url, headless):
        options = self._get_edge_options(headless)
        return webdriver.Remote(command_executor=remote_url, options=options)

    @staticmethod
    def _get_driver_path(driver_name):
        """
        Obtiene la ruta absoluta al controlador del navegador.
        :param driver_name: Nombre del controlador (chromedriver, geckodriver, etc.)
        :return: Ruta absoluta del controlador
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "../drivers", driver_name)

    @staticmethod
    def _get_download_path():
        """
        Obtiene la ruta absoluta al directorio de descargas.
        :return: Ruta absoluta del directorio de descargas
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        download_dir = os.path.join(base_dir, "../drivers/downloads")
        os.makedirs(download_dir, exist_ok=True)
        return os.path.realpath(download_dir)
