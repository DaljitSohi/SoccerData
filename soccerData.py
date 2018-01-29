import httplib
import json
import csv

connection = httplib.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token':'3fbea3e04c574ff5a2af9b4e6d1b1188', 'X-Response-Control':'minified'}
def competitions():
    connection.request('GET', '/v1/competitions', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response

# comp_jsonData = competitions()
# print(comp_jsonData)

"""
    League Tables for :
    Seria A                 - ID: 456
    Premier League          - ID: 445
    Ligue 1                 - ID: 450
    Bundesliga 1            - ID: 452
    # La Liga                 - ID: 399
    # Champions League        - ID: 464
"""
def leagueTable(league):
    league_csvData = "Pos, Team, Points, Games Played, Goals For, Goals Against\n"
    if(league == 'SA'):
        connection.request('GET', '/v1/competitions/456/leagueTable', None, headers)
        response = json.loads(connection.getresponse().read().decode())
        # return response
        for pos in response["standing"]:
            # Pos	 Team	 GamesPlayer	 Points	 Goals For	 Goals Against
            # print(str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]))
            league_csvData += str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]) + "\n"
        print(league_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("SA_Table.csv", "w")
        myFile.writelines(league_csvData)
        myFile.close()

    elif (league == 'PL'):
        connection.request('GET', '/v1/competitions/445/leagueTable', None, headers)
        response = json.loads(connection.getresponse().read().decode())
        # return response
        for pos in response["standing"]:
            # Pos	 Team	 GamesPlayer	 Points	 Goals For	 Goals Against
            # print(str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]))
            league_csvData += str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]) + "\n"
        print(league_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("PL_Table.csv", "w")
        myFile.writelines(league_csvData)
        myFile.close()

    elif (league == 'Ligue1'):
        connection.request('GET', '/v1/competitions/450/leagueTable', None, headers)
        response = json.loads(connection.getresponse().read().decode())
        # return response
        for pos in response["standing"]:
            # Pos	 Team	 GamesPlayer	 Points	 Goals For	 Goals Against
            # print(str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]))
            league_csvData += str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]) + "\n"
        print(league_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("Ligue1_Table.csv", "w")
        myFile.writelines(league_csvData)
        myFile.close()

    elif (league == 'BL1'):
        connection.request('GET', '/v1/competitions/452/leagueTable', None, headers)
        resp = connection.getresponse()
        respBody = resp.read()
        # response = json.loads(connection.getresponse().read().decode())
        response = json.loads(respBody)
        # return response
        for pos in response["standing"]:
            # Pos	 Team	 GamesPlayer	 Points	 Goals For	 Goals Against
            # print(str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]))
            league_csvData += str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]) + "\n"
        print(league_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("BL1_Table.csv", "w")
        myFile.writelines(league_csvData)
        myFile.close()

    # elif(league == 'LaLiga'):
    #     connection.request('GET', '/v1/competitions/399/leagueTable', None, headers)
    #     response = json.loads(connection.getresponse().read().decode())
    #     return response

    # elif(league == 'CL'):
    #     connection.request('GET', '/v1/competitions/464/leagueTable', None, headers)
    #     response = json.loads(connection.getresponse().read().decode())
    #     return response

    else:
        return 'No Data found for the requested league'
'''
league_jsonData = leagueTables('BL1')
# print(type(league_jsonData))
# print(league_jsonData["standing"])

# Print Data in CSV FILE Format
league_csvData = "Pos, Team, Points, Games Played, Goals For, Goals Against\n"
#Loop the league_jsonData["standing"] -> List
for pos in league_jsonData["standing"]:
    # Pos	 Team	 GamesPlayer	 Points	 Goals For	 Goals Against
    # print(str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]))
    league_csvData += str(pos["rank"]) + ", " + pos["team"]  + ", " + str(pos["points"]) + ", " + str(pos["playedGames"]) + ", " +  str(pos["goals"]) + ", " + str(pos["goalsAgainst"]) + "\n"
print(league_csvData)
'''
#Show all the fixtures for the requested league
def fixturesList(league):
    fixtures_csvData = "Match Day, Date, Home Team, Away Team, Home Team Goals, Away Team Goals\n"
    if(league == 'SA'):
        connection.request('GET', '/v1/competitions/456/fixtures', None, headers)
        response = json.loads(connection.getresponse().read().decode())
        # return response ->
        for fix in response["fixtures"]:
            # Match Day	    Date	 Home Team	 Away Team	 Home Team Goals	 Away Team Goals
            # print(str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]['goalsHomeTeam']) + ", " + str(fix["result"]['goalsAwayTeam']))
            fixtures_csvData += str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]["goalsHomeTeam"]) + ", " + str(fix["result"]["goalsAwayTeam"]) + "\n"
        print(fixtures_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("SA_FixtureList.csv", "w")
        myFile.writelines(fixtures_csvData)
        myFile.close()

    elif (league == 'PL'):
        connection.request('GET', '/v1/competitions/445/fixtures', None, headers)
        response = json.loads(connection.getresponse().read().decode())
        # return response
        for fix in response["fixtures"]:
            # Match Day	    Date	 Home Team	 Away Team	 Home Team Goals	 Away Team Goals
            # print(str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]['goalsHomeTeam']) + ", " + str(fix["result"]['goalsAwayTeam']))
            fixtures_csvData += str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]["goalsHomeTeam"]) + ", " + str(fix["result"]["goalsAwayTeam"]) + "\n"
        print(fixtures_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("PL_FixtureList.csv", "w")
        myFile.writelines(fixtures_csvData)
        myFile.close()

    elif (league == 'Ligue1'):
        connection.request('GET', '/v1/competitions/450/fixtures', None, headers)
        resp = connection.getresponse()
        respBody = resp.read()
        # response = json.loads(connection.getresponse().read().decode())
        response = json.loads(respBody)
        for fix in response["fixtures"]:
            # Match Day	    Date	 Home Team	 Away Team	 Home Team Goals	 Away Team Goals
            # print(str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]['goalsHomeTeam']) + ", " + str(fix["result"]['goalsAwayTeam']))
            fixtures_csvData += str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]["goalsHomeTeam"]) + ", " + str(fix["result"]["goalsAwayTeam"]) + "\n"
        print(fixtures_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("Ligue1_FixtureList.csv", "w")
        myFile.writelines(fixtures_csvData)
        myFile.close()

    elif (league == 'BL1'):
        connection.request('GET', '/v1/competitions/452/fixtures', None, headers)
        resp = connection.getresponse()
        respBody = resp.read()
        # response = json.loads(connection.getresponse().read().decode())
        response = json.loads(respBody)
        for fix in response["fixtures"]:
            # Match Day	    Date	 Home Team	 Away Team	 Home Team Goals	 Away Team Goals
            # print(str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]['goalsHomeTeam']) + ", " + str(fix["result"]['goalsAwayTeam']))
            fixtures_csvData += str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]["goalsHomeTeam"]) + ", " + str(fix["result"]["goalsAwayTeam"]) + "\n"
        print(fixtures_csvData + "\n A CSV File has also been in the current directory")
        #Write to a the File
        myFile = open("BL1_FixtureList.csv", "w")
        myFile.writelines(fixtures_csvData)
        myFile.close()
    else:
        return 'No Fixture Data found for the requested league'

# leagueTables("SA")
#
# print("")
#
# fixturesList("PL")
'''
fixtures_jsonData = fixtures('BL1')
# print(fixtures_jsonData["fixtures"])

# Print Data in CSV FILE Format
# fixtures_csvData = "Match Day, Date, Home Team, Away Team, Home Team Goals, Away Team Goals\n" ->
# Loop the fixtures_jsonData["fixtures"] -> List

for fix in fixtures_jsonData["fixtures"]:
    # Match Day	    Date	 Home Team	 Away Team	 Home Team Goals	 Away Team Goals
    # print(str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]['goalsHomeTeam']) + ", " + str(fix["result"]['goalsAwayTeam']))
    fixtures_csvData += str(fix["matchday"]) + ", " + fix["date"] + ", " + fix["homeTeamName"] + ", " + fix["awayTeamName"] + ", " + str(fix["result"]["goalsHomeTeam"]) + ", " + str(fix["result"]["goalsAwayTeam"]) + "\n"
print(fixtures_csvData)
'''
