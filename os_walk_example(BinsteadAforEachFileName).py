import os

basename = "folder"
 
for d in os.walk(basename):
    Fp ="%s" % d[0]

    if 'necessary folder' in Fp:

        print ('Export folder found')
        os.chdir(Fp)

        for filename in os.listdir():
            dst=filename.replace("A","B")
            os.rename (filename, dst)
    
            print(filename + ' to ' + dst)
        
    else:
        SystemExit


                  

