import requests, os, json
from bs4 import BeautifulSoup



file_path = "D:/pq1a/dedup_doi/"

openaire_folder = "D:/pq1a/openaire/"

log_file_path = "D:/pq1a/log_file.tsv"


if not os.path.isfile(log_file_path):
    file = open(log_file_path, "w")
    file.close()


with open(log_file_path, "r", encoding="utf8") as log_file:
    
    log_file_list = []
    
    for item in log_file:
        line = item.strip().split("\t")
        log_file_list.append(line[0])
        


openaire_url_base = "http://api.openaire.eu/search/publications?doi="
scholix_url_base = "http://api.scholexplorer.openaire.eu/v2/Links?targetPid="



source_files = os.listdir(file_path)
    
for entry in source_files[0:31]:

    with open(file_path + entry, "r", encoding="utf8") as file:
        
        for item in file:
            
            publication_found = False
            
            dataset_found = False
            
            line = item.strip().split("\t")
            
            id = line[0]
            doi = line[1]
            
            if id not in log_file_list:
            
                destination_folder = openaire_folder + id[-1]
                
                print(line)
                
                r = requests.get(openaire_url_base + doi)
                
                soup = BeautifulSoup(r.text, "lxml")
                
                result = soup.find("result")
                
                if result != None:
                    
                    publication_found = True
                    
                    if not os.path.isdir(destination_folder):
                        
                        os.mkdir(destination_folder)
                        
                        
                    publication_file_path = destination_folder + "/" + id + "/" + "p-" + id + ".xml"
                        
                        
                    if not os.path.isfile(publication_file_path):
                        
                        os.mkdir(destination_folder + "/" + id)
        
                        file0 = open(publication_file_path, "w", encoding="utf8")
                        file0.write(str(result))
                        file0.close()
                        
                    else:
                        print("publication already processed")
                        
                    r = requests.get(scholix_url_base + doi + "&sourceType=dataset")
                    
                    datasets_file_path = destination_folder + "/" + id + "/" + "d-" + id + ".json"
                    
                    data = json.loads(r.text)
                
                    
                    if data["result"] != []:
                        
                        dataset_found = True
                        
                        if not os.path.isfile(datasets_file_path):
                            file1 = open(datasets_file_path, "w", encoding="utf-8")
                            json.dump(data, file1, ensure_ascii=False)
                            file1.close()
                            
                        else:
                            print("datasets already processed")
    
                                 
                else:
                    print("publication not found")
                    
                    

                    
                log_file = open(log_file_path, "a")
                log_line = id + "\t" + str(publication_found) + "\t" + str(dataset_found) + "\n"
                log_file.write(log_line)
                
                print(log_line)
                
                log_file.close()
            
                
                
            else:
                print(id, "already processed")
            







