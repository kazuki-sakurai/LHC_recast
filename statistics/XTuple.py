#import RTuple
class XTuple:
  
   def __init__(self,name,labels):
      self._file = open(name+".dat",'w')
      self._data = []
      self._dic={}
      j=0
      for label in labels:
         i0 = label.find("/")
         i1 = label.find("[")
         i = i0
         if (i1 >0): i = i1
         xlabel = label[:i]
         self._dic[j]=xlabel
         self._dic[xlabel]=j
         print " booking ",xlabel," ",label
         self._data.append(0.)
         j=j+1

      n = len(self._data)
      sr = ""
      for i in range(n):
         send = "\t"
         if (i == n-1): send = "\n"
         
         sr = sr + self._dic[i] + send
      self._file.write(sr)

   def fillItem(self,name,values):
      if (self._dic.has_key(name) == False):
         print " error not label in ntuple ",name
      i=self._dic[name]
      self._data[i] = values

   def fill(self):
      n = len(self._data)
      sr = ""
      for i in range(n):
         send = "\t"
         if (i == n-1): send = "\n"
         
         sr = sr + str(self._data[i]) + send
      self._file.write(sr)
      self._data[i] = 0.

   def close(self):
      self._file.close()


def test():
   labels = ("i/I","n/I","x[n]/F")
   tup = XTuple("testing",labels)
   for i in range(10):
      tup.fillItem("i",i)
      tup.fillItem("n",i+1)
      tup.fillItem("x",range(i+1))
      tup.fill()
   tup.close()

#def Viewer(char):
   #RTuple.translate(char)
   #RTuple.Viewer(char)
