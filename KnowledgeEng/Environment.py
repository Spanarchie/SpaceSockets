__author__ = 'colinmoore-hill'


def envLimits():
    o2range = range(45,68)



def setO2Level(self, persentage):
    target = self.envLimits.o2range
    print ("The range is {}".format(target))

    if (persentage > target[0]):
        return { 'err':1, 'reason':" O2 Too High" }
    if (persentage < target[-1]):
        return { 'err':2, 'reason':" O2 Too low" }

