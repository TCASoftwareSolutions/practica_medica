
# Proyecto de Testing Automatizado con Python y Selenium
Este proyecto tiene como objetivo automatizar pruebas para una aplicación web utilizando **Python** y **Selenium WebDriver**. La automatización de pruebas permite verificar el correcto funcionamiento de la aplicación de manera eficiente y repetitiva, reduciendo el esfuerzo manual y aumentando la cobertura de pruebas. El proyecto está estructurado siguiendo el patrón de diseño **Page Object Model (POM)**, lo que facilita el mantenimiento y escalabilidad del código. Además, se integra con herramientas como **Pytest** para la ejecución de pruebas y generación de reportes, y Azure Pipelines para la integración continua y despliegue.

## 📚 Estructura del Proyecto

```plaintext
practica_medica-automation-testing/     # Directorio raíz del proyecto de automatización de pruebas.
├── .azure-pipelines/                   # Contiene los archivos de configuración para la integración continua con Azure Pipelines.
├── reports/                            # Almacena los resultados generados por las pruebas, como reportes HTML, capturas de pantalla o logs.
│   ├── html/                           # Reportes HTML generados por herramienta pytest-html.
│   │   ├── report.html                 # Archivo principal que muestra los resultados de las pruebas en un formato fácil de leer.
│   ├── logs/                           # Archivos de registro generados durante la ejecución de las pruebas, útiles para depurar errores o problemas.
│   │   ├── test.log                    # Archivo de registro que contiene información detallada sobre la ejecución de las pruebas.
│   ├── screenshots/                    # Capturas de pantalla tomadas durante la ejecución de las pruebas, útiles para identificar problemas visuales o errores de interfaz.
│       ├── screenshot.png              # E.G
│   ├── xml/                            # Reportes XML generados por herramienta pytest.
│       ├── report.xml                  # Archivo de salida en formato XML que contiene los resultados de las pruebas en un formato compatible con herramientas de integración continua.
├── src/                                # Contiene el código fuente de la automatización de pruebas.
│   ├── adapter/                        # Contiene adaptadores para la automatización con Selenium, que implementan los metodos comunes para la interactuar con la UI.
│   ├── config/                         # Contiene archivos de configuración para el proyecto, como entornos, controladores de navegadores y parámetros globales.
│   │   ├── driver_manager.py           # Clase que gestiona la inicialización y cierre de los controladores de navegadores.
│   │   ├── environments.yaml           # Archivo de configuración que define los entornos de prueba, como URL base, credenciales de acceso o configuraciones específicas.
│   ├── data/                           # Almacena los datos de prueba utilizados en las pruebas, como credenciales de acceso, parámetros de configuración o datos de prueba.
│   │   ├──  default.yaml               # E.G
│   ├──  drivers/                       # Contiene los controladores de navegadores necesarios para ejecutar las pruebas, como ChromeDriver o GeckoDriver.
│   │   ├── chromedriver.exe            # E.G
│   │   ├── geckodriver.exe             # E.G
│   │   ├── downloads/                  # Carpeta donde se almacenan los archivos descargados automáticamente durante la ejecución de las pruebas, como reportes, archivos de datos o cualquier recurso generado por la aplicación bajo prueba.
│   ├── framework/                      # Contiene el núcleo del framework de automatización, incluyendo clases base, utilidades comunes, y componentes reutilizables que soportan la arquitectura general del proyecto.
│   │   ├──pages/                       # Contiene las clases que representan las páginas de la aplicación web bajo prueba, cada clase contiene los elementos y métodos asociados a esa página.
│   │   ├──ports/                       # Contiene las interfaces que deben implementar los adaptadores o servicios concretos del framework de automatización.
│   │   ├──utilities/                   # agrupa utilidades reutilizables que apoyan la automatización, pero que no forman parte directa de los tests ni de los page objects.
│   │   │   ├──logger.py                # Configuración de logs para registrar información detallada sobre la ejecución de las pruebas.
│   │   │   ├──configuration.py         # Ayuda a que la configuracion de una prueba sea reutilizable y facil de mantener.
│   ├──  tests/                         # Contiene los archivos de prueba escritos con pytest, cada archivo contiene una o más pruebas relacionadas con una funcionalidad específica.
│   │   ├── __init__.py                 # Archivo de inicialización para el directorio de pruebas.
│   │   ├── conftest.py                 # Archivo de configuración para pytest, que define fixtures globales y personalizados.
├── .azure-pipelines.yml                # Archivo de configuración para la integración continua con Azure Pipelines, que define los pasos de construcción, pruebas y despliegue del proyecto.
├── .gitignore                          # Archivo para especificar que archivos y directorios deben ser ignorados por GIT.
├── .pre-commit-config.yaml             # Arvhivo para configurar los hooks de pre-coomit
├── pyproject.toml                      # Archivo de configuracion para el proyecto. aqui se definen las dependencias y configuraciones del proyecto
├── README.md                           # Archivo de documentación que describe la estructura y contenido del proyecto de automatización de pruebas.
├── test-output.xml                     # Archivo de salida en formato XML que contiene los resultados de las pruebas en un formato compatible con herramientas de integración continua.```

## 🛠️ Instalación
1.  Clonar el repositorio
```sh
git clone https://github.com/TCASoftwareSolutions/practica_medica
cd practica_medica
```

2. Crear un entorno virtual
```sh
python -m venv .venv
source .venv/bin/activate               # En Linux/Mac
.\.venv\Scripts\activate                # En Windows
 ```

3. Instalar dependencias
```sh
pip install .
```

## 🚀 Uso del Proyecto
1. Configurar los valores en **src/config/environments.yaml**
```yaml
default:
    type_test: "e2e"
    browser: "chrome"
    headless: false
    use_remote: false
    remote_url: "http://localhost:4444/wd/hub"
    api_url: "http://localhost:8000"
    base_url: "http://localhost:8000"
    timeouts:
        implicit_wait: 15
        explicit_wait: 30
    reports:
        logs: "reports/logs"
        html: "reports/html"
        screenshots: "reports/screenshots"
        failures: "reports/screenshots/failure"
    credentials:
        usuario:
            username: "username"
            password: "password"
            company: "company"
            department: "department"
    environment: "default"
```

2. Ejecutar pruebas

Ejecutar todas las pruebas:
```sh
pytest
```

Ejecutar Pruebas especificas por clase:
```sh
pytest -v .\src\tests\e2e\login\test_login.py::TestLogin
```

Ejecutar Pruebas especificas por metodo:
```sh
pytest -v .\src\tests\e2e\login\test_login.py::TestLogin::test01_Login
```

Ejecutar pruebas específicas por custom marker
```sh
pytest -m auth
```

Generar un reporte HTML:
```sh
pytest --html=reports/html/report.html --self-contained-html
```

## 🧰 Herramientas Utilizadas
 - Lenguaje de programación: [ Python ]
 - Frameworks: [ Pytest ]
 - Librerías: [ Faker, Dateutil ]
 - Herramientas de desarrollo: [ Visual Studio Code ]
 - Control de versiones: [ Git ]
 - Servicios en la nube: [ Azure ]
 - Otros: [ Selenium, Webdriver_manager ]