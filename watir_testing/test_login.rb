require 'watir'
require 'webdrivers'  # Import lib for chromedriver

class TestLogin

    def test_success_login()
        # Initialize the Browser
        # If browser not specified Chrome is the default. To specify browser (firefox, internet_explorer, edge, safari)
        puts 'Test No. #1 Success login as admin.'
        browser = Watir::Browser.new :firefox

        # Navigate to Page
        browser.goto 'localhost:8000/login'

        # Fill out Text Field Names
        browser.text_field(id: 'id_username').set 'admin'
        browser.text_field(id: 'id_password').set 'admin'

        # Click Button:
        browser.button(id: 'login').click
        is_logged = browser.div(class: ['alert', 'alert-success', 'mt-2']).text == 'You are now logged in as admin.' # => true

        puts is_logged ? 'Test verified.' : 'Test failed.'

        browser.close
    end

    def test_failed_login()
        puts 'Test No. #2 Failed login as not existing user (space).'
        browser = Watir::Browser.new :firefox

        browser.goto 'localhost:8000/login'

        browser.text_field(id: 'id_username').set ' '
        browser.text_field(id: 'id_password').set ' '

        browser.button(id: 'login').click
        is_logged = browser.div(class: ['alert', 'alert-danger', 'mt-2']).text == 'Invalid username or password.' # => true

        puts is_logged ? 'Test verified.' : 'Test failed.'

        browser.close
    end

end
