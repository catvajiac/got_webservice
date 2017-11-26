# got_webservice
Game of Thrones Webservice for paradigms final project

* Unzip data for API by running unzip_data.sh

* API gives Game of Thrones character information, specifically:
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

  API methods are tested in test.py.

  By default, `load_files()` looks for data to be in `data` directory.

All data comes from https://www.kaggle.com/mylesoneill/game-of-thrones/data.
