import csv
import numpy as np

def get_DF(bestandsnaam):
    
    DF = []
    with open(bestandsnaam) as instructions:
        for instruction in csv.reader(instructions, delimiter=';'):
            DF.append(instruction)
    
    return DF[:31]


def write_pasjes(NDF, bestandsnaam):
    
    with open(bestandsnaam, 'w', newline='') as target:
        writer = csv.writer(target, delimiter=';')
        
        for row in NDF:
            writer.writerow(row)

def write_names(DF):
    names_list = []

    for row in DF[1:]:
        for name in row[1:]:
            if name == "":
                pass

            elif name == " ":
                pass

            elif name in names_list:
                pass

            elif name == "0":
                pass

            elif name == 0:
                pass

            else:
                names_list.append(name)

    return names_list

def append_to_name(schema, naam, appendix):
    for i,row in enumerate(schema):
        if row[0] == naam:
            schema[i].append(appendix)

    return schema


if __name__ == "__main__":
    
    DF = get_DF("Werkschema.csv")
    names = write_names(DF)

    SCHEMA = [[n] for n in names]
    
    DF = np.array(DF)
    taken = DF[0]

    #Ga door shifts
    for chift_nummer,koppel_1 in enumerate([(1,7),(7,13),(13,19),(19,25),(25,30)]):
#        print("Shift %d" % chift_nummer)
        

        for taak in [(i,i + 3) for i in range(1,58,3)]:
#            print("taak is: %s" % DF[0,taak[0]])
            TAAK = DF[0,taak[0]]   
        
            medewerkers_in_cel = []    
            cel = DF[koppel_1[0]:koppel_1[1],taak[0]:taak[1]]
            print(chift_nummer)
            print(TAAK)
            print(cel)
            
            for i, naam in np.ndenumerate(cel):
                if naam == "" or naam == "0" or naam == 0:
                    pass

                else:
                    medewerkers_in_cel.append(naam)
                    
                    NAAM = naam
                    SCHEMA = append_to_name(SCHEMA, NAAM, TAAK)

        for i, row in enumerate(SCHEMA):
            if len(row) != chift_nummer + 2:
                nieuwe_rij = row + ["-"]
                SCHEMA[i] = nieuwe_rij
    
    
    write_pasjes(SCHEMA, "pasjes.csv")