import requests


class YaUploader:
  
    def __init__(self, token: str):
        self.token = token
        
    def get_headers(self):
        return {"Content-Type": 'application/json', 'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": 'true'} 
        response = requests.get(url, headers = headers, params = params)
        response = response.json()
        
        href  = response.get('href', '')
        result = requests.put(href, data=open("test.txt", 'rb'))
        
    

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'requests_hw/test.txt'
    token = input("Введите ваш токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)