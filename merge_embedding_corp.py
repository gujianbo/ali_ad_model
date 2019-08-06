import sys,time,os

user_rec={}
def readfile(fold,outfile):
	for filename in os.listdir(fold):
		if not fold.endswith("_corp"):
			continue
		print("process "+filename)
		with open(filename,"r") as fd:
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
	