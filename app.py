
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

# 1 - Entrar no Site
driver = webdriver.Chrome()
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

# 2 - Clicar no Email e digitar o email
email = driver.find_element(By.XPATH, "//input[@id='email']")
sleep(2)
email.send_keys('admin@contabilidade.com')

# 3 - Clicar na Senha e digitar a senha
senha = driver.find_element(By.XPATH, "//input[@id='senha']")
sleep(2)
senha.send_keys('admin0908')

# 4 - Clicar em entrar
entrar = driver.find_element(By.XPATH, "//button[@id='Entrar']")
sleep(2)
entrar.click()
sleep(5)

# 5 - Clicar em cada campo e completar as opções da planilha
empresas = openpyxl.load_workbook('empresas.xlsx')
page_empresas = empresas['dados empresas']

for linha in page_empresas.iter_rows(min_row=2, values_only=True):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_funcionario, data_fundacao = linha

    driver.find_element(By.ID, "nomeEmpresa").send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID, "emailEmpresa").send_keys(email)
    sleep(1)
    driver.find_element(By.ID, "telefoneEmpresa").send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID, "enderecoEmpresa").send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID, "cnpj").send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID, "areaAtuacao").send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID, "numeroFuncionarios").send_keys(quantidade_funcionario)
    sleep(1)
    driver.find_element(By.ID, "dataFundacao").send_keys(data_fundacao)
    sleep(1)
    driver.find_element(By.XPATH, "//button[@id='Cadastrar']").click()
    sleep(3)

