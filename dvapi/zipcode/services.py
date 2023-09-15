import logging
from typing import Dict

from .models import Zipcode

class ZipcodeService:

    @staticmethod
    def get_zipcodes(zipcode: str) -> Dict:
        zipcodes = Zipcode.objects.filter(zipcode=zipcode)
        if not zipcodes:
            return {}
        
        settlements = []

        for zipcodeData in zipcodes:
            settlements.append({
                "key": zipcodeData.settlement_id,
                "name": zipcodeData.settlement,
                "zone_type": zipcodeData.zone,
                "settlement_type": {
                    "name": zipcodeData.settlement_type
                }
            })

        return {
            "zipcode": zipcodes[0].zipcode,
            "locality": zipcodes[0].municipality,
            "federal_entity": {
                "key": zipcodes[0].state_code,
                "name": zipcodes[0].state,
                "code": None
            },
            "settlements": settlements,
            "municipality": {
                "key": zipcodes[0].municipality_code,
                "name": zipcodes[0].municipality
            }
        }
