###Function-1 

def preprocess_indiv_burner_PTET_no_SULFreq(df):
    df_c = df.copy(deep=True)
    df_c.columns = df_c.columns+'_'+df_c.iloc[0,:]+ '_'+df_c.iloc[1,:]
    #drop the date
    SGT750 = df_c.iloc[2:,1:]
    #Change the index to sequence
    SGT750.index = range(1,SGT750.shape[0]+1)
#     check na values
    nalist  = [x for x in SGT750.isna().sum() if x>0]
    if not(nalist):
        print("No na values")
    else:
    #drop na values
        SGT750 = SGT750.dropna()
    return(SGT750)


###Function - 2
def modifydata2(SGT750):
    datay = SGT750.filter(regex='Flame')
    Burner1 = SGT750.loc[:,[datay.columns[0],'MBM10CP005_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP005_XE02_Low Frequency Pulsation_mbar','MBM10CP005_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP005_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 1_Avg']]
    Burner2 = SGT750.loc[:,[datay.columns.values[1],'MBM10CP010_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP010_XE02_Low Frequency Pulsation_mbar','MBM10CP010_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP010_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 2_Avg']]
    Burner3 = SGT750.loc[:,[datay.columns.values[2],'MBM10CP015_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP015_XE02_Low Frequency Pulsation_mbar','MBM10CP015_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP015_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 3_Avg']]
    Burner4 = SGT750.loc[:,[datay.columns.values[3],'MBM10CP020_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP020_XE02_Low Frequency Pulsation_mbar','MBM10CP020_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP020_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 4_Avg']]
    Burner5 = SGT750.loc[:,[datay.columns.values[4],'MBM10CP025_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP025_XE02_Low Frequency Pulsation_mbar','MBM10CP025_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP025_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 5_Avg']]
    Burner6 = SGT750.loc[:,[datay.columns.values[5],'MBM10CP030_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP030_XE02_Low Frequency Pulsation_mbar','MBM10CP030_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP030_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 6_Avg']]
    Burner7 = SGT750.loc[:,[datay.columns.values[6],'MBM10CP035_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP035_XE02_Low Frequency Pulsation_mbar','MBM10CP035_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP035_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 7_Avg']]
    Burner8 = SGT750.loc[:,[datay.columns.values[7],'MBM10CP040_XE01_Ultra Low Frequency Pulsation_mbar',
                            'MBM10CP040_XE02_Low Frequency Pulsation_mbar','MBM10CP040_XE03_Medium Frequency Pulsation_mbar',
                            'MBM10CP040_XE04_High Frequency Pulsation_mbar',
                            'MBB10FT923_ZE11_T7 Exhaust Temp Average Ring1_°C','MBB10FT923_ZE12_T7 Exhaust Temp Average Ring 2_°C',
                            'MBB10FT923_ZE13_T7 Exhaust Temp Average Ring 3_°C','Powerturbine Inlet Temp 8_Avg']]
    datalist = [Burner1,Burner2,Burner3,Burner4,Burner5,Burner6,Burner7,Burner8]
    dfcols = ['BurnerStatus','UltraLow_Frequency','Low_Frequency','Medium_Frequency','High_Frequency','TempRing1','TempRing2','TempRing3','T_6']
    for dc in datalist:
        dc.columns = dfcols
    return(datalist)