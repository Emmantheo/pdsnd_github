#List of the links I used as guidance in this project
#https://www.analyticsvidhya.com/blog/2020/05/datetime-variables-python-pandas/
#https://www.geeksforgeeks.org/python-pandas-series-dt-date/
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
#https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week

#time to import important folders

import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['chicago', 'new york city', 'washington']
    while True:
       city = input("What city do you want to analyse?\n").lower()
       if city not in city_list:
           print("invalid input; try again\n")
           continue
       else:
           break
    month_list=['january', 'february', 'march', 'april', 'may','june','all']
    while True:
        month = input("What month?\n").lower() #getting input for months
        if month not in month_list:
            print("wrong month; try again\n")
            continue
        else:
            break
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input ("What day of the week?\n").lower() #getting input for days of the week
        if day not in day_list:
            print("incorrect; enter the right day \n")
            continue
        else:
            break

    print('-'*40)
    return city, month, day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    df = pd.read_csv(CITY_DATA[city])
#converting the start_time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
#create month,day of the week and hour from start_time column
    df['month'] = df['Start Time'].dt.month #for month
    df['day_of_week'] = df['Start Time'].dt.day_name() #day of the week
    df['hour'] = df['Start Time'].dt.hour #hour
#filtering by months
    if month!='all':
        #use the index of the month list to get the corresponding int
          month_list= ['january','february','march','april','may','june']
          month=month_list.index(month)+1

        # filter by month to create the new dataframe
          df = df[df['month'] == month]

    if day != 'all':

         df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time)) #time taken for code to run
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_commonly_used_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_commonly_used_start_station)
    # TO DO: display most commonly used end station
    most_commonly__used_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_commonly__used_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(most_frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time)) #time taken for code to run
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given fitered data is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time)) #time taken for code to run
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given fitered data is: \n",  str(user_types))

    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n", gender)

        # TO DO: Display earliest, most recent, and most common year of birth

        birth_year = df['Birth Year']
        #To display the earlier year of birth
        earliest_year = birth_year.min()
        print('The earliest birth from the given data is: \n', int(earliest_year))
        #To display the most recent year of birth
        most_recent_birth = birth_year.max()
        print('The most recent birth from the given data is: \n', int(most_recent_birth))
        #To display the most common year of birth
        most_common_birth = birth_year.value_counts().idxmax()
        print('The most common birth from the given data is: \n', int(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time)) #time taken for code to run
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\n Would you prefer to view next five row of raw data? Enter yes or no.\n').lower()
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you prefer to view first five row of raw data? Enter yes or no.\n').lower()
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
