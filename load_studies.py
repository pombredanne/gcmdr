from general_tm_utils import *
from general_utils import *

#this is my conf, make your own -- no need to commit
from stephen_joseph_conf import *

#getting the studytreelist from this file
#getting the synthottolid from here as well
from metazoa import *

print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

delete_database(dload)
copy_database(dott,dload)

print "loading trees"
for i in studytreelist:
    load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"loaded_"+i+".tre",False)


