import os
from requests import get
from requests.exceptions import RequestException
from dotenv import load_dotenv

load_dotenv()


def fetch_data(url, headers=None):
    try:
        response = get(url, headers=headers, timeout=10)
        response.raise_for_status()

        return response.json()
    except RequestException as e:
        print("API request failed:", e)
        return None


# ESPN API
ESPN_SCOREBOARD_URL = (
    "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard")


def get_scores():
    print("\n=== ESPN NBA SCOREBOARD ===")

    data = fetch_data(ESPN_SCOREBOARD_URL)
    if not data:
        return

    games = data["events"]

    for game in games:
        competition = game["competitions"][0]
        teams = competition["competitors"]

        name = game["name"]
        status = game["status"]["type"]["description"]

        print("-" * 40)
        print(name)

        for team in teams:
            team_name = team["team"]["displayName"]
            score = team.get("score", "N/A")

            print(f"{team_name}: {score}")

        print(status)


# BALLDONTLIE API
BALLDONTLIE_URL = "https://api.balldontlie.io/v1/teams"

API_KEY = os.getenv("BALLDONTLIE_API_KEY")
if not API_KEY:
    raise ValueError("Missing BALLDONTLIE_API_KEY")


def get_teams():
    print("\n=== BALLDONTLIE NBA TEAMS ===")

    headers = {
        "Authorization": API_KEY
    }

    data = fetch_data(BALLDONTLIE_URL, headers=headers)
    if not data:
        return

    for i, team in enumerate(data["data"]):
        print(f"{i + 1}. {team['full_name']} ({team['abbreviation']})")


# TheSportsDB API
SPORTSDB_URL = (
    "https://www.thesportsdb.com/api/v1/json/3/"
    "search_all_teams.php?l=NBA"
)


def get_team_info():
    print("\n=== TheSportsDB NBA TEAM INFO ===")

    data = fetch_data(SPORTSDB_URL)
    if not data:
        return

    for team in data["teams"]:
        print("-" * 40)
        print("Team:", team["strTeam"])
        print("Stadium:", team.get("strStadium", "Unknown"))
        print("Location:", team.get("strLocation", "Unknown"))
        print("Founded:", team.get("intFormedYear", "Unknown"))


def main():
    get_scores()
    get_teams()
    get_team_info()


main()
