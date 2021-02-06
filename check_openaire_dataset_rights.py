import requests, os
from bs4 import BeautifulSoup



file_path = "../pq1a/dedup_datasets2.tsv"

log_file_path = "../pq1a/dedup_datasets2_log.tsv"


if not os.path.isfile(log_file_path):
    file = open(log_file_path, "w")
    file.close()


with open(log_file_path, "r", encoding="utf8") as log_file:
    
    log_file_list = []
    
    for item in log_file:
        line = item.strip().split("\t")
        log_file_list.append(line[0])
        


openaire_url_base = "http://api.openaire.eu/search/datasets?doi="


with open(file_path, "r", encoding="utf8") as file:
    
    filelines = file.readlines()
    
    for line in filelines:
        
        doi = line.strip().split("\t")[0]
        
        if doi not in log_file_list:
        
            rights = "NOT FOUND"
            
            #print(openaire_url_base + doi)
            
            r = requests.get(openaire_url_base + doi)
                    
            soup = BeautifulSoup(r.text, "lxml")
                    
            result = soup.find("result")
            

            
            #print(result)
            
            if result != None:
                
                rights = result.find("bestaccessright")
                
                rights = rights["classid"]
                
                
            log_line = doi + "\t" + rights + "\n"                    
            log_file = open(log_file_path, "a")
            log_file.write(log_line)
                            
            print(log_line)
                            
            log_file.close()
            
        else:
            
            print(doi, "already processed!")







