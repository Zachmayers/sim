from Api_handler import Api_handler

API_handler = Api_handler()

activites = API_handler.get_activity_list()
print(activites)

