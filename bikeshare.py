import time
import pandas as pd
import numpy as np
import datetime as dt 
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
    city = input("would you like to see data for Chicago, New York City, or Washington?\n").lower()
    while city not in CITY_DATA:
        city = input("please write valid city from the three cities provided above..\n").lower()
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['Monday', 'Thursday', 'Wednesday', 'Tuesday', 'Saturday', 'Sunday',
       'Friday']
    choice = input("would you like to filter the data by month, day, both, or not at all? Type 'None' for no time filter..\n")
    

    
    # TO DO: get user input for month (all, january, february, ... , june)
    if choice.lower() == "month":
        month = input("Choose a month from Januaray to June:").lower()
        while month not in months:
            month = input("please write valid month from the January to June only..\n").lower()
        month = months.index(month) + 1
        day = None
    
    #  TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif choice.lower() == "day":
        day = input("Choose a day (e.g. monday,tuesday,...):\n").title()
        while day not in days:
            day = input("please write valid day..\n").title()
        month = None
        
    elif choice.lower() == "both":
        month = input("Choose a month from Januaray to June:").lower()
        while month not in months:
            month = input("please write valid month from the January to June only..\n").lower()
        month = months.index(month) + 1
        
        day = input("Choose a day (e.g. monday,tuesday,...):\n").title()
        while day not in days:
            day = input("please write valid day..\n").title()

    elif choice.lower() == "none":
        month = None
        day = None
        
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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    df["months"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["Start hour"] = df["Start Time"].dt.hour
    
    
    if month is not None and day is not None:
        df = df[(df["day_of_week"] == day) & (df["months"] == month)]
    elif month is not None and day is None:
        df = df[df["months"] == month]
    elif day is not None and month is None:
            df = df[df["day_of_week"] == day]
    else:
        pass
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["months"].mode()[0]
    print(f"common month: {common_month}")


    # TO DO: display the most common day of week
    common_weekday = df["day_of_week"].mode()[0]
    print(f"common weekday: {common_weekday}")


    # TO DO: display the most common start hour
    common_hour = df["Start hour"].mode()[0]
    print(f"common starting hour: {common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print(f"common start station: {common_start_station}")


    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f"common end station: {common_end_station}")


    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = "From " + (df['Start Station'] + " To " + df["End Station"]).mode()[0]
    print(f"combination of start station and end station trip: {popular_combination}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["Travel Time"] = df["End Time"] - df["Start Time"]
    total_travel_time = df["Travel Time"].max()
    print(f"total travel time: {total_travel_time}")


    # TO DO: display mean travel time
    mean_travel_time = df["Travel Time"].mean()
    print(f"average travel time: {mean_travel_time}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        subscriber_count = df["User Type"].value_counts()["Subscriber"]
        customer_count = df["User Type"].value_counts()["Customer"]
        print(f"count of Subscriber: {subscriber_count}")
        print(f"count of Customer: {customer_count}")


    # TO DO: Display counts of gender
    
        males_count = df["Gender"].value_counts()["Male"]
        females_count = df["Gender"].value_counts()["Female"]
        print(f"count of males: {males_count}")
        print(f"count of females: {females_count}")
    


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df["Birth Year"].min()
        most_recent = df["Birth Year"].max()
        common_year = df["Birth Year"].mode()[0]
        print(f"earliest birth year: {earliest}")
        print(f"most recent birth year: {most_recent}")
        print(f"common birth year: {common_year}")
        
    except:
        print("something went wrong")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        question = input("Do you want to check the first 5 rows of the dataset related to the chosen city?")
        count = 5
        while question.lower() == "yes":
            print(df.head(count))
            count = count + 5
            question = input("Do you want to check the first 5 rows of the dataset related to the chosen city?")
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
