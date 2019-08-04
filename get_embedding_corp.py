import sys,time

user_rec={}

def readfile(file):
	cnt=0
	with open(file,"r") as fd:
		for line in fd:
			cnt+=1
			if cnt%100000==0:
				print(str(cnt)+" lines")
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
			process(user_id,time_stamp,btag,cate,brand)
			
def sort_corp(file):
	fd=open(file,"w")
	for user in user_rec.keys():
		items=user_rec[user]
		item_dic={}
		li=""
		for i in items:
			(tm,cate)=i.split(":")
			item_dic[tm]=cate
		for k in sorted(item_dic.keys()):
			li+=k+":"+item_dic[k]+","
		fd.write(user+"\t"+li.strip()+"\n")
	fd.close()

def process(user_id,time_stamp,btag,cate,brand):
	if btag!="pv":
		return
	if user_id not in user_rec:
		user_rec[user_id]=[]
	user_rec[user_id].append(time_stamp+":"+cate)

if __name__=="__main__":
	readfile(sys.argv[1])
	sort_corp(sys.argv[2])