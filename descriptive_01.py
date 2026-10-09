import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r"C:\Users\priya\Downloads\Population_Survey_Data_lyst1750274390196.csv")
print(data.head())
#SIMPLE RANDOM SAMPLING 
sample_data=data.sample(n=10,random_state=30)
print(sample_data)

# # STRATIFIED SAMPLING
# print(data['Region'].value_counts())
# # satisfied_sampling=data.groupby('Region').apply(lambda x: x.sample(25,random_state=1)).reset_index(drop=True)
# satisfied_sampling = data.groupby('Region', group_keys=False).apply(lambda x: x.sample(min(len(x),25)))
# print(satisfied_sampling.to_csv('STRATIFIED SAMPLING.csv'))

# # CLUSTERING SAMPLING : manufacturing data by batch number
# manufacturing_data=pd.read_csv(r"C:\Users\priya\Downloads\Manufacturing_Data_lyst1750274395200.csv")
# print(manufacturing_data.head())
# cluster=manufacturing_data['BatchNumber'].unique()
# print(cluster)
# '''[25 45 20 31 14  8 36 30 21  9 11 42 35 47 12 22  5 48 23  7 44 33 38  4
#  18  6 28  2 34 41 40 19 16 46 49 43 17  3 13 10 29 32 24 26 39 15  1 27
#  37]'''
# #Now we will randomly select 5 clusters  based on above result 
# selected_clusters = np.random.choice(cluster,size=5,replace= False)
# print(selected_clusters)
# #[25  8 37  5 21]
# final_result=manufacturing_data[manufacturing_data['BatchNumber'].isin(selected_clusters)]
# print(final_result)

# # SYSTEMATIC SAMPLING
# systematic_sampling=data.iloc[: : 10, :]
# print(systematic_sampling)

# # HOMEWORKK TASK 
# ''' Measure of central tendency (mean,median,mode) for the whole data followed by the all sampling technique
# Compare the mean of all diffferent types of the sample and finally conclude which specific sampling technique 
# mean value is almost similar to the population mean value  '''
# # Mean for whole data 
# print(data)
# whole_mean=np.mean(data['Income'])
# print(f"The mean of the data is {whole_mean}")
# #Median for whole data
# whole_median=np.median(data["Income"])
# print(f'The median for whole data is {whole_median}')
# # mode of the data 
# whole_mode=data['Income'].mode()
# print(f'The mode of the data is {whole_mode} ')
# # catche=data['Income'].unique()
# # print(catche)
# # Now by using sampling technique to find the all three

# #                          Random sampling 

# sample_data=data.sample(n=10,random_state=30)
# # print(sample_data)
# sample_mean=np.mean(sample_data['Income'])
# print(f'The mean of random sampling is {sample_mean}')

# sample_median=np.median(sample_data['Income'])
# print(f'The median of random sampling is {sample_median}')

# sample_mode=sample_data['Income'].mode()
# print(f'The mode of random sampling is {sample_mode}')

# #               stratified sampling 
# # satisfied_sampling = data.groupby('Region', group_keys=False).apply(lambda x: x.sample(min(len(x),25)))
# # print(satisfied_sampling.to_csv('STRATIFIED SAMPLING.csv'))
# stratified_mean=np.mean(satisfied_sampling['Income'])
# print(f"The mean of stratified sampling is {stratified_mean}")

# stratified_median=np.median(satisfied_sampling['Income'])
# print(f"The median of stratified sampling is {stratified_median}")

# stratified_mode=satisfied_sampling['Income'].mode()
# print(f"The mode of stratified sampling is {stratified_mode}")

# # cluster sampling 
# # cluster=manufacturing_data['BatchNumber'].unique()
# # print(cluster)
# '''[25 45 20 31 14  8 36 30 21  9 11 42 35 47 12 22  5 48 23  7 44 33 38  4
#  18  6 28  2 34 41 40 19 16 46 49 43 17  3 13 10 29 32 24 26 39 15  1 27
#  37]'''
# # #Now we will randomly select 5 clusters  based on above result 
# # selected_clusters = np.random.choice(cluster,size=5,replace= False)
# # print(selected_clusters)
# #[25  8 37  5 21]