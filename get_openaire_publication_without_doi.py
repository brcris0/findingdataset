import requests, os, json, re
import Levenshtein as lev
from bs4 import BeautifulSoup



file_path = "../pq1a/dedup_sem_doi.tsv"

output_path = "../pq1a/output_pub_sem_doi.tsv"

log_file_path = "../pq1a/log_file_sem_doi.tsv"


if not os.path.isfile(log_file_path):
    file = open(log_file_path, "w")
    file.close()
    
if not os.path.isfile(output_path):
    file = open(output_path, "w")
    file.close()



with open(log_file_path, "r", encoding="utf8") as log_file:
    
    log_file_list = []
    
    for item in log_file:
        line = item.strip().split("\t")
        log_file_list.append(line[0])
        


openaire_url_base = "http://api.openaire.eu/search/publications?title="
scholix_url_base = "http://api.scholexplorer.openaire.eu/v2/Links?targetPid="


file = open(file_path, "r", encoding="utf8")

file_lines = file.readlines()

for line in file_lines:
    
    line = line.strip().split("\t")
    
    print(line)

        
    publication_found = False
    
    dataset_found = False
    

    id = line[0]
    
    try: 
        year = line[1]
    except:
        year = ""
        
    try:
        title = line[2]
    except:
        title = ""

    title_key = re.sub('[^A-Za-z0-9]+', '', title).lower()
    
    if id not in log_file_list:
    

        r = requests.get(openaire_url_base + title)
        
        soup = BeautifulSoup(r.text, "lxml")
        
        result = soup.find("result")
        
        year_match = False
                
        title_match = False
        
        if result != None:
            
            publication_found = True
            
            
            items = result.find_all("metadata")
            
            for item in items:
                
                year_match = False
                
                title_match = False
                
                dates = item.find_all("relevantdate")
                
                
                for date in dates:
                    
                    if date.text[:4] == year:
                        
                        year_match = True
                        
                if year_match:
                    
                    print("year match!")
                    
                    
                    titles = item.find_all("title")
                    
                    for title in titles:
                        
                        title_key0 = re.sub('[^A-Za-z0-9]+', '', title.text).lower()
                        
                        distance = lev.distance(title_key, title_key0)
                        
                        if distance <= 10:
                            
                            title_match = True
            
                    if title_match:
                
                        pid = item.find("pid")
                        
                        print("title match!")
                        
                        try:
                            pid = pid.text
                        except:
                            pid = ""
                        
                        output_file = open(output_path, "a")
                        
                        output_file.write(id + "\t" + pid + "\n")
                        
                        output_file.close()
        
            
        

            
        log_file = open(log_file_path, "a")
        log_line = id + "\t" + str(year_match) + "\t" + str(title_match) + "\n"
        log_file.write(log_line)
        
        print(log_line)
        
        log_file.close()
    
        
        
    else:
        print(id, "already processed")
            







