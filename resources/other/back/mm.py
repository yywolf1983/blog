import os

def Test2(rootDir): 
    mm_list = ["mp3","w3m","flac","webm"]
    obt = open("mm.m3u","a+")
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 

        if path.split(".")[-1] in mm_list:
            print("https://fs.usda.one/mm/"+path)
            obt.write("https://fs.usda.one/mm/"+path+"\n")
        if os.path.isdir(path): 
            Test2(path) 
    obt.close()

obt = open("mm.m3u","w+")
obt.close()
Test2("./")
