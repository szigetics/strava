import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import time

def getActivityById(idNumber):
    # create an instance of the API class
    api_instance = swagger_client.ActivitiesApi()
    id = idNumber # Long | The identifier of the activity.
    includeAllEfforts = True # Boolean | To include all segments efforts. (optional)


    try:
        # Get Activity
        api_response = api_instance.getActivityById(id, includeAllEfforts=includeAllEfforts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)



if __name__ == "__main__":

    StravaClientID = 'YourKey'
    StravaClientSecret = 'YourKey'
    StravaYourAccessToken = 'YourKey'
    StravaYourRefreshToken = 'YourKey'

    with open('/home/dalri/Documents/key.txt') as fp:
        line = fp.readline()
        while line:
            if (line.split(';')[0] == 'StravaClientID'):
                StravaClientID = line.split(';')[1]
            elif (line.split(';')[0] == 'StravaClientSecret'):
                StravaClientSecret = line.split(';')[1]
            elif (line.split(';')[0] == 'StravaYourAccessToken'):
                StravaYourAccessToken = line.split(';')[1]
            elif (line.split(';')[0] == 'StravaYourRefreshToken'):
                StravaYourRefreshToken = line.split(';')[1]
            line = fp.readline()

    # Configure OAuth2 access token for authorization: strava_oauth
    swagger_client.configuration.access_token = StravaYourAccessToken

    getActivityById(2950171403)
