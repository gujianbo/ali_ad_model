import sys,time

def import_ad(ad_file):
	cnt=0
	ad_map={}
	with open(ad_file,"r") as fd:
		for line in fd:
			cnt+=1
			#if cnt>=20:
			#	break
			if cnt==1:
				continue
			line=line.strip()
			try:
				(adgroup_id,cate_id,campaign_id,customer,brand,price)=line.split(",")
			except:
				print("Error line:",line)
				continue
			ad_map[adgroup_id]=line
			#print(adgroup_id,cate_id,campaign_id,customer_id,brand,price)
	return ad_map

def import_user(user_file):
	cnt=0
	user_map={}
	with open(user_file,"r") as fd:
		for line in fd:
			cnt+=1
			#if cnt>=20:
			#	break
			if cnt==1:
				continue
			line=line.strip()
			try:
				(user_id,cms_segid,cms_group_id,final_gender_code,age_level,pvalue_level,shopping_level,occupation,new_user_class_level)=line.split(",")
			except:
				print("Error line:",line)
				continue
			user_map[user_id]=line
			#print(user_id,cms_segid,cms_group_id,final_gender_code,age_level,pvalue_level,shopping_level,occupation,new_user_class_level)
	return user_map
	

def gen_train(ad_file,user_file,log_file,outfile):
	ad_map=import_ad(ad_file)
	user_map=import_user(user_file)
	
	fdout=open(outfile,"w")
	cnt=0
	with open(log_file,"r") as fd:
		for line in fd:
			cnt+=1
			if cnt==1:
				continue
			#if cnt==10000:
			#	break
			line=line.strip()
			try:
				(user_id,time_stamp,adgroup_id,pid,nonclk,clk)=line.split(",")
				tm=abs(int(time_stamp))
				tm=time.localtime(tm)
				tm=time.strftime('%Y-%m-%d %H:%M:%S',tm)
			except:
				print("Error line:",line)
				continue
			
			if user_id in user_map:
				user_feat=user_map[user_id]
				ui=user_feat.split(",")
				user_feat=','.join(ui[1:])
			else:
				user_feat=""
			
			if adgroup_id in ad_map:
				ad_feat=ad_map[adgroup_id]
				ai=ad_feat.split(",")
				ad_feat=','.join(ai[1:])
			else:
				ad_feat=""
			
			fdout.write("%s,%s,%s,%s|%s|%s|%s\n"%(user_id,adgroup_id,tm,pid,user_feat,ad_feat,clk))
	
	fdout.close()

if __name__=="__main__":
	gen_train(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])