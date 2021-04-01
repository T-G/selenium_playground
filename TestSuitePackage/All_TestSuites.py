import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest
from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Master Test Suite - all tests cases falls under master test suite. LoginTest, SignUpTest, PaymentTest, PaymentReturnsTest
# Sanity Test Suite - LoginTest, SignUpTest
# Functional Test Suite - PaymentTest, PaymentReturnsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test Suites
sanity_test_suite = unittest.TestSuite([tc1, tc2])
functional_test_suite = unittest.TestSuite([tc3, tc4])
master_test_suite = unittest.TestSuite([tc1, tc2, tc3, tc4])
#unittest.TextTestRunner().run(sanity_test_suite)
#unittest.TextTestRunner().run(functional_test_suite)
unittest.TextTestRunner(verbosity=2).run(master_test_suite)
