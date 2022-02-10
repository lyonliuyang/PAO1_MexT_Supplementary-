import requests
import os
import time

def arg():
    pass
    arg.workdir = '/data/Lyon/project2/orthology_pao1_fromdatabase/'
    return

def main():
    arg()
    os.system("""cut -f5 '%s/Pseudomonas_aeruginosa_PAO1_107.tsv' | sed 's/PGD//g' > %s/PAO1_gene_id.txt"""%(arg.workdir,arg.workdir))
    with open('%s/PAO1_gene_id.txt'%arg.workdir) as f:
        PAO1_id = f.readlines()
    
    script_log = open('%s/download.sh'%arg.workdir,'w')
    for i in PAO1_id:
        
        _id_ = i.rstrip()
        if 'Gene ID' in _id_:continue
        url = ('http://pseudomonas.com/orthologs/list?format=tab&extension=tab&id=%s'%_id_)

        script_log.write("""wget '%s' -O %s/orthology_group_pao1_tab/%s.tab\n"""%(url,arg.workdir,_id_))
        script_log.write('sleep 1s \n')
    script_log.close()
    return

if __name__ == '__main__':
    main()
    #os.system("""'nohup bash %s/download.sh &'%arg.workdir""")
