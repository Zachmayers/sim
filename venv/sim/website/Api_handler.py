import requests

class Api_handler:

    def __init__(self):
        '''
            Handler for sending and receiving data to the api
        '''
        self.KEY = 'test123'

    def _get_activities(self):
        try:
            url = f"https://milliondollarmacrame.com/PlusOneSim/loneme_api/get_list.php?type=activity&key={self.KEY}"

            payload={}
            headers = {
            'Cookie': 'PHPSESSID=dc9a4cc7a4248712329bd5f834d5d234'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            print(response)
            return response.json()
        except Exception as e:
            print(e)
            return


    def get_activity_list(self):
        activites = self._get_activities()

        activity_name_list = []

        for i in activites:
            activity_name_list.append(i['activity'])
        
        return activity_name_list
