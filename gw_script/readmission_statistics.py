import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_csv(filepath):
    admissions = pd.read_csv(filepath + 'ADMISSIONS.csv')
    return admissions


def get_admission_count_by_religion(admissions, religion_list):
    for rel in religion_list:
        admissions_sub = admissions.loc[admissions['RELIGION'] == rel]
        fig2 = plt.figure(figsize=(6, 6))
        admissions_sub.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
        plt.title('Distribution of admission counts for ' + rel + ' patients')
        plt.ylabel('')
        fig2.savefig('admission_count_freq_' + rel + '.png')


def get_admission_count_by_admissiontype(admissions, admission_type_list):
    for type in admission_type_list:
        admissions_sub = admissions.loc[admissions['ADMISSION_TYPE'] == type]
        fig2 = plt.figure(figsize=(6, 6))
        admissions_sub.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
        plt.title('Distribution of admission counts for ' + type + ' patients')
        plt.ylabel('')
        fig2.savefig('admission_count_freq_' + type + '.png')


def main():
    file_path = './'
    admissions = read_csv(file_path)

    # print(admissions.shape)
    print(admissions.head(5))
    # fig = plt.figure(figsize=(11, 11))
    # admissions.MARITAL_STATUS.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    # plt.title('Marital status vs all-admissions')
    # plt.ylabel('')
    # fig.savefig('marital_status_all.png')

    admissions['freq'] = admissions.groupby('SUBJECT_ID')['SUBJECT_ID'].transform('count')

    fig1 = plt.figure(figsize=(6, 6))
    admissions.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    plt.title('Distribution of admission counts per patient')
    plt.ylabel('')
    fig1.savefig('admission_count_freq.png')

    admissions_married = admissions.loc[admissions['MARITAL_STATUS'] == 'MARRIED']
    fig2 = plt.figure(figsize=(6, 6))
    admissions_married.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    plt.title('Distribution of admission counts for married patients')
    plt.ylabel('')
    fig2.savefig('admission_count_freq_married.png')

    admissions_divorced = admissions.loc[admissions['MARITAL_STATUS'] == 'DIVORCED']
    fig3 = plt.figure(figsize=(6, 6))
    admissions_divorced.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    plt.title('Distribution of admission counts for divorced patients')
    plt.ylabel('')
    fig3.savefig('admission_count_freq_divorced.png')

    admissions_widowed = admissions.loc[admissions['MARITAL_STATUS'] == 'WIDOWED']
    fig4 = plt.figure(figsize=(6, 6))
    admissions_widowed.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    plt.title('Distribution of admission counts for widowed patients')
    plt.ylabel('')
    fig4.savefig('admission_count_freq_widowed.png')

    admissions_separated = admissions.loc[admissions['MARITAL_STATUS'] == 'SEPARATED']
    fig4 = plt.figure(figsize=(6, 6))
    admissions_separated.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    plt.title('Distribution of admission counts for separated patients')
    plt.ylabel('')
    fig4.savefig('admission_count_freq_separated.png')

    admissions_lifepartner = admissions.loc[admissions['MARITAL_STATUS'] == 'LIFE PARTNER']
    fig4 = plt.figure(figsize=(6, 6))
    admissions_lifepartner.freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    plt.title('Distribution of admission counts for life-partner patients')
    plt.ylabel('')
    fig4.savefig('admission_count_freq_lifepartner.png')

    ### religion
    fig = plt.figure(figsize=(11, 11))
    # admissions.RELIGION.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    admissions.RELIGION.value_counts().plot.bar()
    plt.title('Religion vs all-admissions')
    plt.ylabel('')
    fig.savefig('religion_bar_all.png')

    religion_list = ['CATHOLIC', 'NOT SPECIFIED', 'PROTESTANT QUAKER', 'JEWISH', 'BUDDHIST', 'HINDU', 'MUSLIM']
    get_admission_count_by_religion(admissions, religion_list)

    ### admission_type
    fig = plt.figure(figsize=(11, 11))
    # admissions.RELIGION.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    admissions.ADMISSION_TYPE.value_counts().plot.bar()
    plt.title('ADMISSION_TYPE vs all-admissions')
    plt.ylabel('')
    fig.savefig('ADMISSION_TYPE_bar_all.png')

    admission_type_list = ['EMERGENCY', 'NEWBORN', 'ELECTIVE', 'URGENT']
    get_admission_count_by_admissiontype(admissions, admission_type_list)

    admissions_deadDF = admissions.loc[admissions['DEATHTIME'] != 'NaN']
    admissions_deadDF['dead_admi_freq'] = admissions_deadDF.groupby('SUBJECT_ID')['SUBJECT_ID'].transform('count')
    fig4 = plt.figure(figsize=(6, 6))
    admissions_deadDF.dead_admi_freq.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    plt.title('Distribution of admission counts for dead patients')
    plt.ylabel('')
    fig4.savefig('dead_admission_count_freq.png')

    # admissions_once = admissions.loc[admissions['freq'] == 1]
    # fig2 = plt.figure(figsize=(11, 11))
    # admissions_once.MARITAL_STATUS.value_counts().plot.pie(startangle=45, autopct='%1.0f%%')
    # plt.title('Marital status vs single-admissions')
    # plt.ylabel('')
    # fig2.savefig('marital_status_single.png')

    
if __name__ == "__main__":
    main()
