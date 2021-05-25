import hashlib
  
def getHash(string):
    sha = hashlib.new("sha1")
    sha.update(string.encode("UTF-8"))
    return sha.hexdigest()
salt = []
for i in range(10000000,50000001):
    salt.append(str(i)+"salt_for_you")
print("Make Salt Complete")
fd = open("./rainbowtable.txt", "a")
for parse in salt:
    hashstr = parse
    for i in range(500):
        hashstr = getHash(hashstr)
    fd.writelines(parse + ':' + hashstr + "\n")
fd.close()
