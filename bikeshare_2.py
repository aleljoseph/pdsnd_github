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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    c = (input ('Type the name of the city to analyze: '))
    c = c.lower()
    while c not in ['chicago', 'new york city', 'washington']:
        c = (input('I´m not sure what city you want to analyze, please try again: '))




    # get user input for month (all, january, february, ... , june)
    m = input ('Type the name of the month to filter by, or "all" to apply no month filter: ')
    m = m.lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    d = input ('Finally type the name of the day of week to filter by, or "all" to apply no day filter: ')
    d = d.lower()

    print('-'*40)
    return c, m, d


def load_data(c, m, d):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[c].lower())

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if m.lower() != 'all':
        ms = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        m = ms.index(m) + 1
        df = df[df['month'] == m]

    if d.lower() != 'all':
        df = df[df['day_of_week'] == d.title()]

    df.fillna(0)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is {}. \n'.format(popular_month))

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is {}. \n'.format(popular_day_of_week))

    # display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('The most common start hour is {}. \n'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}. \n'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}. \n'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    start_to_end = df['Start Station'].astype(str) + 'to' + df['End Station'].astype(str)
    popular_combination_start_end_stations = start_to_end.mode()[0]
    print('The most commonly combination of start and end station trip is {}. \n'.format(popular_combination_start_end_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {}. \n'.format(total_travel_time))

    # display mean travel time
    mean_total_travel_time = df['Trip Duration'].mean()
    print('The mean of the total travel time is {}. \n'.format(mean_total_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, c):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type Count /n')
    print('{}'.format(user_types))

    # Display counts of gender
    if c != 'washington':
        gender = df['Gender'].value_counts()
        print('Gender Count /n')
        print('{}'.format(gender))

    # Display earliest, most recent, and most common year of birth
    if c != 'washington':
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('The earliest birth of year is {}, the most recent birth of year is {} and the most common birth year is {}'.format(earliest_year_of_birth, most_recent_year_of_birth, most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view_data = input('\nWould you like to view the first 5 rows of individual trip data? \nEnter yes or no\n').lower()
    start_loc = 0
    while view_data:
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_display = input('Do you wish to continue?: ').lower()
        if view_display == 'no':
            view_data = False


def main():
    while True:
        c, m, d = get_filters()
        df = load_data(c, m, d)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, c)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
