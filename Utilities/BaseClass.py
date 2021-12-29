import inspect

import pytest
import logging

from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class Baseclass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("C:\\Users\\hemank\\PycharmProjects\\pythonProject1\\Reports\\loging.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def selectByVisibleText(self, locator, text):
        s = Select(locator)
        s.select_by_visible_text(text)
