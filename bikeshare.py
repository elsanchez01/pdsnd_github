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
    select_city = True
    while select_city:
        city = input('Please select a city: Chicago, New York City or Washington: ').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            select_city = False
        else:
            print('Invalid choice')


    # TO DO: get user input for month (all, january, february, ... , june)
    select_month = True
    while select_month:
        month = input('Please select a month from January to June or all: ').lower()
        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
            select_month = False
        else:
            print('Invalid choice!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    select_day = True
    while select_day:
        day = input('Please select a day from Monday to Sunday or all: ').lower()
        if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday'                   or day == 'all':
            select_day = False
        else:
            print('Invalid choice!')



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
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

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
    popular_month = df['month'].mode()[0]
    print('The most common month is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', popular_day)

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_and_end_station = df[['Start Station','End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip are: {} and {}'.format(popular_start_and_end_station[0],                       popular_start_and_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('Counts of user type: ', user_types_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        counts_of_gender = df['Gender'].value_counts()
        print('Counts of gender: ',counts_of_gender)
    else:
        print('\nGender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('\nEarliest year of birth: {}\nMost recent year of birth: {}\nMost common year of birth: {}\n'.format(earliest_birth, recent_birth, common_birth))
    else:
        print('\nBirth Year stats cannot be calculated because Birth Year does not appear in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays 5 rows of data if user request it"""
    select_answer = True
    while select_answer:
        view_data = input("Would you like to view 5 rows of individual trip  data? Enter yes or no? ".lower())
        if view_data != 'yes':
            select_answer = False
        else:
            start_loc = 0
            while True:
                print(df.iloc[start_loc:start_loc + 5])
                start_loc += 5
                view_display = input("Do you wish to continue?: ").lower()
                if view_display != 'yes':
                    select_answer = False
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
