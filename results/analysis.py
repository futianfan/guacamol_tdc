import pickle, os  
import numpy as np 
import matplotlib.pyplot as plt 
iter2score = {}
idx_lst = []


# ### graph ga
# folder = "/Users/futianfan/Downloads/spring2021/guacamol_tdc/results/graph_ga"
# for file in os.listdir(folder): 
# 	if file[-3:]!='pkl':
# 		continue 
# 	idx = int(file.split('.')[0])
# 	idx_lst.append(idx)
# 	full_file = os.path.join(folder, file)
# 	assert os.path.exists(full_file)
# 	smiles2score = pickle.load(open(full_file, 'rb'))
# 	for smiles,score in smiles2score.items():
# 		smiles2score[smiles] = -score 
# 	score_lst = [score for smiles, score in smiles2score.items()]
# 	score_lst.sort(reverse = True)

# 	top1 = score_lst[0]
# 	top10 = np.mean(score_lst[:10])
# 	top100 = np.mean(score_lst[:100])
# 	iter2score[idx] = (top1, top10, top100)

# 	if idx in [100,500,1000,5000]:
# 		smiles_score_lst = [(smiles,score) for smiles, score in smiles2score.items()]
# 		smiles_score_lst.sort(key = lambda x:x[1])
# 		smiles_score_lst = smiles_score_lst[:100]
# 		with open(os.path.join(folder, 'smiles_lstm_' + str(idx) + '.txt'),'w') as fout:
# 			for smiles,score in smiles_score_lst:
# 				fout.write(smiles + '\t' + str(score) + '\n')



# idx_lst.sort()
# plt.plot(idx_lst, [iter2score[idx][0] for idx in idx_lst], label = 'top1')
# plt.plot(idx_lst, [iter2score[idx][1] for idx in idx_lst], label = 'top10')
# plt.plot(idx_lst, [iter2score[idx][2] for idx in idx_lst], label = 'top100')
# plt.legend()
# plt.savefig('results/graph_ga.png')
# plt.cla()





### smiles lstm
scale = 15 ### the score is normalized to [0,1], so we need to recover 
folder = "/Users/futianfan/Downloads/spring2021/guacamol_tdc/results/smiles_lstm_hc_"
i_list = [1,2,3]
num_lst = [i*100 for i in range(1,51)]
for i in i_list:
	result_folder = folder + str(i)
	top1, top10, top100 = [],[],[]
	for j in range(1,51):
		file = str(j * 100) + '.pkl' 
		file = os.path.join(result_folder, file)

		## get top-100,10,1
		smiles2score = pickle.load(open(file, 'rb'))
		for smiles,score in smiles2score.items():
			smiles2score[smiles] = -scale*score 
		score_lst = [score for smiles, score in smiles2score.items()]
		score_lst.sort()

		top1.append(score_lst[0])
		top10.append(np.mean(score_lst[:10]))
		top100.append(np.mean(score_lst[:100]))

		# 100, 500, 1k, 5k 
		if j in [1,5,10,50]:
			smiles_score_lst = [(smiles,score) for smiles, score in smiles2score.items()]
			smiles_score_lst.sort(key = lambda x:x[1])
			smiles_score_lst = smiles_score_lst[:100]
			with open('results/smiles_lstm_' + str(i) + '_' + str(j*100) + '.txt','w') as fout:
				for smiles,score in smiles_score_lst:
					fout.write(smiles + '\t' + str(score) + '\n')
	if i==1:
		plt.plot(num_lst, top1, color='b', label = 'top1')
		plt.plot(num_lst, top10, color='y', label = 'top10')
		plt.plot(num_lst, top100, color='r', label = 'top100')
	else:
		plt.plot(num_lst, top1, color='b', )
		plt.plot(num_lst, top10, color='y', )
		plt.plot(num_lst, top100, color='r', )		
plt.legend()
plt.savefig('results/smiles_lstm_hc.png')













