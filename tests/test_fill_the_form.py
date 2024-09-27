import os
from selene import browser, have


def test_fill_the_form():

    browser.open('/')

    browser.element('#firstName').type('Madam')
    browser.element('#lastName').type('Enot')
    browser.element('#userEmail').type('123@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="5"]').click()
    browser.element('.react-datepicker__year-select option[value="1994"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--004').click()
    browser.element('#subjectsInput').type('Ma').press_enter().type('Bi').press_enter()
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('bichon.jpg'))
    browser.element('#currentAddress').type('Tyumen, Respublic street, 100')
    browser.element('#react-select-3-input').type('U').press_enter()
    browser.element('#react-select-4-input').type('Agr').press_enter()
    browser.element('.btn.btn-primary').click()

    browser.all('tbody').should(
        have.texts(
            'Student Name Madam Enot'
            '\nStudent Email 123@mail.ru'
            '\nGender Female'
            '\nMobile 1234567890'
            '\nDate of Birth 04 June,1994'
            '\nSubjects Maths, Biology'
            '\nHobbies Music'
            '\nPicture bichon.jpg'
            '\nAddress Tyumen, Respublic street, 100'
            '\nState and City Uttar Pradesh Agra'
        )
    )
