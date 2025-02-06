import allure
import time
import os
from selene import be, have, browser, command
from selene.support.shared.jquery_style import s
from utils import attach


def test_registration_form(open_browser):
    first_name = "Sonic"
    last_name = "Syndicate"

    with allure.step('Открыть форму регистрации'):
        browser.open('https://demoqa.com/automation-practice-form')

        browser.execute_script("document.querySelectorAll('iframe').forEach(e => e.remove());")
        browser.execute_script("document.querySelectorAll('.ads, .ad-container, #fixedban, footer').forEach(e => e.remove());")
        # time.sleep(1)
        browser.execute_script("document.querySelectorAll('iframe[id^=\"google_ads_iframe\"]').forEach(e => e.remove());")

        attach.add_screenshot(browser)
        attach.add_html(browser)

    with allure.step('Заполнить ФИО'):
        s('#firstName').type(first_name)
        s('#lastName').type(last_name)
        attach.add_screenshot(browser)

    with allure.step('Заполнить поле ввода e-mail'):
        s('#userEmail').type('test@mail.ru')
        attach.add_screenshot(browser)

    with allure.step('Выбрать пол'):
        s('[for="gender-radio-1"]').perform(command.js.scroll_into_view).should(be.clickable).click()
        attach.add_screenshot(browser)

    with allure.step('Заполнить поле ввода телефон'):
        s('#userNumber').type('9939993388')
        attach.add_screenshot(browser)

    with allure.step('Установить дату рождения'):
        birth_input = s('#dateOfBirthInput')
        birth_input.perform(command.js.scroll_into_view).should(be.clickable).click()

        s('.react-datepicker__month-select').click().s('[value="2"]').click()
        s('.react-datepicker__year-select').click().s('[value="1960"]').click()
        s('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click()
        attach.add_screenshot(browser)

    with allure.step('Выбрать предмет'):
        s('#subjectsInput').type('Maths').press_enter()
        attach.add_screenshot(browser)

    with allure.step('Выбрать хобби'):
        s('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).should(be.clickable).click()
        s('[for="hobbies-checkbox-3"]').should(be.clickable).click()
        attach.add_screenshot(browser)

    with allure.step('Загрузить файл'):
        file_path = os.path.abspath("tests/resources/pic.png")
        s('#uploadPicture').send_keys(file_path)
        attach.add_screenshot(browser)

    with allure.step('Заполнить поле ввода "адрес"'):
        s('#currentAddress').type('Moscow 5')
        attach.add_screenshot(browser)

    with allure.step('Выбрать штат'):
        state_element = s('#state')
        state_element.perform(command.js.scroll_into_view).should(be.visible)

        try:
            state_element.click()
        except:
            browser.execute_script("arguments[0].click();", state_element.get_actual_webelement())

        s('#react-select-3-option-0').should(be.visible).click()
        attach.add_screenshot(browser)

    with allure.step('Выбрать город'):
        city_element = s('#city')
        city_element.should(be.visible)

        try:
            city_element.click()
        except:
            browser.execute_script("arguments[0].click();", city_element.get_actual_webelement())

        s('#react-select-4-option-0').should(be.visible).click()
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