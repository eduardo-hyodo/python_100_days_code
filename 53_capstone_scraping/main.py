from property_scrapper import PropertyScrapper 
from form_submit import FormSubmit

ps = PropertyScrapper()
price_list = ps.get_prices()
url_list = ps.get_urls()
address_list = ps.get_address()

form = FormSubmit()
form.post_properties(price_list,url_list,address_list)
