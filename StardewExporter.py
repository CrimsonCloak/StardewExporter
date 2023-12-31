from prometheus_client import start_http_server, Metric, REGISTRY
import time, os, sys
from bs4 import BeautifulSoup

# Version 1.0

class StardewExporter(object):
  def collect(self):
    if(len(sys.argv) >1): #Check if an argument was given -> if so set path to that argument
      File_Path = sys.argv[1]
    #SaveFile = 'C:\\Users\\alexa\\AppData\\Roaming\\StardewValley\\Saves\\Prom_347722748\\SaveGameInfo'
    else: #No path given -> Basic example savegame
      File_Path = os.path.join(os.path.dirname(__file__), "savefile/SaveGameInfo")
    #print(File_Path)
# Fetch XML data 
    with open(File_Path, 'r') as f:
        data = f.read()
        
    Bs_data = BeautifulSoup(data,features="lxml")
    
    #Metrics for Currencies 

    #Metric for Current Money

    Money = Bs_data.find("money")

    CurrentMoney = Metric(name="sv_money", documentation="Displays current amount of money", typ="gauge")    
    CurrentMoney.add_sample("sv_money", labels={}, value=Money.contents[0])
    yield CurrentMoney

    #Metric for Qigems

    Qigems = Bs_data.find("qigems")

    CurrentQigems = Metric(name="sv_qigems", documentation="Displays current amount of qigems", typ="gauge")    
    CurrentQigems.add_sample("sv_qigems", labels={}, value=Qigems.contents[0])
    yield CurrentQigems


    #Metrics for Player Statistics
    #Metrics for Farming level
    FarmLevel= Bs_data.find("farminglevel")
    FarmingLevel = Metric(name="sv_farminglevel", documentation="Displays current farming level", typ="gauge")    
    FarmingLevel.add_sample("sv_farminglevel", labels={}, value=FarmLevel.contents[0])
    yield FarmingLevel

    #Metrics for Mining level
    MineLevel= Bs_data.find("mininglevel")
    MiningLevel = Metric(name="sv_mininglevel", documentation="Displays current mining level", typ="gauge")    
    MiningLevel.add_sample("sv_mininglevel", labels={}, value=MineLevel.contents[0])
    yield MiningLevel


    #Metrics for Combat level
    FightLevel= Bs_data.find("combatlevel")
    CombatLevel = Metric(name="sv_combatlevel", documentation="Displays current combat level", typ="gauge")    
    CombatLevel.add_sample("sv_combatlevel", labels={}, value=FightLevel.contents[0])
    yield CombatLevel

    #Metrics for Foraging level
    Foraging= Bs_data.find("foraginglevel")
    ForagingLevel = Metric(name="sv_foraginglevel", documentation="Displays current foraging level", typ="gauge")    
    ForagingLevel.add_sample("sv_foraging", labels={}, value=Foraging.contents[0])
    yield ForagingLevel

     #Metrics for Fishing level
    Fishing= Bs_data.find("fishinglevel")
    FishingLevel = Metric(name="sv_fishinglevel", documentation="Displays current fishing level", typ="gauge")    
    FishingLevel.add_sample("sv_fishinglevel", labels={}, value=Fishing.contents[0])
    yield FishingLevel

     #Metrics for Luck level
    Luck= Bs_data.find("lucklevel")
    LuckLevel = Metric(name="sv_lucklevel", documentation="Displays current luck level", typ="gauge")    
    LuckLevel.add_sample("sv_lucklevel", labels={}, value=Luck.contents[0])
    yield LuckLevel
    #Metric for Deepest Mine Level

    Mine = Bs_data.find("deepestminelevel")
    print(Mine)
    DeepestMineLevel = Metric(name="sv_deepestminelevel", documentation="Displays the deepest level of the mine", typ="gauge")    
    DeepestMineLevel.add_sample("sv_deepestminelevel", labels={}, value=Mine.contents[0])
    yield DeepestMineLevel




    #Metrics for miscellaneous statistics of player
    # List all children to explore data
    Stats = Bs_data.find("stats").children
    for item in Stats:
      # print(item)
      # print(item.name)
      # print("\n")
      if(item.text):
        StatName = Metric(name=("sv_" + item.name),documentation="" ,typ="gauge")
        StatName.add_sample(("sv_" + item.name), labels={"Name": item.name, "Category": "Misc_Stats"}, value=item.contents[0])
        yield StatName
    # Mine = Bs_data.find("deepestminelevel")
    # DeepestMineLevel = Metric(name="sv_deepestminelevel", documentation="Displays the deepest level of the mine", typ="gauge")    
    # DeepestMineLevel.add_sample("sv_deepestminelevel", labels={}, value=Mine.contents[0])
    # yield DeepestMineLevel
  



    # Convert requests and duration to a summary in seconds
if __name__ == '__main__':
  start_http_server(9321)
  REGISTRY.register(StardewExporter())

  while True: time.sleep(1)