import sys,time

def fold(file,prefix):
	fdout={}
	with open(infile,"r") as fd:
		for line in fd:
			try:
				(user_id,time_stamp,btag,cate,brand)=line.split(",")
				tm=abs(int(time_stamp))
				tm=time.localtime(tm)
				time_format=time.strftime('%Y-%m-%d %H:%M:%S',tm)
				dt=time.strftime('%Y%m%d',tm)
			except:
				print("Error line:",line)
				continue
			if dt>='20170422' or dt<='20170513':
				if not fdout.has_key(dt):
					fdout[dt]=open(prefix+"/behavior_"+dt+".csv")
				fdout[dt].write(line+"\n")
	for value in fdout.values():
		value.close()

if __name__=="__main__":
	fold(sys.argv[1],sys.argv[2])