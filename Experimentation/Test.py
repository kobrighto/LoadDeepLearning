import Utilities
from os import chdir

chdir('/home/minh/Desktop/Google_Data/processed')

cpuList, memList = Utilities.meanLoad(10,30)

markPoint = int(0.9*len(cpuList))
trainList = cpuList[:markPoint]
testList = cpuList[markPoint:]
X_train,y_train = Utilities.makeTrainorTestList(trainList=trainList,trainingStep=1,inputvector=(2,6)
                                                         ,labelvector=(1,6))
X_test,y_test = Utilities.makeTrainorTestList(trainList=testList,trainingStep=1,inputvector=(1,6)
                                                       ,labelvector=(1,6))

for i in xrange(20):
    print('X_train[',i,']',X_train[i])