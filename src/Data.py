import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import scipy 
import random
import time

# Create an Array of N Datetimes Between Two Dates
def random_dates(start, end, n, unit='D', seed=None):
    if not seed:  # from piR's answer
        np.random.seed(0)
    ndays = (end - start).days + 1
    return pd.to_timedelta(np.random.rand(n) * ndays, unit=unit) + start

# Surveys
Surveys = pd.DataFrame({'survey_id' : np.arange(1,40001),
'survey_overall_score' : random.choices([1,2,3,4,5], [2000,5000,20000,8000,5000],k=40000),
'survey_waiting_score' : random.choices([1,2,3,4,5], [2000,5000,20000,7000,6000],k=40000)  })
Surveys.to_csv('Surveys.csv', index=False)

# Scores 
Scores = pd.DataFrame({'ed_score_id' : np.arange(1,100001) ,
'APACHE_II_score' : list(np.repeat(np.arange(1,10),1000)) + list(np.repeat(np.arange(11,50),2000)) + list(np.repeat(np.arange(51,71),650)),
'ESI_score' : [1]*10000 +  [2]*40000 + [3]*40000 + [4]*5000 + [5]*5000 })
Scores.to_csv('Scores.csv', index=False)

# Patients
Patients = pd.DataFrame({'patient_id': np.arange(1,70001) ,
'atient_age' : np.random.gamma(50, 1, 70000),
'patient_lat' : random.choices([float('40.' + str(i)) for i in range(745,792)], k=70000),
'patient_long' : random.choices([float('-73.' + str(i)) for i in range(663,731)], k=70000),
'patient_race' : random.choices(['white','black','asian','native/oceanic',
                               'mixed race', 'patient declined'], [50000,10000,8000,500,1000,500], k=70000),
'patient_homeless' : random.choices(['No','Yes'], [98,2],k=70000) })
Patients.to_csv('Patients.csv', index=False)

# Staff on per Visit
Provider_Visits = pd.DataFrame({'visit_id' : list(np.arange(1,1000001)) * 6 ,
'provider_id' : random.choices(random.choices(np.arange(1,10),k=2) + random.choices(np.arange(11,50),k=4), k=6000000)})
Provider_Visits.to_csv('Provider_Visits.csv', index=False)

# Providers
Providers = pd.DataFrame({'provider_id' : np.arange(1,51),
'provider_role' : ['MD']*5 + ['PA']*5 + ['RN']*40 })
Providers.to_csv('Providers.csv', index=False)

# Referrals
Referrals = pd.DataFrame({'referral_id' : np.arange(1,40001) ,
'referral_name' : random.choices(['Primary Care','Orthopedics', 'Neurology', 'Addiction Medicine', 
                                'Gastroenterology', 'Cardiology'], [15000,10000,5000,1000,4000,5000], k=40000) })
Referrals.to_csv('Referrals.csv', index=False)

# Referral Benchmarks per Year
Referral_Benchmarks = pd.DataFrame({'referral_benchmark_id' : np.arange(1,19),
'referral_name' : ['Primary Care','Orthopedics', 'Neurology', 'Addiction Medicine', 'Gastroenterology', 'Cardiology'] * 3,
'referral_report_date' : ['2021']*6 + ['2022']*6 + ['2023']*6 ,
'referral_pct' : [0.375, 0.27, 0.125, 0.005, 0.1, 0.125,0.395, 0.25, 0.125, 0.004, 0.1, 0.126,0.385, 0.29, 0.121, 0.003, 0.1, 0.101] })
Referral_Benchmarks.to_csv('Referral_Benchmarks.csv', index=False)


# ED Visits with FKs
ED_Visits = pd.DataFrame(
    {
'visit_id' : np.arange(1,100001) ,
'ed_score_id' : np.arange(1,100001),
'survey_id' : np.arange(1,100001) , # convert all > 40000 to np.nan
'referral_id' : np.arange(1,100001) , # convert all > 40000 to np.nan   
'patient_id' : random.choices(np.arange(1,700001) , k=100000),
'arrival_dt' :  random_dates(pd.to_datetime('2021-01-01'), pd.to_datetime('2024-01-01'), n=100000) ,  
'admitted' : random.choices(['No', 'Yes'], weights=[70,30], k=100000)
    }
)
ED_Visits.loc[ED_Visits.referral_id > 40000, 'referral_id' ] = np.nan
ED_Visits.loc[ED_Visits.survey_id > 40000, 'survey_id' ] = np.nan
ED_Visits['patient_seen_dt'] = ED_Visits['arrival_dt'] + pd.to_timedelta(np.random.gamma(50, 1,len(ED_Visits['arrival_dt']))
                                                                         ,unit='minutes')
ED_Visits['admission_dt'] = np.where(ED_Visits['admitted'] == 'Yes', ED_Visits['patient_seen_dt']+ pd.to_timedelta(np.random.gamma(50, 1,len(ED_Visits['arrival_dt']))
                                                                         ,unit='minutes'), ED_Visits['patient_seen_dt'])
ED_Visits.to_csv('ED_Visits.csv', index=False)
