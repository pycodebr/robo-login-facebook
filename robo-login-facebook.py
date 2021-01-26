from selenium import webdriver


# Manter o chromedriver.exe atualizado conforme a versão do seu Google chrome #
# https://chromedriver.chromium.org/downloads #
browser = webdriver.Chrome(r'.\chromedriver.exe')


browser.get('https://www.facebook.com/')

# Digita o email #
browser.find_element_by_id('email').send_keys('***EMAIL***')

# Digita a senha #
browser.find_element_by_id('pass').send_keys('***SENHA***')

# Clica em Entrar #
browser.find_element_by_name('login').click()