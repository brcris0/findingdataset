import json


file_path = "../pq1a/pub_dataset2.tsv"

openaire_folder = "../pq1a/openaire/"

log_file_path = "../pq1a/dataset2_log_file.tsv"


log_file = open(log_file_path, "w", encoding="utf8")



with open(file_path, "r", encoding="utf8") as file:
    
    i = 0

    
    for item in file:
        
        line = item.strip()
        

        #if line[1] == "True" and line[2] == "True":
            
        id = line #[0]
        
        jsonfile = open(openaire_folder + id[-1] + "/" + id + "/d-" + id + ".json", "r", encoding="utf8")
        
        json_text = json.load(jsonfile)
        
        results = json_text["result"]
        
        for result in results:
            
            RelationshipType_Name = result["RelationshipType"]["Name"]
            RelationshipType_SubType = result["RelationshipType"]["SubType"]
            
            source_identifiers = result["source"]["Identifier"]
            

            identifiers_seq = ""
            identifiers_scheme = ""

            
            for identifier in source_identifiers:
                
                
                if identifier["IDScheme"] != "D-Net Identifier":
                    
                    identifiers_seq = identifiers_seq  + identifier["ID"] + "||"
                    identifiers_scheme = identifiers_scheme  + identifier["IDScheme"] + "||"
    
            
            if identifiers_seq != "":
                
                identifiers_seq = identifiers_seq[:-2]
                identifiers_scheme = identifiers_scheme[:-2]
                
                
                            
            creators = result["source"]["Creator"]
                
            
            creators_names = ""
            creators_ids = ""
                
            for creator in creators:
                
                creators_names = creators_names + "'" + creator["Name"] + "'||"
                
                if creator["Identifier"] != []:
                    
                    creators_ids = creators_ids + "'" + creator["Identifier"] + "'||"
                    
                    
            if creators_names != "":                  
                creators_names = creators_names[:-2]
                
            if creators_ids != "":                  
                creators_ids= creators_ids[:-2]



            
            if RelationshipType_SubType != "References" and RelationshipType_SubType != "IsReferencedBy":
                
                i += 1
                
                if creators != []:
                    
                    log_line =  str(i) + "\t" + id + "\t" + RelationshipType_Name + "_" + RelationshipType_SubType + "\t" + identifiers_seq + "\t" + identifiers_scheme + "\t" + creators_names + "\t" + creators_ids + "\n"

                    print(log_line)

                    log_file.write(log_line)
                        
log_file.close()






