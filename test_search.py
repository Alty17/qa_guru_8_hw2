from selene import browser, have, be
def test_search_ok(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
def test_search_not_ok(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('dfgdhgdjfhjdhfshgdshghsdfguisdhgsid').press_enter()
    assert browser.element('#extabar #result-stats').should(have.text('Результатов: примерно 0')), "Text is not found"
