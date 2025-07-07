"""
# Clase: NavegacionLocators
# Descripción: Clase para almacenar los localizadores de la página de navegación.
"""

from selenium.webdriver.common.by import By


class NavegacionLocators:
    """Localizadores de la página de navegación."""

    app_loading = (By.XPATH, "//div[@id='loading-zone']")
    app_system_date = (By.XPATH, "//span[@id='MasterPage_SystemDate']")
    app_uuid = (By.XPATH, "//span[@id='MasterPage_LogFileId']")

    btnSearch = (By.CSS_SELECTOR, ".icon-search")
    txtSearch = (By.XPATH, "//input[contains(@id,'sbxSearch_Input')]")

    btnImageProfile = (By.XPATH, "//div[@id='Header_UserName']//span[contains(@id,'MasterPage_Profile_UserName_Initials')]")
    btnLogout = (By.XPATH, "//div[@onclick='GoLogOut()']/ancestor::li[contains(@class,'rmItem')]")
    btnConfirmar = (By.XPATH, "//div[@class='alertify  ajs-movable ajs-closable ajs-pinnable ajs-zoom']//button[contains(@class,'ajs-button ajs-ok')]")

    btnLogoutSuccess = (By.XPATH, "//input[contains(@id,'btnGotoLogin_input')]")
    lblLogoutSuccess = (By.XPATH, "//div[@class='infoTopText']")

    divHeader = (By.XPATH, "//div[@id='HeaderPanel']")
    divMenu = (By.XPATH, "//div[@class='menu-fixer']//div[@id='Menu']")
    divModulos = (By.XPATH, "//div[@class='welcome-modules']")
