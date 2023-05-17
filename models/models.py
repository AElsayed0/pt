# models.py
from odoo import models, fields, api
from bs4 import BeautifulSoup
import requests


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    link = fields.Char(string='Link')
    base_number = fields.Char(string='Base Number')
    card_number = fields.Char(string='Card Number')

    def confirm_link(self):
        try:
            for order in self:
                if order.link:
                    response = requests.get(order.link)

                    soup = BeautifulSoup(response.content, 'html.parser')

                    base_number_data = soup.select_one('[id*="basenumber"]').text  # Gets the base number using the id
                    order.base_number = base_number_data

                    card_number_data = soup.select_one('[id*="idnumber"]').text   # Gets the card number using the id
                    order.card_number = card_number_data

        except:
            order.base_number = order.card_number = "الرجاء التأكد من الرابط"

