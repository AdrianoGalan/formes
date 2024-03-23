from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://forms.office.com/Pages/ResponsePage.aspx?id=2vWDhPF1aEyKmmTbGHFWmcshb5HoZL5DoYrHfV7kyXVUQ1I0RTJDMDhQRjZXVFBCMzJEVTcwSUVZSi4u&qrcode=true")

    # Encontre todos os elementos que possuem o atributo 'data-automation-value'
    elements_with_data_value = page.query_selector_all('[data-automation-value]')

    # Lista para armazenar os valores dos atributos 'data-automation-value'
    data_values = []

    # Iterar sobre os elementos e obter o valor do atributo 'data-automation-value'
    for element in elements_with_data_value:
        data_value = element.get_attribute('data-automation-value')
        data_values.append(data_value)

    print(data_values)

    browser.close()


