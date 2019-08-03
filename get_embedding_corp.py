import sys,time



def readfile(file)
	
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
			if dt<'20170422' or dt>'20170513':
				continue

def process():
	if user_id in 

if __name__=="__main__":
	