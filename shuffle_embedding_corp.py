import sys,time,os
import hashlib

def readfile(fold,outfile):
	fdout={}
	filelist=[]
	for filename in os.listdir(fold):
		print(filename)
		if filename.endswith("_corp"):
			filelist.append(filename)
	filelist.sort()
	print(filelist)
	for filename in filelist:
		print("process "+filename)
		with open(fold+filename,"r") as fd:
			cnt=0
			for line in fd:
				cnt+=1
				if cnt%1000000==0:
					print(str(cnt)+" lines")
				try:
					line=line.strip()
					(user,words)=line.split("\t")
				except:
					print("Error line:",line)
					continue
				bk = bucket(user)
				if bk not in fdout:
					fdout[bk] =open(outfile+"_"+str(bk),"w")
				fdout[bk].write(line+"\n")
	
	for k in fdout.keys():
		fdout[k].close()

def bucket(user):
	hash_md5 = hashlib.md5(user.encode("utf-8"))
	hash_md5_hex = hash_md5.subString[15,20]
	return int(hash_md5_hex, 16)%16

if __name__=="__main__":
	readfile(sys.argv[1],sys.argv[2])
	