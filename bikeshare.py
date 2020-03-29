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
    while(True):
        city = input("\nENTER CITY NAME: ")
        city = city.lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("\n*****Please check your input and type either new york city or chicago or washington*****")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
            month=input("ENTER MONTH: ")
            month=month.lower()
            if month not in('january', 'february', 'march', 'april', 'may','june', 'all'):
               print("\n*****Please check your input and enter either all or any month between january and june*****\n")
            else:
                break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
        day=input("Enter day: ")
        day=day.lower()
        if day not in('sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'all'):
            print("\n*****OOPS! Please enter either all or any day in the week*****")
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print("Most common month: ",popular_month)

    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print("Most common day: ",popular_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print("Most common hour: ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].value_counts().mode()[0]
    print("Most commonly used start station: ",start_station)

    # TO DO: display most commonly used end station
    end_station=df['End Station'].value_counts().mode()[0]
    print("Most commonly used end station: ",end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_combination = df['Combination'].value_counts().mode()[0]
    print('\nMost Commonly used combination of start station and end station trip:', popular_combination)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time=df['Trip Duration'].sum()
    print("Total travel time: ",Total_travel_time)

    # TO DO: display mean travel time
    Mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time: ",Mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_statistics(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types:\n",user_types)

    # TO DO: Display counts of gender
    print("\nPrinting GENDER AND BIRTH INFO for NYC and Chicago because Washington doesn't have Gender listed\n")
    try:
        Gender_types=df['Gender'].value_counts()
        print("Gender Types:\n",Gender_types)

    except KeyError:
        print("NO DATA LISTED FOR THIS SELECTION :(\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_year)
    except KeyError:
      print("\nEarliest Year: NO DATA LISTED FOR THIS SELECTION :(")

    try:
      Most_recent_year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_recent_year)
    except KeyError:
      print("\nMost Recent Year: NO DATA LISTED FOR THIS SELECTION :(")

    try:
      Most_common_year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_common_year)
    except KeyError:
      print("\nMost Common Year: NO DATA LISTED FOR THIS SELECTION :(")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual(df):
        start,end=0,5
        print(df.iloc[start:end])
        start+=5
        end+=5

        #calling main function

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_statistics(df)
        individual(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
