import pandas as pd
import os

def arg():
    pass
    arg.workdir = '/data/Lyon/project2/orthology_pao1_fromdatabase/'
    return
  
def main():
    arg()
    os.system("""grep 'Reference' %s/orthology_group_pao1_tab/*.tab | cut -d":" -f1 | rev | cut -d"/" -f1 | rev | sort | uniq -c | sort | awk '{if($1==1)print$2}' | sed 's/.tab//g'| sed 's/^/PGD/g' > %s/single_copy_genesID.tsv"""%(arg.workdir,arg.workdir))
    df = pd.read_csv('%s/Pseudomonas_aeruginosa_PAO1_107.tsv'%arg.workdir,sep='\t',index_col = 4)
    
    single_copy_genesID_df = pd.read_csv('%s/single_copy_genesID.tsv'%arg.workdir,sep='\t',index_col = 0,names=['PGDID'])
    single_copy_genesID_list = single_copy_genesID_df.index.to_list()
    
    for index,value in df.iterrows():
        if index not in single_copy_genesID_list:
            df.drop(index=index,inplace=True,errors='ignore')
    print(df[['Locus Tag']]) # these are single-copy groups based on PAO1 reference genome.
    
if __name__ == '__main__':
    main()
