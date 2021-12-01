require_relative "test_login"
require_relative "test_register"

# TO run tests: ruby run_tests.rb

test_login = TestLogin.new
test_register = TestRegister.new

test_login.test_success_login()
test_login.test_failed_login()

test_register.test_success_register()
test_register.test_failed_register()
