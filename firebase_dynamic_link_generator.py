# -*- coding:utf-8 -*-

import requests

class GenerateFirebaseDynamicLink():

	FIREBASE_API_URL = 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={}'

	def __init__(self, api_key, domain):
        self.api_key 	= api_key
        self.domain 	= domain
        self.api_url 	= self.FIREBASE_API_URL.format(self.api_key)


     def generate_dynamic_link(self, link, short=True, linkinfo_params={}, suffix_params={}):
        payload = {
            "dynamicLinkInfo": {
                "domainUriPrefix": self.domain,
                "link": link
            },
            "suffix": {
                "option": "SHORT" if short else "UNGUESSABLE"
            }
        }

        ## update the parameters
        payload['dynamicLinkInfo'].update(linkinfo_params)
        payload['suffix'].update(suffix_params)

        ## request firebase dynamic link
        response = requests.post(self.api_url, json=payload)

        data = response.json()

        ## return response if not success
        if not response.status_code == 200:
        	return data

       	## return link data if success response
        return data['shortLink']