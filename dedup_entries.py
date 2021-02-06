
file_path = "../pq1a/resultado_parcial.tsv"
outfile_path = "../pq1a/resultado_parcial0.tsv"

file = open(file_path, "r", encoding="utf8")
outfile = open(outfile_path, "w", encoding="utf8")

filelines = file.readlines()

for line in filelines:
    
    line = line.strip().split("\t")
    
    #doi = line[0]
    #rights = line[1]
    #pub_id_list = line[2].split("||")
    #authors_lattes_list = line[3].split("||")
    
    print(line)
    
    id = line[0]
    found_pub_list = line[1].split("||")
    lattes_id_list = line[2].split("||")
    nome_list = line[3].split("||")
    grande_area_list = line[4].split("||")
    area_list = line[5].split("||")
    ano_list = line[7].split("||")
    doi_list = line[8].split("||")
    titulo_list =line[9].split("||")
    
    #pub_id_list= list(dict.fromkeys(pub_id_list))
    #authors_lattes_list = list(dict.fromkeys(authors_lattes_list))
    
    
    found_pub_list= list(dict.fromkeys(found_pub_list))
    lattes_id_list= list(dict.fromkeys(lattes_id_list))
    nome_list= list(dict.fromkeys(nome_list))
    grande_area_list= list(dict.fromkeys(grande_area_list))
    area_list= list(dict.fromkeys(area_list))
    ano_list= list(dict.fromkeys(ano_list))
    doi_list= list(dict.fromkeys(doi_list))
    titulo_list= list(dict.fromkeys(titulo_list))
    

    #pub_id = '||'.join(pub_id_list)
    #authors_lattes = '||'.join(authors_lattes_list)
    
    found_pub = '||'.join(found_pub_list)
    lattes_id = '||'.join(lattes_id_list)
    nome = '||'.join(nome_list)
    grande_area = '||'.join(grande_area_list)
    area = '||'.join(area_list)
    ano = '||'.join(ano_list)
    doi = '||'.join(doi_list)
    titulo = '||'.join(titulo_list)
    
    
    #outline = doi + "\t" + rights + "\t" +  pub_id + "\t" +  authors_lattes + "\n"
    
    outline = id + "\t" + found_pub + "\t" +  lattes_id + "\t" +  nome + "\t" +  grande_area + "\t" +  area + "\t" +  ano + "\t" +  doi + "\t" +  titulo + "\n"
    
    print(outline)
    
    outfile.write(outline)
    
file.close()    
outfile.close()
    
    
    
    
        
        
    
    
    
    
    #10.15468/0t4xnc