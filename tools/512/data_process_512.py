
import csv 
import pandas as pd
import os 
from collections import Counter
import numpy as np

# dict_data = {}
all_pri=[]
all_label = []
te_min = 0
te_max = 0
def read_file_and_get_data(filename,num):
    count = 0
    ab_path = os.walk(filename)
    for path,dir_list,file_list in ab_path:
        print("文件数")
        print(len(file_list))
        i = 0
        for file in file_list:
            i +=1 
            dict_data = {}
            # count+=1
            # print("正在处理"+file)
            # 此时拿到所有的csv文件名
            csv_name = os.path.join(path,file)
            # print(csv_name)
            df = pd.read_csv(csv_name,usecols=["Label","Data"])
            data = list(df.get("Data"))
            label = list(df.get("Label"))
            # print(data)
            count+=1
            generate_vector(file,data,label,num,len(file_list),i)

            # print(count)
            
def generate_vector(file,data_list,label_list,num,num_file,j):
    
    pri_ = []
    
    # 循环key值，生成向量
    # print(len(data_list))
    # print(label_list[0])
    for i in range(len(data_list)): 
        # print(len(data_list))
        # print(data_list[127])
        # print(i)
        if i>=15 and i<=496:
            # print(i)
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],\
                data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[i+1]-data_list[i],data_list[i+2]-data_list[i],data_list[i+3]-data_list[i],\
                    data_list[i+4]-data_list[i],data_list[i+5]-data_list[i],data_list[i+6]-data_list[i],data_list[i+7]-data_list[i],data_list[i+8]-data_list[i],data_list[i+9]-data_list[i],data_list[i+10]-data_list[i],data_list[i+11]-data_list[i],data_list[i+12]-data_list[i],data_list[i+13]-data_list[i],data_list[i+14]-data_list[i],data_list[i+15]-data_list[i]])   
            # all_pri.append(pri_)label_list
            # pri_ = []label_list
            # print(i)
            # print(len(pri_[i]))
        elif i==0:
            pri_.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,data_list[1]-data_list[i],data_list[2]-data_list[i],data_list[3]-data_list[i],data_list[4]-data_list[i],data_list[5]-data_list[i],data_list[6]-data_list[i],data_list[7]-data_list[i],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i]])
            # print(i)
            if len(pri_[i])!=30:
                print(i)
            # print(len(pri_[i]))
            # pri_ = []
        elif i==1:
            pri_.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[2]-data_list[i],data_list[3]-data_list[i],data_list[4]-data_list[i],data_list[5]-data_list[i],data_list[6]-data_list[i],data_list[7]-data_list[i],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i]])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
        elif i==2:
            pri_.append([0,0,0,0,0,0,0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[3]-data_list[i],data_list[4]-data_list[i],data_list[5]-data_list[i],data_list[6]-data_list[i],data_list[7]-data_list[i],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==3:
            pri_.append([0,0,0,0,0,0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[4]-data_list[i],data_list[5]-data_list[i],data_list[6]-data_list[i],data_list[7]-data_list[i],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i]])
            if len(pri_[i])!=30:

                print(i)
            
        elif i==4:
            pri_.append([0,0,0,0,0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[5]-data_list[i],data_list[6]-data_list[i],data_list[7]-data_list[i],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==5:
            pri_.append([0,0,0,0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[6]-data_list[i],data_list[7]-data_list[i],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[14]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==6:
            pri_.append([0,0,0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[7]-data_list[i],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i]])    
            if len(pri_[i])!=30:
                print(i)
            
        elif i==7:
            pri_.append([0,0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[8]-data_list[i],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==8:
            pri_.append([0,0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[i]-data_list[7],data_list[9]-data_list[i],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i],data_list[23]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==9:
            pri_.append([0,0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[i]-data_list[7],data_list[i]-data_list[8],data_list[10]-data_list[i],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i],data_list[23]-data_list[i],data_list[24]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==10:
            pri_.append([0,0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[i]-data_list[7],data_list[i]-data_list[8],data_list[i]-data_list[9],data_list[11]-data_list[i],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i],data_list[23]-data_list[i],data_list[24]-data_list[i],data_list[25]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==11:
            pri_.append([0,0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[i]-data_list[7],data_list[i]-data_list[8],data_list[i]-data_list[9],data_list[i]-data_list[10],data_list[12]-data_list[i],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i],data_list[23]-data_list[i],data_list[24]-data_list[i],data_list[25]-data_list[i],data_list[26]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==12:
            pri_.append([0,0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[i]-data_list[7],data_list[i]-data_list[8],data_list[i]-data_list[9],data_list[i]-data_list[10],data_list[i]-data_list[11],data_list[13]-data_list[i],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i],data_list[23]-data_list[i],data_list[24]-data_list[i],data_list[25]-data_list[i],data_list[26]-data_list[i],data_list[27]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==13:
            pri_.append([0,0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[i]-data_list[7],data_list[i]-data_list[8],data_list[i]-data_list[9],data_list[i]-data_list[10],data_list[i]-data_list[11],data_list[i]-data_list[12],data_list[14]-data_list[i],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i],data_list[23]-data_list[i],data_list[24]-data_list[i],data_list[25]-data_list[i],data_list[26]-data_list[i],data_list[27]-data_list[i],data_list[28]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==14:
            pri_.append([0,data_list[i]-data_list[0],data_list[i]-data_list[1],data_list[i]-data_list[2],data_list[i]-data_list[3],data_list[i]-data_list[4],data_list[i]-data_list[5],data_list[i]-data_list[6],data_list[i]-data_list[7],data_list[i]-data_list[8],data_list[i]-data_list[9],data_list[i]-data_list[10],data_list[i]-data_list[11],data_list[i]-data_list[12],data_list[i]-data_list[13],data_list[15]-data_list[i],data_list[16]-data_list[i],data_list[17]-data_list[i],data_list[18]-data_list[i],data_list[19]-data_list[i],data_list[20]-data_list[i],data_list[21]-data_list[i],data_list[22]-data_list[i],data_list[23]-data_list[i],data_list[24]-data_list[i],data_list[25]-data_list[i],data_list[26]-data_list[i],data_list[27]-data_list[i],data_list[28]-data_list[i],data_list[29]-data_list[i]])
            if len(pri_[i])!=30:
                print(i)
            
        # 处理后四个
            
        elif i==497:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[498]-data_list[i],data_list[499]-data_list[i],data_list[500]-data_list[i],data_list[501]-data_list[i],data_list[502]-data_list[i],data_list[503]-data_list[i],data_list[504]-data_list[i],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==498:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[499]-data_list[i],data_list[500]-data_list[i],data_list[501]-data_list[i],data_list[502]-data_list[i],data_list[503]-data_list[i],data_list[504]-data_list[i],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==499:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[500]-data_list[i],data_list[501]-data_list[i],data_list[502]-data_list[i],data_list[503]-data_list[i],data_list[504]-data_list[i],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==500:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[501]-data_list[i],data_list[502]-data_list[i],data_list[503]-data_list[i],data_list[504]-data_list[i],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==501:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[502]-data_list[i],data_list[503]-data_list[i],data_list[504]-data_list[i],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0])
            if len(pri_[i])!=30:
                print(i)
            
        elif i==502:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[503]-data_list[i],data_list[504]-data_list[i],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
           
        elif i==503:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[504]-data_list[i],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==504:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[505]-data_list[i],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==505:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[506]-data_list[i],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==506:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[507]-data_list[i],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==507:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[508]-data_list[i],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==508:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[509]-data_list[i],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==509:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[510]-data_list[i],data_list[511]-data_list[i],0,0,0,0,0,0,0,0,0,0,0,0,0])            # all_pri.append(pri_)
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==510:
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],data_list[511]-data_list[i],0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
        elif i==511:   
            pri_.append([data_list[i]-data_list[i-15],data_list[i]-data_list[i-14],data_list[i]-data_list[i-13],data_list[i]-data_list[i-12],data_list[i]-data_list[i-11],data_list[i]-data_list[i-10],data_list[i]-data_list[i-9],data_list[i]-data_list[i-8],data_list[i]-data_list[i-7],data_list[i]-data_list[i-6],data_list[i]-data_list[i-5],data_list[i]-data_list[i-4],data_list[i]-data_list[i-3],data_list[i]-data_list[i-2],data_list[i]-data_list[i-1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            # print(i)
            # print(len(pri_[i]))
            if len(pri_[i])!=30:
                print(i)
            
    # 首先去除pri<=50和pri>=2500的值
    # print(pri_)
   
    # 此处对每一个向量进行正态分布归一化处理
    # pri = normal_process(pri_)
    # print(len(pri_))
    pri = [data/12500  for pri in pri_ for data in pri]
    all_pri.append(pri)
    all_label.append(label_list)
    # print(all_pri)
    print(file+"pri阈值处理、归一化完成")
    print(file+"生成向量完成")
    print(j)
    if num==0:
        # print("dasd")
        foldername = "all_data_vector_train.csv"
        write_vector_to_file(file,foldername,label_list,pri,1)
    elif num==1:
        foldername = "all_data_vector_test.csv"
        write_vector_to_file(file,foldername,label_list,pri,1)
    elif num==2 :
        foldername = "all_data_vector_val.csv"
        write_vector_to_file(file,foldername,label_list,pri,1)

def max_min(all_pri,all_label):
    all_pri_ = [ pri_ for pri in all_pri for pri_ in pri]
    all_label = [ l for label in all_label for l in label] 
    # print(len(all_pri_))
    all_pri_ = np.array(all_pri_)
    max_ = all_pri_.max()
    min_ = all_pri_.min() 
    all_pri_ = [ (pri-min_)/(max_-min_) for pri in all_pri_]
    print(len(all_pri_))
    return all_pri_,all_label

def normal_process(all_pri,all_label):
    # 第一步先计算一组向量的平均值，然后就算方差，在逐一归一化。
    # average_value = sum(pri_)/len(pri_)
    # 平均值
    mean_ = np.array(all_pri).mean()
    std_ = np.array(all_pri).std()
    all_pri_ = [ (pri_-mean_)/std_ for pri in all_pri for pri_ in pri]
    all_label_ = [l for label in all_label for l in label]
    return all_pri_,all_label_
def write_vector_to_file(file,filename,label_list,data_list,temp):

    if temp==1:
        # if语句中的内容只有在train中使用
        f = open(filename,'a')
        step = 30
        # 还原回原来的格式
        data_list = [ data_list[i:i+step]  for i in range(0,len(data_list),step) ]
        sorted_list = []
        sorted_list_= []
        sorted_list=[sorted(da) for da in data_list]
        # print()
        for s in sorted_list:
            sorted_list_.append([str(da) for da in s])
        num = 0
        data_list_ = []
        label_list_ = []
        for d in data_list:
            # print(sum(d))filename
            # if sum(d)!=0.0:
            data_list_.append(d)
            # print(num)
            label_list_.append(label_list[num])
            num+=1
        # 此时拿到了所有的合格的数据
        # print(len(label_list_))
        final_data_str=[]
        sorted_list = []
        for data in data_list_:
            final_data_str.append([str(da) for da in data])
        con = ','
        for num in range(len(final_data_str)):
            # print(label_list_[num])
            if label_list_[num] == 100:
                label_list_[num] = 0
            else:
                label_list_[num] = 1
            # print(con.join(final_data_str[num]))
            f.write(str(label_list_[num])+","+con.join(final_data_str[num])+"\n")

    
if __name__ == "__main__":

    # read_file_and_get_data('/home/wang/Radar数据/Deinterleaving/data/3/test/',1)
    # read_file_and_get_data('/home/wang/Radar数据/Deinterleaving/data/5/test/',1)
    read_file_and_get_data('/home/wang/Radar数据/Deinterleaving/data/7/test/',1)
    # read_file_and_get_data('/home/wang/Radar数据/Deinterleaving/data/5test/',3)
    # read_file_and_get_data('/home/wang/Radar数据/Deinterleaving/data/5参差/two/',4)
    
    