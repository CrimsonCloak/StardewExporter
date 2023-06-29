from prometheus_client import start_http_server, Metric, REGISTRY
import time
from bs4 import BeautifulSoup

# Version 1.0

class StardewExporter(object):
  def collect(self):
    #nog aan te passen!!!!
    SaveFile = 'C:\\Users\\alexa\\AppData\\Roaming\\StardewValley\\Saves\\Prom_347722748\\SaveGameInfo'


# Fetch XML data 
    with open(SaveFile, 'r') as f:
        data = f.read()
    Bs_data = BeautifulSoup(data, "html")
    
    #print(Bs_data)
    Mine = Bs_data.find("deepestminelevel")
    print(Mine)

    DeepestMineLevel = Metric(name="sv_deepestminelevel", documentation="Displays the deepest level of the mine", typ="gauge")    
    DeepestMineLevel.add_sample("sv_deepestminelevel", labels={}, value=Mine.contents[0])
    yield DeepestMineLevel

    Money = Bs_data.find("money")

    CurrentMoney = Metric(name="sv_money", documentation="Displays current amount of money", typ="gauge")    
    CurrentMoney.add_sample("sv_money", labels={}, value=Money.contents[0])
    yield CurrentMoney





    # Convert requests and duration to a summary in seconds
if __name__ == '__main__':
  start_http_server(9321)
  REGISTRY.register(StardewExporter())

  while True: time.sleep(1)