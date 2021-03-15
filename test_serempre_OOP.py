#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:53:22 2021

@author: Katherin Pérez Ceballos
"""
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pyunitreport import HTMLTestRunner
import time

# Run typing: python3 -m unittest discover
# Run typing: python3 test_serempre_OOP.py
# Run typing: ./test_serempre_OOP.py
class TestSerempre(unittest.TestCase):

    def setUp(self):
        url = 'https://co-tc-shopper-web-stage.serempre.dev/'
        self.driver = webdriver.Firefox(executable_path='Drivers/geckodriver')
        driver = self.driver
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)

    def test_serempre(self):
        driver = self.driver
        # Select Bogotá in dropdown menu and click on "Continuar" button
        dropdown = driver.find_element_by_id('react-select-2-input')
        dropdown.send_keys('Bogotá', Keys.ENTER)
        time.sleep(2)
        button_continue = driver.find_element_by_class_name('sc-jSFkmK')
        button_continue.click()

        # Click on "Consumidor" button
        time.sleep(2)
        button_consumer = driver.find_element_by_class_name('sc-jSFkmK')
        button_consumer.click()
        time.sleep(2)

        # Input a phone number
        phone_number = driver.find_element_by_id('abi-phone')
        phone_number.send_keys('321654928')
        time.sleep(2)
        button_input = driver.find_element_by_class_name('sc-jSFkmK')
        button_input.click()

        # Checking terms and policies
        time.sleep(5)
        checkbox_terms = driver.find_element_by_name('abi-checkbox-terms')
        if checkbox_terms.is_displayed() is True and checkbox_terms.is_selected() is False:
            checkbox_terms.click()
        checkbox_policies = driver.find_element_by_name('abi-checkbox-policies')
        if checkbox_policies.is_displayed() is True and checkbox_policies.is_selected() is False:
            checkbox_policies.click()
        time.sleep(2)
        button_continue = driver.find_element_by_class_name('sc-jSFkmK')
        button_continue.click()

        # Fill the form with first name, last name, and email
        first_name = driver.find_element_by_id('register-name')
        first_name.send_keys('Candy')
        last_name = driver.find_element_by_id('register-lastName')
        last_name.send_keys('Montes')
        email = driver.find_element_by_id('register-email')
        email.send_keys('candymontes@gmail.com')
        time.sleep(2)
        button_next = driver.find_element_by_class_name('sc-jSFkmK')
        button_next.click()

        # Input the address Cra. 13 #96-67
        address = driver.find_element_by_id('address')
        address.send_keys('Cra. 13 #96-67')
        time.sleep(4)
        nearest_location = driver.find_element_by_class_name('sc-cBoprd')
        nearest_location.click()
        time.sleep(4)
        button_select_location = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div[2]/div/form[2]/button')
        button_select_location.click()

        # Validation text
        validated = driver.find_element_by_class_name('sc-carGAA')
        print(validated.text)
        #self.assertEqual(validated.text, '¡Te has validado exitosamente!')
        time.sleep(4)
        validated = driver.find_element_by_class_name('text-gray-secondary')
        print(validated.text)
        self.assertTrue(validated.text == 'Ingresa el código que enviamos a tu celular +57 321654928')

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output='reports', report_name='test_serempre-report'))