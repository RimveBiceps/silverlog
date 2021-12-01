require 'watir'
require 'webdrivers'  # Import lib for chromedriver
require 'faker'

class TestRegister

    def initialize()
        # Use Random data via Faker gem
        # Read more about Faker gem here: https://github.com/stympy/faker#readme
        random_email = Faker::Internet.email
        random_name = Faker::Name.first_name
        random_password = Faker::Internet.password

        puts "Faker generated email: #{random_email}; name: #{random_name}; password: #{random_password}"
        puts "---------------------------"

        @random_email = random_email
        @random_name = random_name
        @random_password = random_password
    end

    def test_success_register()
        puts 'Test No. #3 Success register as user generated with faker lib.'
        browser = Watir::Browser.new :firefox

        browser.goto 'localhost:8000/register'

        browser.text_field(id: 'id_username').set @random_name
        browser.text_field(id: 'id_email').set @random_email
        browser.text_field(id: 'id_password1').set @random_password
        browser.text_field(id: 'id_password2').set @random_password

        browser.button(id: 'register').click
        is_logged = browser.div(class: 'alert alert-success mt-2').text == 'Registration successful.'

        puts is_logged ? 'Test verified.' : 'Test failed.'

        browser.close
    end

    def test_failed_register()
        puts 'Test No. #4 Failed register as existing user.'
        browser = Watir::Browser.new :firefox

        browser.goto 'localhost:8000/register'

        browser.text_field(id: 'id_username').set @random_name
        browser.text_field(id: 'id_email').set @random_email
        browser.text_field(id: 'id_password1').set @random_password
        browser.text_field(id: 'id_password2').set @random_password

        browser.button(id: 'register').click
        is_logged = browser.div(class: 'alert alert-danger mt-2').text == 'Unsuccessful registration. Invalid information.'

        puts is_logged ? 'Test verified.' : 'Test failed.'

        browser.close
    end

end
