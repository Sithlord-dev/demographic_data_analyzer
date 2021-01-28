import pandas as pd


def calculate_demographic_data(print_data=True):
    
    # Reading data from file
    df = pd.read_csv('adult.data.csv', na_values = ['?'])

    # Races represented in the dataset
    race_count = race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # Percentage of people who have a Bachelor's degree
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].size / df.size * 100,1)

    # Percentage of people:
    ## with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    lower_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]

    ## Percentage with salary >50K
    higher_education_rich = round(higher_education[(higher_education['salary'] == '>50K')].size / higher_education.size * 100,1)
    lower_education_rich = round(lower_education[(lower_education['salary'] == '>50K')].size / lower_education.size ,1)

    # The minimum number of hours a person works per week 
    min_work_hours = df['hours-per-week'].min()

    # Percentage of the people who work the minimum number of hours per week have a salary of >50K
    num_min_workers = num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K'].size / num_min_workers.size

    # Country with the highest percentage of people that earn >50K
    rich_country = df['native-country'][df['salary'] == '>50K'].value_counts()
    highest_earning_country = round(rich_country / df['native-country'].value_counts() * 100,2).idxmax()
    highest_earning_country_percentage = round(rich_country / df['native-country'].value_counts() * 100,2).max()

    # The most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().idxmax()


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
