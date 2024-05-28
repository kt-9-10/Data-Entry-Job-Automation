from zillow_controller import ZillowController
from form_controller import FormController

zc = ZillowController()
links = zc.get_list_of_links()
prices = zc.get_list_of_prices()
addresses = zc.get_list_of_address()

fc = FormController()
fc.submit_form(addresses, prices, links)
