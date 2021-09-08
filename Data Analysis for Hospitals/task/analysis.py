import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# write your code here
pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

table = pd.concat([general, prenatal, sports], ignore_index=True)

table.drop(columns='Unnamed: 0', inplace=True)

table.dropna(axis=0, how='all', inplace=True)
# table.to_csv('table.csv')

table['gender'].replace('male', 'm', inplace=True)
table['gender'].replace('female', 'f', inplace=True)
table['gender'].replace('man', 'm', inplace=True)
table['gender'].replace('woman', 'f', inplace=True)

table['gender'].fillna('f', inplace=True)

table['bmi'].fillna(0, inplace=True)
table['diagnosis'].fillna(0, inplace=True)
table['blood_test'].fillna(0, inplace=True)
table['ecg'].fillna(0, inplace=True)
table['ultrasound'].fillna(0, inplace=True)
table['mri'].fillna(0, inplace=True)
table['xray'].fillna(0, inplace=True)
table['children'].fillna(0, inplace=True)
table['months'].fillna(0, inplace=True)

# table.to_csv('table.csv')

interval1 = table.loc[(table['age'] > 0) & (table['age'] < 15)].shape[0]
interval2 = table.loc[(table['age'] > 15) & (table['age'] < 35)].shape[0]
interval3 = table.loc[(table['age'] > 35) & (table['age'] < 55)].shape[0]
interval4 = table.loc[(table['age'] > 55) & (table['age'] < 70)].shape[0]
interval5 = table.loc[(table['age'] > 70) & (table['age'] < 80)].shape[0]
maxVal = max(interval1, interval2, interval3, interval4, interval5)
text = ''
if maxVal == interval1:
    text = '0 - 15'
elif maxVal == interval2:
    text = '15 - 35'
elif maxVal == interval3:
    text = '35 - 55'
elif maxVal == interval4:
    text = '55 - 70'
elif maxVal == interval5:
    text = '70 - 80'

print('The answer to the 1st question: {}'.format(text))

table.plot(y='age', kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.show()

print('The answer to the 2nd question: {}'.format(table['diagnosis'].mode()[0]))
table['diagnosis'].value_counts().plot(kind='pie')
plt.show()

sns.set_theme(style="whitegrid")
sns.violinplot(x=table["height"])
plt.show()
print("The answer to the 3rd question: It's because the large values")


