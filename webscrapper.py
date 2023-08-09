from bs4 import BeautifulSoup
import requests

print('''Yb        dP 88888 88""Yb .dP"Y8  dP""b8 88""Yb    db    88""Yb 88""Yb 888888 88""Yb 
 Yb  db  dP    .dP 88__dP `Ybo." dP   `" 88__dP   dPYb   88__dP 88__dP 88__   88__dP 
  YbdPYbdP   o `Yb 88""Yb o.`Y8b Yb      88"Yb   dP__Yb  88"""  88"""  88""   88"Yb  
   YP  YP    YbodP 88oodP 8bodP'  YboodP 88  Yb dP""""Yb 88     88     888888 88  Yb ''')

try:
 user_website_url = str(input("\n\n\nEnter The URL Of The Website: "))
 req = requests.get(user_website_url)
 data_req = BeautifulSoup(req.content, "html.parser")
 final_data = data_req.prettify()
 user_location = input("Enter The Path To Txt File Where You Want To Save ( Do Not Add Quotation Around The Path) : ")
 with open(user_location, "w") as file_output:
   file_output.write(final_data)
   print(f"Data Saved In {user_location} ")
except Exception as e:
  print("Error Occured, Please Check The URL Or The Path Of Txt File")
  exit()
     
