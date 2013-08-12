from general_tm_utils import *
from general_utils import *

#this is my conf, make your own -- no need to commit
from stephen_laptop_conf import *

#getting the studytreelist from this file
#getting the synthottolid from here as well
from metazoa import *

print "loading studytreelist:",studytreelist

delete_database(dload)
copy_database(dott,dload)

print "loading trees"
for i in studytreelist:
    ingroup,matchedtaxa = test_one_study(studyloc,i,javapre,treemloc,dload,"loaded_"+i+".tre",False)
    if ingroup == True:
        tfile = open("loaded_"+i+".tre","w")
        for j in matchedtaxa:
            tfile.write(j+"\t"+matchedtaxa[j]+"\n")
        tfile.close()

