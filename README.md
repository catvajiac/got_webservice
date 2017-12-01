# GotWeb?
  
  GotWeb is a Game of Thrones webservice that offers vital information for any and all characters
  in the Song of Ice and Fire series. 

## Resources:
  /characters/ - A list of all characters
  /characters/:character_name - Information On A Specific Character (Name passed with '\_' instead of spaces) 
  /houses/ - A list of all houses
  /houses/:house_name - A list of all characters in a house
  /dead/ - A list of all dead characters
  /dead/:book_num - A list of all dead characters from a specific book
  /bookstats/ - Statistics on all books
  /bookstats/:book_num - Statistics on a specific book

## Usage
Port Number = 7000

Get data files from zip
$ `bash unzip_data.sh`

Test methods
$ `python3 test.py`

Start Webservice 
$ `python3 main.py`

Run Webservice Test
$ `python3 test_ws.py`

## Applicible Methods

  * `get_characters()`: A list of all characters
  * `get_character(character)`: Information On A Specific Character (Name passed with '\_' instead of spaces) 
  * `get_houses()`: A list of all houses
  * `get_house(house_name)`: A list of all characters in a house
  * `get_dead()`: A list of all dead characters
  * `get_dead_by_book(book_num)`: A list of all dead characters from a specific book
  * `get_books()`: Statistics on all books
  * `get_book(book_num)`: Statistics on a specific book

  All methods return -1 if character is not in dataset.

## Sources

  All data comes from https://www.kaggle.com/mylesoneill/game-of-thrones/data.
