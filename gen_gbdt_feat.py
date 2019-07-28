import sys
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import random


def gen_feat(infile):
	X=[]
	Y=[]
	cnt=0
	with open(infile,"r") as fd:
		for line in fd:
			cnt+=1
			if cnt==1:
				continue
			if random.randint(0,20)>=1:
				continue
			line=line.strip()
			x,y=gen_data(line)
			X.append(x)
			Y.append(y)
	return X,Y

def test(gbdt,infile):
	y_pred=[]
	Y=[]
	cnt=0
	with open(infile,"r") as fd:
		for line in fd:
			cnt+=1
			if cnt==1:
				continue
			if random.randint(0,20)>=1:
				continue
			#if cnt==10000:
			#	break
			line=line.strip()
			x,y=gen_data(line)
			Y.append(y)
			y_p=gbdt.predict_proba([x])
			y_pred.append(y_p[0])
	return np.array(y_pred),np.array(Y)
	
def auc_get(y_pred,y):
	#print(y)
	print("shape:",y_pred.shape)
	print(y_pred)
	fpr, tpr, thresholds = roc_curve(y, y_pred[:, 1])
	roc_auc = auc(fpr, tpr)
	
	print("fpr:",fpr, ",tpr:",tpr, "thresholds:",thresholds,"auc:",roc_auc)
	plt.figure()
	lw = 2
	plt.plot(fpr, tpr, color='darkorange',
			 lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
	plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
	plt.xlim([0.0, 1.0])
	plt.ylim([0.0, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('Receiver operating characteristic example')
	plt.legend(loc="lower right")
	plt.show()

def gen_data(line):
	x=[]
	y=[]
	base,user_feat,ad_feat,clk=line.split("|")
	(cms_segid,cms_group_id,final_gender_code,age_level,pvalue_level,shopping_level,occupation,new_user_class_level)=(None,None,None,None,None,None,None,None)
	try:
		(cms_segid,cms_group_id,final_gender_code,age_level,pvalue_level,shopping_level,occupation,new_user_class_level)=user_feat.split(",")
	except:
		print("user_feat is",user_feat)
	(cate_id,campaign_id,customer,brand,price)=(None,None,None,None,None)
	try:
		(cate_id,campaign_id,customer,brand,price)=ad_feat.split(",")
	except:
		print("ad_feat is",ad_feat)
	x=[]
	try:
		x.append(float(cms_segid))
	except:
		x.append(float(-1))
	try:
		x.append(float(cms_group_id))
	except:
		x.append(float(-1))
	try:
		x.append(float(final_gender_code))
	except:
		x.append(float(-1))
	try:
		x.append(float(age_level))
	except:
		x.append(float(-1))
	try:
		x.append(float(pvalue_level))
	except:
		x.append(float(-1))
	try:
		x.append(float(shopping_level))
	except:
		x.append(float(-1))
	try:
		x.append(float(occupation))
	except:
		x.append(float(-1))
	try:
		x.append(float(new_user_class_level))
	except:
		x.append(float(-1))
	
	try:
		x.append(float(cate_id))
	except:
		x.append(float(-1))
	try:
		x.append(float(campaign_id))
	except:
		x.append(float(-1))
	try:
		x.append(float(brand))
	except:
		x.append(float(-1))
	try:
		x.append(float(price))
	except:
		x.append(float(-1))
	
	y=float(clk)
	return x,y

def train(X,y):
	gbdt = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=5, random_state=0)
	gbdt.fit(X,y)
	return gbdt

if __name__=="__main__":
	X,y=gen_feat(sys.argv[1])
	print("begin to train")
	gbdt=train(X,y)
	print("begin to test")
	y_pred,y=test(gbdt,sys.argv[2])
	auc_get(y_pred,y)