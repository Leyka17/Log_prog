name='my_tree_kira.ged'
name_out='output.txt'
file= open(name, 'r',encoding ="utf-8")
information=file.readlines()
file.close()

keys_for_family=['SEX','NAME']
my_family={}
person = {}
name=""
id=""
id_dad=""
id_mom=""
to_out_put=""


for line in information:
    if (line.find('INDI', 0, len(line) - 1) != -1):
            str = line.split(' ')
            person.fromkeys(keys_for_family)
            id=str[1]
    if ((line.find('GIVN',0,len(line)-1)!=-1)):

        str=line.split(' ')
        name=str[2].rstrip()
    if ((line.find('SURN', 0, len(line) - 1) != -1)):
        str = line.split(' ')
        name=name+' '+str[2].rstrip()
        person['NAME']=name
        name=""
    if((line.find('SEX', 0, len(line) - 1) != -1)):
        str=line.split(' ')
        person['SEX']=str[2].rstrip()
        my_family[id]=person.copy()
        person.clear()

    if ((line.find('HUSB', 0, len(line) - 1) != -1)):
        str=line.split(' ')
        id_dad=str[2].rstrip()
    if ((line.find('WIFE', 0, len(line) - 1) != -1)):
        str=line.split(' ')
        id_mom=str[2].rstrip()
    if((line.find('CHIL', 0, len(line) - 1) != -1)):
        str = line.split(' ')
        id = str[2].rstrip()
        to_out_put=to_out_put+("parents("+my_family[id]['NAME']+','+my_family[id_dad]['NAME']+','+my_family[id_mom]['NAME']+')\n')
file=open(name_out,'w',encoding="UTF-8")
file.write(to_out_put)
file.close()



