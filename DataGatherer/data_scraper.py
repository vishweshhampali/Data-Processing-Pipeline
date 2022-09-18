import json
import csv
import urllib.request
import sys
import codecs
import logging
from datetime import datetime

cities = ['mumbai','pune']

current_datetime =  datetime.now()
str_current_datetime = str(current_datetime)

log_file_name = str_current_datetime+".log"

logging.basicConfig(filename="/home/sasuke/Projects/DataProcessing/DataGatherer/DataScrapingLogs/"+log_file_name, level=logging.DEBUG, format="%(asctime)s %(message)s")

for city in cities:
    result_file_name = str_current_datetime+"_"+city.upper()+"_.json"
    
    try:
        logging.info("Getting information from website"+":"+city.upper())
        ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+city+"/yesterday?unitGroup=metric&key=LXDRVGBYRHAFP5SWNPQSKCST7&contentType=json")
        logging.info("Information loaded in ResultBytes"+":"+city.upper())
        jsonData = json.loads(ResultBytes.read().decode('utf-8'))
        logging.info("Information conversted to JSON"+":"+city.upper())
        if jsonData:
            with open("/home/sasuke/Projects/DataProcessing/DataGatherer/DataScraped/"+result_file_name, "w") as outfile:
                json.dump(jsonData, outfile)
            logging.info("Json file created successfully"+":"+city.upper())
            logging.info("------------------------------------------------------")
        else:
            logging.warning("jsonData is null"+":"+city.upper())
            logging.info("------------------------------------------------------")
    except urllib.error.HTTPError  as e:
        ErrorInfo= e.read().decode()
        logging.warning('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo= e.read().decode()
        logging.warning('Error code: ', e.code,ErrorInfo)
        sys.exit()


 
