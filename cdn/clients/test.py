import glob

txtfiles = []
for file in glob.glob("*"):
    txtfiles.append(file)
for file in txtfiles:
    print("""
        <div class="col"><img src="/cdn/clients/%s" class="img-fluid" alt=""></div>
""" %(file))
