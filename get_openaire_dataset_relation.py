import requests, os, json



file_path = "../pq1a/pub_sem_doi.tsv"

openaire_folder = "../pq1a/openaire/"

log_file_path = "../pq1a/log_file_dataset2.tsv"


if not os.path.isfile(log_file_path):
    file = open(log_file_path, "w")
    file.close()


with open(log_file_path, "r", encoding="utf8") as log_file:
    
    log_file_list = []
    
    for item in log_file:
        line = item.strip().split("\t")
        log_file_list.append(line[0])
        

scholix_url_base = "http://api.scholexplorer.openaire.eu/v2/Links?targetPid="


with open(file_path, "r", encoding="utf8") as file:
    
    filelines = file.readlines()
    
    for line in filelines:
        
        line = line.strip().split("\t")
        
        
        dataset_found = False
        
        
        doi = line[0]
        id = line[1].split("||")[0]
        
        
        if id not in log_file_list:
        
            
            
            print(line)
            
                    
            r = requests.get(scholix_url_base + doi + "&sourceType=dataset")
            
        

            
            data = json.loads(r.text)
        
            
            if data["result"] != []:
                
                dataset_found = True
                
                
                destination_folder = openaire_folder + id[-1]
                
                publication_path = destination_folder + "/" + id
                
                datasets_file_path = publication_path + "/" + "d-" + id + ".json"
                
                if not os.path.isdir(destination_folder):
                            
                    os.mkdir(destination_folder)
                    
                if not os.path.isfile(publication_path):
                            
                    os.mkdir(destination_folder + "/" + id)
            
                
                if not os.path.isfile(datasets_file_path):
                    file1 = open(datasets_file_path, "w", encoding="utf-8")
                    json.dump(data, file1, ensure_ascii=False)
                    file1.close()
                    
                else:
                    print("datasets already processed")

            
            log_file = open(log_file_path, "a")
            log_line = id + "\t" + str(dataset_found) + "\n"
            log_file.write(log_line)
            
            print(log_line)
            
            log_file.close()
        
            
            
        else:
            print(id, "already processed")
        







