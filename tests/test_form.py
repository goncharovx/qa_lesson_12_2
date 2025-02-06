import os
import allure
from selene import have, be
from selene.api import s
from utils import attach

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'resources', 'pic.png')

def test_registration_form(open_browser):
    browser = open_browser

    first_name = "Sonic"
    last_name = "Syndicate"

    with allure.step('Открыть форму регистрации'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.execute_script("$('footer').remove()")
        browser.execute_script("$('#fixedban').remove()")
        browser.execute_script("document.querySelectorAll('iframe').forEach(iframe => iframe.remove())")
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)

    with allure.step('Заполнить ФИО'):
        s('#firstName').type(first_name)
        s('#lastName').type(last_name)
        attach.add_screenshot(browser)

    with allure.step('Заполнить поле ввода e-mail'):
        s('#userEmail').type('test@mail.ru')
        attach.add_screenshot(browser)

    with allure.step('Выбрать пол'):
        s('[for="gender-radio-1"]').click()
        attach.add_screenshot(browser)

    with allure.step('Заполнить поле ввода телефон'):
        s('#userNumber').type('9939993388')
        attach.add_screenshot(browser)

    with allure.step('Установить дату рождения'):
        s('#dateOfBirthInput').should(be.clickable).click()
        s('.react-datepicker__month-select').click().s('[value="2"]').click()
        s('.react-datepicker__year-select').click().s('[value="1960"]').click()
        s('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click()
        attach.add_screenshot(browser)

    with allure.step('Выбрать предмет'):
        s('#subjectsInput').type('Maths').press_enter()
        attach.add_screenshot(browser)

    with allure.step('Выбрать хобби'):
        s('[for="hobbies-checkbox-1"]').click()
        s('[for="hobbies-checkbox-3"]').click()
        attach.add_screenshot(browser)

    with allure.step('Загрузить файл'):
        s('#uploadPicture').send_keys(file_path)
        attach.add_screenshot(browser)

    with allure.step('Заполнить поле ввода "адрес"'):
        s('#currentAddress').type('Moscow 5')
        attach.add_screenshot(browser)

    with allure.step('Выбрать штат'):
        s('#state').click().s('#react-select-3-option-0').click()
        attach.add_screenshot(browser)

    with allure.step('Выбрать город'):
        s('#city').click().s('#react-select-4-option-0').click()
        attach.add_screenshot(browser)

    with allure.step('Подтвердить регистрацию'):
        s('#submit').click()
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)

    with allure.step('Проверить форму регистрации'):
        s('.table-responsive').should(have.text(first_name + ' ' + last_name))
        s('.table-responsive').should(have.text('test@mail.ru'))
        s('.table-responsive').should(have.text('Male'))
        s('.table-responsive').should(have.text('9939993388'))
        s('.table-responsive').should(have.text('03 March,1960'))
        s('.table-responsive').should(have.text('Maths'))
        s('.table-responsive').should(have.text('Sports'))
        s('.table-responsive').should(have.text('Music'))
        s('.table-responsive').should(have.text('pic.png'))
        s('.table-responsive').should(have.text('Moscow 5'))
        s('.table-responsive').should(have.text('NCR Delhi'))
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)