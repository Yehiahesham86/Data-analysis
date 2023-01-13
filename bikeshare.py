import time
import pandas as pd

# import numpy as np

CITY_DATA = {'chicago': 'F:/Data Analysis/2-Professional Level/project/all-project-files/chicago.csv',
             'new york city': 'F:/Data Analysis/2-Professional Level/project/all-project-files/new_york_city.csv',
             'washington': 'F:/Data Analysis/2-Professional Level/project/all-project-files/washington.csv'}
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = ['all', 'saturday ', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs
    while True:
        city = input("Enter City Name (chicago, new york city, washington) : ").lower()

        if city not in CITY_DATA:
            print('pls enter one of these cities (chicago, new york city, washington)\n')
            continue
        else:
            while True:
                # get user input for month (all, january, february, ... , june)
                month = input("Enter Month ( january, february, ... , june) or Enter all: ")
                if month not in months:
                    print('pls enter one of these Months (january, february, ... , june) or Enter all\n')
                    continue
                else:
                    while True:
                        # get user input for day of week (all, monday, tuesday, ... sunday)
                        day = input("Enter Day Name ( monday, tuesday, ... sunday) or Enter all : ")
                        if day not in days:
                            print('pls enter one of these Days ( monday, tuesday, ... sunday) or Enter all\n')
                            continue
                        else:
                            print('--' * 40)
                            break
                    break

            break

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        # day = days.index(day)
        df = df[df['day of week'] == day.title()]
    print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df['month'].mode()[0]
    print("Most common Month :", most_month)
    # display the most common day of week
    most_day = df['day of week'].mode()[0]
    print("Most common day :", most_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_start_hour = df['hour'].mode()[0]
    print("Most common Hour :", most_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station : ", most_start_station)
    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("Most Common End Station : ", most_end_station)
    # display most frequent combination of start station and end station trip
    df['start&end'] = df['Start Station'] + "," + df['End Station']
    most_frequent_combination_of_start_station_and_end_station_trip = df['start&end'].mode()[0]
    print('--' * 40)
    print("most_frequent_combination_of_start_station_and_end_station_trip : ", "\n", "Start Station :",
          most_frequent_combination_of_start_station_and_end_station_trip.split(',')[0],
          "\n", "End Station : ", most_frequent_combination_of_start_station_and_end_station_trip.split(',')[1])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # df.info()
    # df['total travel time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Trip Duration'].sum()
    print(float(total_travel_time // 60 // 60), " h")
    print(float(total_travel_time // 60), " m")
    print(float(total_travel_time), " s")
    # print(total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean_travel_time : ', round(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = len(pd.unique(df['User Type'].dropna()))
    print("counts of user types : ", counts_of_user_types)
    if city != "washington":
        # Display counts of gender
        counts_of_gender = len(pd.unique(df['Gender'].dropna()))
        most_gender = df['Gender'].mode()[0]
        print("counts of Gender types : ", counts_of_gender)
        print("most_gender : ", most_gender)
        # Display counts of gender
        counts_of_gender = len(pd.unique(df['Gender'].dropna()))
        print("counts of Gender types : ", counts_of_gender)
        # Display earliest, most recent, and most common year of birth

        earliest_year_of_birth = df['Birth Year'].min()
        print("earliest year of birth : ", int(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print("most recent year of birth : ", int(most_recent_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print("most common year of birth : ", int(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_data(df):
    display_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()

    start_loc = 0
    end_loc = 5
    while display_data == "yes":
        print(df[start_loc:end_loc])
        end_loc += 5
        start_loc += 5
        view_data = input("Do you wish to continue?: Enter yes or no\n").lower()
        if view_data == "yes":
            continue
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
