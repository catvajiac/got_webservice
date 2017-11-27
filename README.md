# GotWeb?
  
  GotWeb is a Game of Thrones webservice that offers vital information for any and all characters
  in the Song of Ice and Fire series. 

## Character Info:
  - Is the character dead? What year did they die? In which book did they die?
  - What gender is the character?
  - Is the character nobility or a commonder? If nobility, what is their title?
  - What house does the character belong to?
  - What year was the character born?
  - In which chapter was the character first introduced?

## Usage

Get data files from zip
$ `bash unzip_data.sh`

Test methods
$ `python3 test.py`

## Methods

  * `is_dead(character)`: if character is dead yet
  * `get_gender(character)`: gender
  * `get_nobility(character)`: if character is common or nobility
  * `get_nobility(character)`: character's house
  * `get_house(character)`: character's birth year
  * `get_birth_year(character)`: character's death year
  * `get_death_book(character)`: book character died in
  * `get_intro_chapter(chapter)`: chapter character first appeared in
  * `get_title(character)`: character's title, if applicable

  All methods return -1 if character is not in dataset.

## Sources

  All data comes from https://www.kaggle.com/mylesoneill/game-of-thrones/data.
