# https://www.codegrepper.com/code-examples/typescript/session+not+created%3A+This+version+of+ChromeDriver+only+supports+Chrome+version+85

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())