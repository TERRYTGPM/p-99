import os
import shutil
import time

pathname = input("Enter the path name: ")

vartime = time.time()

existancetime = input("How old des the file have to be (in months): ")

if os.path.exists(pathname) == true:
     files = os.listdir(pathname)

     for i in files:
           name, extention = os.splitext(i)

           if os.path.exists(pathname+"/"+name+"."+extention):
                  fullnameofthefile = pathname+"/"+name+"."+extention
                  fileage = os.stat(pathname+"/"+name+"."+extention).st_ctime
                  fileageins = time.gmtime(pathname+"/"+name+"."+extention)
                  fileageinm = int(time.strftime("%m", fileageins))

                  if fileageinm<= existancetime:
                        os.remove(fullnameofthefile)
                        print("DELETED")
                    else:
                          continue
           else:
                 continue
else:
      print("this is not a directory")
                 