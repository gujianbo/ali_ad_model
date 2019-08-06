import sys,time,os

user_rec={}
def readfile(fold,outfile):
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
					if user in user_rec:
						user_rec[user]+=words
					else:
						user_rec[user]=words
				except:
					print("Error line:",line)
					continue
	fdout=open(outfile,"w")
	for k in user_rec.keys():
		fdout.write(k+"\t"+user_rec[k]+"\n")
	fdout.close()
	
if __name__=="__main__":
	readfile(sys.argv[1],sys.argv[2])
	