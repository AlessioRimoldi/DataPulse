import datetime
import json
import logging
import os
import sys

import requests
import pwinput
import readchar

from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

# Configure debug logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
"""
export G_EMAIL=<your garmin email>
export G_PASSWORD=<your garmin password>
"""
# Load environment variables if defined

class Retrieve:
    
    def __init__(self,start = 0,limit = 100):
        self.email = os.getenv("G_EMAIL")
        self.password = os.getenv("G_PASSWORD")
        self.api = None

        self.today = datetime.date.today()
        self.startdate = self.today - datetime.timedelta(days=7) # Select past week
        self.start = start
        self.limit = limit
        self.start_badge = 1  # Badge related calls calls start counting at 1                
        self.activityfile = "MY_ACTIVITY.fit" # Supported file types are: .fit .gpx .tcx

        self.menu_options = {
            "1": "Get full name",
            "2": "Get unit system",
            "3": f"Get activity data for '{self.today.isoformat()}'",
            "4": f"Get activity data for '{self.today.isoformat()}' (compatible with garminconnect-ha)",
            "5": f"Get body composition data for '{self.today.isoformat()}' (compatible with garminconnect-ha)",
            "6": f"Get body composition data for from '{self.startdate.isoformat()}' to '{self.today.isoformat()}' (to be compatible with garminconnect-ha)",
            "7": f"Get stats and body composition data for '{self.today.isoformat()}'",
            "8": f"Get steps data for '{self.today.isoformat()}'",
            "9": f"Get heart rate data for '{self.today.isoformat()}'",
            "0": f"Get training readiness data for '{self.today.isoformat()}'",
            ".": f"Get training status data for '{self.today.isoformat()}'",
            "a": f"Get resting heart rate data for {self.today.isoformat()}'",
            "b": f"Get hydration data for '{self.today.isoformat()}'",
            "c": f"Get sleep data for '{self.today.isoformat()}'",
            "d": f"Get stress data for '{self.today.isoformat()}'",
            "e": f"Get respiration data for '{self.today.isoformat()}'",
            "f": f"Get SpO2 data for '{self.today.isoformat()}'",
            "g": f"Get max metric data (like vo2MaxValue and fitnessAge) for '{self.today.isoformat()}'",
            "h": "Get personal record for user",
            "i": "Get earned badges for user",
            "j": f"Get adhoc challenges data from start '{self.start}' and limit '{self.limit}'",
            "k": f"Get available badge challenges data from '{self.start_badge}' and limit '{self.limit}'",
            "l": f"Get badge challenges data from '{self.start_badge}' and limit '{self.limit}'",
            "m": f"Get non completed badge challenges data from '{self.start_badge}' and limit '{self.limit}'",
            "n": f"Get activities data from start '{self.start}' and limit '{self.limit}'",
            "o": "Get last activity",
            "p": f"Download activities data by date from '{self.startdate.isoformat()}' to '{self.today.isoformat()}'",
            "r": f"Get all kinds of activities data from '{self.start}'",
            "s": f"Upload activity data from file '{self.activityfile}'",
            "t": "Get all kinds of Garmin device info",
            "Z": "Logout Garmin Connect portal",
            "q": "Exit",
        }

    def display_json(self,api_call, output):
        """Format API output for better readability."""
        dashed = "-"*20
        header = f"{dashed} {api_call} {dashed}"
        footer = "-"*len(header)
        print(header)
        print(json.dumps(output, indent=4))
        print(footer)
        
    def get_credentials(self):
        """Get user credentials."""
        email = input("Login e-mail: ")
        password = pwinput.pwinput(prompt='Password: ')
        
        return email,password


    def init_api(self):
        """Initialize Garmin API with your credentials."""

        try:
            ## Try to load the previous session
            with open("session.json") as f:
                saved_session = json.load(f)

                print(
                    "Login to Garmin Connect using session loaded from 'session.json'...\n"
                )

                # Use the loaded session for initializing the API (without need for credentials)
                api = Garmin(session_data=saved_session)

                # Login using the
                api.login()

        except (FileNotFoundError, GarminConnectAuthenticationError):
            # Login to Garmin Connect portal with credentials since session is invalid or not presentlastweek.
            print(
                "Session file not present or invalid, login with your credentials, please wait...\n"
            )
            try:
                # Ask for credentials if not set as environment variables
                if (self.email is None) or (self.password is None):
                    self.email, self.password = self.get_credentials()

                api = Garmin(self.email, self.password)
                api.login()

                # Save session dictionary to json file for future use
                with open("session.json", "w", encoding="utf-8") as f:
                    json.dump(api.session_data, f, ensure_ascii=False, indent=4)
            except (
                GarminConnectConnectionError,
                GarminConnectAuthenticationError,
                GarminConnectTooManyRequestsError,
                requests.exceptions.HTTPError,
            ) as err:
                logger.error("Error occurred during Garmin Connect communication: %s", err)
                return None

        return api

    def print_menu(self):
        """Print examples menu."""
        for key in self.menu_options.keys():
            print(f"{key} -- {self.menu_options[key]}")
        print("Make your selection: ", end="", flush=True)

    def switch(self,api, i, activitytype = ""):  #["cycling", 'running', 'swimming', 'multi_sport', 'fitness_equipment', 'hiking', 'walking', 'other']
        """Run selected API call."""

        # Exit example program
        if i == "q":
            print("Bye!")
            sys.exit()

        # Skip requests if login failed
        if api:
            try:
                print(f"\n\nExecuting: {self.menu_options[i]}\n")

                # USER BASICS
                if i == "1":
                    # Get full name from profile
                    self.display_json("api.get_full_name()", api.get_full_name())
                elif i == "2":
                    # Get unit system from profile
                    self.display_json("api.get_unit_system()", api.get_unit_system())

                # USER STATISTIC SUMMARIES
                elif i == "3":
                    # Get activity data for 'YYYY-MM-DD'
                   self.display_json(f"api.get_stats('{self.today.isoformat()}')", api.get_stats(self.today.isoformat()))
                elif i == "4":
                    # Get activity data (to be compatible with garminconnect-ha)
                    self.display_json(f"api.get_user_summary('{self.today.isoformat()}')", api.get_user_summary(self.today.isoformat()))
                elif i == "5":
                    # Get body composition data for 'YYYY-MM-DD' (to be compatible with garminconnect-ha)
                    self.display_json(f"api.get_body_composition('{self.today.isoformat()}')", api.get_body_composition(self.today.isoformat()))
                elif i == "6":
                    # Get body composition data for multiple days 'YYYY-MM-DD' (to be compatible with garminconnect-ha)
                    self.display_json(f"api.get_body_composition('{self.startdate.isoformat()}', '{self.today.isoformat()}')",
                        api.get_body_composition(self.startdate.isoformat(), self.today.isoformat())
                    )
                elif i == "7":
                    # Get stats and body composition data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_stats_and_body('{self.today.isoformat()}')", api.get_stats_and_body(self.today.isoformat()))

                # USER STATISTICS LOGGED
                elif i == "8":
                    # Get steps data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_steps_data('{self.today.isoformat()}')", api.get_steps_data(self.today.isoformat()))
                elif i == "9":
                    # Get heart rate data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_heart_rates('{self.today.isoformat()}')", api.get_heart_rates(self.today.isoformat()))
                elif i == "0":
                    # Get training readiness data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_training_readiness('{self.today.isoformat()}')", api.get_training_readiness(self.today.isoformat()))
                elif i == ".":
                    # Get training status data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_training_status('{self.today.isoformat()}')", api.get_training_status(self.today.isoformat()))
                elif i == "a":
                    # Get resting heart rate data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_rhr_day('{self.today.isoformat()}')", api.get_rhr_day(self.today.isoformat()))
                elif i == "b":
                    # Get hydration data 'YYYY-MM-DD'
                    self.display_json(f"api.get_hydration_data('{self.today.isoformat()}')", api.get_hydration_data(self.today.isoformat()))
                elif i == "c":
                    # Get sleep data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_sleep_data('{self.today.isoformat()}')", api.get_sleep_data(self.today.isoformat()))
                elif i == "d":
                    # Get stress data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_stress_data('{self.today.isoformat()}')", api.get_stress_data(self.today.isoformat()))
                elif i == "e":
                    # Get respiration data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_respiration_data('{self.today.isoformat()}')", api.get_respiration_data(self.today.isoformat()))
                elif i == "f":
                    # Get SpO2 data for 'YYYY-MM-DD'
                    self.display_json(f"api.get_spo2_data('{self.today.isoformat()}')", api.get_spo2_data(self.today.isoformat()))
                elif i == "g":
                    # Get max metric data (like vo2MaxValue and fitnessAge) for 'YYYY-MM-DD'
                    self.display_json(f"api.get_max_metrics('{self.today.isoformat()}')", api.get_max_metrics(self.today.isoformat()))
                elif i == "h":
                    # Get personal record for user
                    self.display_json("api.get_personal_record()", api.get_personal_record())
                elif i == "i":
                    # Get earned badges for user
                    self.display_json("api.get_earned_badges()", api.get_earned_badges())
                elif i == "j":
                    # Get adhoc challenges data from start and limit
                    self.display_json(
                        f"api.get_adhoc_challenges({self.start},{self.limit})", api.get_adhoc_challenges(self.start, self.limit)
                    )  # 1=start, 100=limit
                elif i == "k":
                    # Get available badge challenges data from start and limit
                    self.display_json(
                        f"api.get_available_badge_challenges({self.start_badge}, {self.limit})", api.get_available_badge_challenges(self.start_badge, self.limit)
                    )  # 1=start, 100=limit
                elif i == "l":
                    # Get badge challenges data from start and limit
                    self.display_json(
                        f"api.get_badge_challenges({self.start_badge}, {self.limit})", api.get_badge_challenges(self.start_badge, self.limit)
                    )  # 1=start, 100=limit
                elif i == "m":
                    # Get non completed badge challenges data from start and limit
                    self.display_json(
                        f"api.get_non_completed_badge_challenges({self.start_badge}, {self.limit})", api.get_non_completed_badge_challenges(self.start_badge, self.limit)
                    )  # 1=start, 100=limit

                # ACTIVITIES
                elif i == "n":
                    # Get activities data from start and limit
                    self.display_json(f"api.get_activities({self.start}, {self.limit})", api.get_activities(self.start, self.limit)) # 0=start, 1=limit
                elif i == "o":
                    # Get last activity
                    self.display_json("api.get_last_activity()", api.get_last_activity())
                elif i == "p":    
                    # Get activities data from startdate 'YYYY-MM-DD' to enddate 'YYYY-MM-DD', with (optional) activitytype
                    # Possible values are: cycling, running, swimming, multi_sport, fitness_equipment, hiking, walking, other
                    activities = api.get_activities_by_date(
                        self.startdate.isoformat(), self.today.isoformat(), activitytype
                    )

                    # Download activities
                    for activity in activities:
                        activity_id = activity["activityId"]
                        self.display_json(f"api.download_activity({activity_id})", api.download_activity(activity_id))

                        gpx_data = api.download_activity(
                            activity_id, dl_fmt=api.ActivityDownloadFormat.GPX
                        )
                        output_file = f"./{str(activity_id)}.gpx"
                        with open(output_file, "wb") as fb:
                            fb.write(gpx_data)

                        tcx_data = api.download_activity(
                            activity_id, dl_fmt=api.ActivityDownloadFormat.TCX
                        )
                        output_file = f"./{str(activity_id)}.tcx"
                        with open(output_file, "wb") as fb:
                            fb.write(tcx_data)

                        zip_data = api.download_activity(
                            activity_id, dl_fmt=api.ActivityDownloadFormat.ORIGINAL
                        )
                        output_file = f"./{str(activity_id)}.zip"
                        with open(output_file, "wb") as fb:
                            fb.write(zip_data)

                        csv_data = api.download_activity(
                            activity_id, dl_fmt=api.ActivityDownloadFormat.CSV
                        )
                        output_file = f"./{str(activity_id)}.csv"
                        with open(output_file, "wb") as fb:
                            fb.write(csv_data)

                elif i == "r":
                    # Get activities data from start and limit
                    activities = api.get_activities(self.start, self.limit)  # 0=start, 1=limit

                    # Get activity splits
                    first_activity_id = activities[0].get("activityId")

                    self.display_json(f"api.get_activity_splits({first_activity_id})", api.get_activity_splits(first_activity_id))

                    # Get activity split summaries for activity id
                    self.display_json(f"api.get_activity_split_summaries({first_activity_id})", api.get_activity_split_summaries(first_activity_id))

                    # Get activity weather data for activity
                    self.display_json(f"api.get_activity_weather({first_activity_id})", api.get_activity_weather(first_activity_id))

                    # Get activity hr timezones id
                    self.display_json(f"api.get_activity_hr_in_timezones({first_activity_id})", api.get_activity_hr_in_timezones(first_activity_id))

                    # Get activity details for activity id
                    self.display_json(f"api.get_activity_details({first_activity_id})", api.get_activity_details(first_activity_id))

                    # Get gear data for activity id
                    self.display_json(f"api.get_activity_gear({first_activity_id})", api.get_activity_gear(first_activity_id))

                    # Activity self evaluation data for activity id
                    self.display_json(f"api.get_activity_evaluation({first_activity_id})", api.get_activity_evaluation(first_activity_id))

                elif i == "s":
                    # Upload activity from file
                    self.display_json(f"api.upload_activity({self.activityfile})", api.upload_activity(self.activityfile))

                # DEVICES
                elif i == "t":
                    # Get Garmin devices
                    devices = api.get_devices()
                    self.display_json("api.get_devices()", devices)

                    # Get device last used
                    device_last_used = api.get_device_last_used()
                    self.display_json("api.get_device_last_used()", device_last_used)

                    # Get settings per device
                    for device in devices:
                        device_id = device["deviceId"]
                        self.display_json(f"api.get_device_settings({device_id})", api.get_device_settings(device_id))

                elif i == "Z":
                    # Logout Garmin Connect portal
                    self.display_json("api.logout()", api.logout())
                    api = None

            except (
                GarminConnectConnectionError,
                GarminConnectAuthenticationError,
                GarminConnectTooManyRequestsError,
                requests.exceptions.HTTPError,
            ) as err:
                logger.error("Error occurred: %s", err)
            except KeyError:
                # Invalid menu option chosen
                pass
        else:
            print("Could not login to Garmin Connect, try again later.")
    
    def run(self):
        
        print("Connecting to Garmin Site...")
        
        api = self.init_api()
        self.print_menu()
        print("Select option : ")
        option = readchar.readkey()
        self.switch(api,option)
        
        

if __name__ == "__main__":
    
    ret = Retrieve()
    
    ret.run()

