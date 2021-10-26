import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df=pd.read_csv('adult.data.csv', header=0)
#print(df.head())


#print(df['race'])
#print(pd.Series(pd.Categorical(df['race'])))
    index=pd.Series(pd.Categorical(df['race']))
#print(index.value_counts())
    race_count= index.value_counts()


    Is_Male=df.loc[:,'sex']=='Male'
    Male=df.loc[Is_Male]
#print(pd.Series(pd.Categorical((Male['age'].mean()).round()))[0])
    average_age_men= (pd.Series(pd.Categorical((Male['age'].mean()).round(1)))[0])


    With_Bachelor=df.loc[:,'education']=='Bachelors'
    Bachelor=df.loc[With_Bachelor]
#print(Bachelor)
#print((len(Bachelor.index))*100/(len(df.index)))
    percentage_bachelors= round(((len(Bachelor.index))*100/(len(df.index))),1)
#print(percentage_bachelors)

    higher_education=df[df.education.isin(['Bachelors','Masters','Doctorate'])]
    lower_education=df[~df['education'].isin (['Bachelors', 'Masters', 'Doctorate'])]
#CUIDADIN!! No es lo mismo poner> ~df[].isin que poner df[]!=(a or b or c)
#print(lower_education)
    Is_Rich=higher_education.loc[:,'salary']=='>50K'
    Rich=higher_education.loc[Is_Rich]
    Is_luckyRich=lower_education.loc[:,'salary']== '>50K'
    LuckyRich= lower_education.loc[Is_luckyRich]
#print(Rich)
#print((len(Rich.index)))
#print((len(higher_education.index)))
#print((len(Rich.index))*100/(len(df.index)))
    higher_education_rich= round((len(Rich.index))*100/(len(higher_education.index)),1)
    lower_education_rich= round((len(LuckyRich.index))*100/ (len(lower_education.index)),1)
    #print (lower_education_rich, higher_education_rich)




#print(pd.Series(pd.Categorical(df['hours-per-week'].min())))
    min_work_hours= pd.Series(pd.Categorical(df['hours-per-week'].min()))[0]

    Min_hours= df.loc[:,'hours-per-week']==1
    num_min_workers=df.loc[Min_hours]
#print(num_min_workers)
    Min_Rich= num_min_workers.loc[:,'salary']=='>50K'
    Min_is_Rich= num_min_workers.loc[Min_Rich]
#print(Min_is_Rich)
#print((len(Min_is_Rich.index))*100/(len( num_min_workers.index)))
    rich_percentage= (len(Min_is_Rich.index))*100/(len( num_min_workers.index))


    Richess=df.loc[:,'salary']=='>50K'
    Just_Rich=df.loc[Richess]
#print(Just_Rich)
    earnings= pd.Series(pd.Categorical(df['native-country']))
#print(earnings.value_counts())
    highest_earning=pd.Series(pd.Categorical(Just_Rich['native-country']))
#print(highest_earning.value_counts())
    great_salary_over_salaries=(highest_earning.value_counts()*100/earnings.value_counts()).sort_values(ascending=False)
    highest_earning_country= (great_salary_over_salaries.index.tolist()[0])
    highest_earning_country_percentage = round((highest_earning.value_counts()*100/earnings.value_counts()).max(),1)


    IndianBool=df.loc[:,'native-country']=='India'
    Indian=df.loc[IndianBool]
    Rich_Indian=Indian.loc[:,'salary']== '>50K'
    Is_Rich_Indian=Indian.loc[Rich_Indian]
    Ocup=pd.Series(pd.Categorical(Is_Rich_Indian['occupation']))
    index_ocup=Ocup.value_counts()
    top_IN_occupation=(index_ocup.index.tolist()[0])




    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
