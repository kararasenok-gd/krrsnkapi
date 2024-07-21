import requests
import json

class KrrsnkAPIError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
class KrrsnkAPI:
    def __init__(self, api_key):
        """
        Initializes a new instance of the KrrsnkAPI class.

        Args:
            api_key (str): The API key used for authentication.

        Initializes the following instance variables:
            - api_key (str): The API key used for authentication.
            - base_url (str): The base URL for the API.
            - KrrsnkCHAT (KrrsnkCHAT): An instance of the KrrsnkCHAT class initialized with the provided API key.
        """
        self.api_key = api_key
        self.base_url = 'https://kararasenok.ueuo.com/api/v2/'
        self.KrrsnkCHAT = self.__KrrsnkCHAT__(api_key)
        
    class __KrrsnkCHAT__:
        def __init__(self, api_key):
            """
            Initializes a new instance of the KrrsnkCHAT class.
            
            Args:
                api_key (str): The API key used for authentication.
            """
            self.api_key = api_key
            self.base_url = 'https://kararasenok.ueuo.com/api/v2/'
            
        def send_message(self, message, username = None):
            """
            Sends a message using the KrrsnkAPI. 

            Args:
                message (str): The message to be sent.
                username (str, optional): The username associated with the message. Defaults to None (will be used api key name if not specified).

            Returns:
                bool: True if the message was sent successfully.
                
            Raises:
                KrrsnkAPIError: If the server returns a non-200 code.

            """
            url = self.base_url + 'krrsnkchat/add.php'
            
            response = requests.post(url, data = {'key': self.api_key, 'message': message} if username is None else {'key': self.api_key, 'message': message, 'username': username})
            
            response = json.loads(response.text)
            code = response['code']
            
            if code != 200:
                raise KrrsnkAPIError(f"Server returned non-200 code ({code}). Error message: {response['error']}")
            
            return True

        def get_messages(self):
            """
            Retrieves messages from the server using the KrrsnkAPI.

            Returns:
                dict: A dictionary containing the messages retrieved from the server.

            Raises:
                KrrsnkAPIError: If the server returns a non-200 code.

            """
            
            url = self.base_url + 'krrsnkchat/get.php'
            
            response = requests.post(url, data = {'key': self.api_key})
            
            response = json.loads(response.text)
            code = response['code']
            
            if code != 200:
                raise KrrsnkAPIError(f"Server returned non-200 code ({code}). Error message: {response['error']}")
            
            return response['messages']
        
        def get_message_by_id(self, message_id):
            """
            Retrieves a message from the server by its ID.

            Args:
                message_id (int): The ID of the message to retrieve.

            Returns:
                dict: The message dictionary containing the message content.

            Raises:
                KrrsnkAPIError: If the server returns a non-200 code.

            """
            url = self.base_url + 'krrsnkchat/getByID.php'
            
            response = requests.post(url, data = {'key': self.api_key, 'id': message_id})
            
            response = json.loads(response.text)
            code = response['code']
            
            if code != 200:
                raise KrrsnkAPIError(f"Server returned non-200 code ({code}). Error message: {response['error']}")
            
            return response['message']