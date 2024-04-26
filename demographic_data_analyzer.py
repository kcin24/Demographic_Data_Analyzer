import pandas as pd


def calculate_demographic_data(print_data=True):

    df = pd.read_csv('adult.data.csv')
    print(df)
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = df['race'].value_counts()
    race_count.values

    # What is the average age of men?
    male = df['sex']== 'Male'
    average_age_men = round(df[male].age.mean(),1)
   

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_count =df[df['education']== 'Bachelors'].count()[0]
    total_count = df['education'].count()
    percentage_bachelors = round(((bachelor_count/total_count) * 100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    advanced_education_df = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    more_than_50k = advanced_education_df[advanced_education_df['salary'] == '>50K']
    higher_education_rich = (more_than_50k.count()[0] / advanced_education_df.count()[0]) * 100
    higher_education_rich = round(higher_education_rich, 1)
    higher_education_rich

    # What percentage of people without advanced education make more than 50K?

    advanced_education_df = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    more_than_50k = advanced_education_df[advanced_education_df['salary'] == '>50K']
    lower_education_rich = (more_than_50k.count()[0] / advanced_education_df.count()[0]) * 100
    lower_education_rich = round(lower_education_rich, 1)
    lower_education_rich

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = None
    #lower_education = None

    # percentage with salary >50K
    # higher_education_rich = None
    #lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    min_work_hours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_value = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_hours = df[df['hours-per-week'] == min_value]
    min_value_salary = df_min_hours[df_min_hours['salary'] == '>50K']
    num_of_people = len(df_min_hours)
    num_of_people_salary_above_50k = len(min_value_salary)
    rich_percentage = (num_of_people_salary_above_50k / num_of_people) * 100
    rich_percentage

    # What country has the highest percentage of people that earn >50K?
    df_salary = df[df['salary'] == '>50K']
    df_salary_country = df_salary['native-country'].value_counts()
    population = df['native-country'].value_counts()
    highest_earning_country_percentage = round(((df_salary_country / population) *100),1)
    max = highest_earning_country_percentage.max()
    highest_earning_country = highest_earning_country_percentage.index[highest_earning_country_percentage == max].to_list()[0]
    highest_earning_country 
    highest_earning_country_percentage = round(max, 1)
  

    # Identify the most popular occupation for those who earn >50K in India.
    df_salary = df[df['salary'] == '>50K']
    df_salary_country = df_salary['native-country'].value_counts()
    df_salary_India = df_salary[df_salary['native-country'] == 'India']
    df_occupation= df_salary_India['occupation'].value_counts()
    max = df_occupation.max()
    top_IN_occupation = df_occupation.index[df_occupation == max].to_list()[0]
    top_IN_occupation
    

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
