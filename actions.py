from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet,AllSlotsReset
import requests

class ActionWeather(Action):
	def name(self):
		return 'action_weather'

	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = '' #your apixu key
		loc = tracker.get_slot('location')
		api_address='http://api.weatherstack.com/current?access_key={}&query={}'.format(api_key,loc)
		current = requests.get(api_address).json()
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['weather_descriptions'][0]
		temperature_c = current['current']['temperature']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_speed']
		#dispatcher.utter_message("You said " +tracker.latest_message["text"])
		#output sentence format
		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
		dispatcher.utter_message(response)
		#SlotSet('location',loc)
		return [AllSlotsReset()]
