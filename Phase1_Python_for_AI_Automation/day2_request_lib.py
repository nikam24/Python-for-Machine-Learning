import requests 

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(f"Response code: {response.status_code}\n")
print(f"Response body: {response.text}\n") 
print(f"Response headers:{response.headers}\n")
print(f"Response cookies: {response.cookies}")