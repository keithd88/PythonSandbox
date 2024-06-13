# %%
import pandas as pd
import numpy as np
df = pd.read_csv('eyetracker.log')  # import data log
df

# %%
# Step 1: AOI cleanup
AOIvalues = [0, 2, 3]  # acceptable AOI values
validAOI = df['AOI'].isin(AOIvalues)
df.loc[~validAOI, 'AOI'] = -1  # replace all non-acceptable values with AOI of -1
df

# %%
# Step 2: Validity Check
Validity_left = df['Validity_left'].isin(['Valid'])  # acceptable Validity values
Validity_right = df['Validity_right'].isin(['Valid'])  # acceptable Validity values
Type = df['Type'].isin(['Fixation', 'Saccade'])  # acceptable Type values
df.loc[~Validity_left, 'AOI'] = -1  # replace all non-acceptable values with AOI of -1
df.loc[~Validity_right, 'AOI'] = -1
df.loc[~Type, 'AOI'] = -1
df

# %%
# Step 2 continued
Valid_Data = df['AOI'].isin(AOIvalues)
df['Data_Validity'] = Valid_Data  # adding new column for validity
df.head(10)

# %%
# Step 3 prep
df['Timestamp'] = df['Timestamp'] - df['Timestamp'].min()  # set 1st timestamp to zero for readability
df

# %%
# Step 3: Finding total durations
Fix_pts = df.loc[df['Type'] == 'Fixation']  # Fixation points
Sac_pts = df.loc[df['Type'] == 'Saccade']  # Saccade points
Valid_pts = df['Data_Validity']  # Valid time points
Invalid_pts = ~df['Data_Validity']  # Invalid time points
FRV_pts = df.loc[df['AOI'] == 2]  # FRV AOI points
Phone_pts = df.loc[df['AOI'] == 3]  # Phone AOI points
Fix_time = Fix_pts['Duration'].sum()  # finding duration for each condition
Sac_time = Sac_pts['Duration'].sum()
Valid_time = df.loc[Valid_pts, 'Duration'].sum()
Invalid_time = df.loc[Invalid_pts, 'Duration'].sum()
FRV_time = FRV_pts['Duration'].sum()
Phone_time = Phone_pts['Duration'].sum()
durations = {"Fixation": [Fix_time], "Saccade": [Sac_time], "Valid": [Valid_time], "Invalid": [Invalid_time],"FRV": [FRV_time], "Phone": [Phone_time]}  # creating array for new DF
df_time = pd.DataFrame(durations)  # create new DF for storing duration
df_time.to_csv('Solutions/Step_3_Durations.txt', index_label='Index')
df_time  # print DF to confirm values

# %%
# Step 4: Data Quality Check
Timestamp_duration = ((df['Timestamp']-(df['Timestamp'].shift()).fillna(0))/1000).round(0)  # create series of timestamp duration to compare and round to nearest integer
Timestamp_duration = Timestamp_duration.shift(periods=-1)  # shift series to match our data
Time_dif = pd.Series(np.where(df['Duration'] == Timestamp_duration, False, True))  # compare calculated vs recorded duration
df.loc[Time_dif, 'Data_Validity'] = False  # mark as invalid if durations don't match
df['Duration'] = Timestamp_duration  # store correct duration
df

# %%
# Step 5: Reduction of Duplicate Invalid Data
#df.drop_duplicates(subset='Data_Validity')
#Id = df.loc[df['Data_Validity'] == False]  # pull out all Invalid data points
#Id.loc[Id['Index'].shift() != Id['Index']]
#Id[~(Id.loc[:,'Data_Validity'] == Id.loc[:,'Data_Validity'].shift()).all(axis=1)].reset_index(drop=True)  # trying to delete only consecutive duplicates

# %%
# Step 6: Finding updated total durations
Fix_pts = df.loc[df['Type'] == 'Fixation']  # Fixation points
Sac_pts = df.loc[df['Type'] == 'Saccade']  # Saccade points
Valid_pts = df['Data_Validity']  # Valid time points
Invalid_pts = ~df['Data_Validity']  # Invalid time points
FRV_pts = df.loc[df['AOI'] == 2]  # FRV AOI points
Phone_pts = df.loc[df['AOI'] == 3]  # Phone AOI points
Fix_time = Fix_pts['Duration'].sum()  # finding duration for each condition
Sac_time = Sac_pts['Duration'].sum()
Valid_time = df.loc[Valid_pts, 'Duration'].sum()
Invalid_time = df.loc[Invalid_pts, 'Duration'].sum()
FRV_time = FRV_pts['Duration'].sum()
Phone_time = Phone_pts['Duration'].sum()
durations = {"Fixation": [Fix_time], "Saccade": [Sac_time], "Valid": [Valid_time], "Invalid": [Invalid_time],"FRV": [FRV_time], "Phone": [Phone_time]}  # creating array for new DF
df_time = pd.DataFrame(durations)  # create new DF for storing duration
df_time.to_csv('Solutions/Step_6_Durations.txt', index_label='Index')
df_time  # print DF to confirm values

# %%
# Step 7: Validity
Validity_ratio = (df['Data_Validity'].value_counts(normalize=True)*100).round(1)  # find % of false/true data points by normalizing
Valid_dur = (df.loc[df['Data_Validity'] == True])['Duration'].sum()  # find total time of valid duration
Duration_ratio = (Valid_dur/df['Duration'].sum()*100).round(1)  # find ratio of valid duration to total duration

Valid_perc = pd.DataFrame({"Valid Data %": [Validity_ratio[1]], "Duration Validity %": [Duration_ratio]}) #create new DF to store outputs
Valid_perc.to_csv('Solutions/Step_7_Validity_Percentages.txt', index_label='Index')
Valid_perc

# %%
df.to_csv('Solutions/Final_Data_Log.csv', index_label='Index')  # export final modified data log

# %%



