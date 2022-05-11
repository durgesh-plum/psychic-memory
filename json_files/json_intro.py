import json

car_data = {"name":"tesla", "engineer":"electric"}

print(car_data)
print(car_data["name"])

car_data_json_String = json.dumps(car_data)

print(car_data_json_String)

#class RatesParser:

 #   def __init__(self, rates_file):
  #      rate_info = self.open_json_file(rates_file)
   #     self.base = rate_info["base"]
    #    self.date = rate_info["date"]
     #   self.rates = rate_info["rates"]
     #   self.aud = self.rates["AUD"]
#
 #       self.gbp = self.rates["GBP"]
  #      self.usd = self.rates["USD"]
#
 #   def open_json_file(self, file):
  #      with open(file) as rates:

   #         return json.load(rates)
#
#
r#ate_reader = RatesParser("exchange_rates.json")
#pr#int(rate_reader.aud)
#
#
#
