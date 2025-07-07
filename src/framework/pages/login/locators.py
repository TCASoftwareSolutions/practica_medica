"""
# Clase: LoginLocators
# Descripción: Clase que contiene los localizadores de la página de login.
"""

from selenium.webdriver.common.by import By


class LoginLocators:
    """Clase para almacenar los localizadores de la página de login."""

    # Controles de la página de login
    txtUsername = (By.XPATH, "//input[contains(@id,'ctl00_usercontrol2_txt9001')]")
    txtPassword = (By.XPATH, "//input[contains(@id,'ctl00_usercontrol2_txt9004')]")
    cmbCompany = (By.XPATH, "//div[contains(@id,'ctl00_usercontrol2_ddlCompany')]")
    cmbDepartment = (By.XPATH, "//div[contains(@id,'ctl00_usercontrol2_ddlDepartamento')]")
    btnLogin = (By.XPATH, "//input[contains(@id,'ctl00_usercontrol2_T9500_Login_input')]")

    btnConfirmCredentialsAnotherUser = (By.XPATH, "//div[@class='ajs-primary ajs-buttons']//button[@class='ajs-button ajs-ok']")

    # Controles de la validación de credenciales'
    confirmCredentials = (By.XPATH, "//div[@class='alertify  ajs-movable ajs-pinnable ajs-fade']")
    txtUsernameConfirm = (By.XPATH, "//div[@class='alertify  ajs-movable ajs-pinnable ajs-fade']//input[contains(@id,'uvbUserName')]")
    txtPasswordConfirm = (By.XPATH, "//div[@class ='alertify  ajs-movable ajs-pinnable ajs-fade']//input[contains(@id,'uvbPassword')]")
    btnConfirmCredentials = (By.XPATH, "//div[@class='alertify  ajs-movable ajs-pinnable ajs-fade']//button[@class='ajs-button ajs-ok']")
    btnCancelarValidacionCredentials = (By.XPATH, "//div[@class='alertify  ajs-movable ajs-pinnable ajs-fade']//button[@class='ajs-button ajs-cancel']")
