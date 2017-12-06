PORT = '51062'
HOST = "localhost"
//HOST = "student04.cse.nd.edu"
BASE_URL = "http://" + HOST + ":" + PORT
URLS = ["/characters/","/houses/","/dead/","/bookstats/"]

//CAPTIONS creates headers with Text = Caption[0], id = Caption[1], and Size = Caption[2] (from 1 - Biggest, to 5 - Smallest)
CAPTIONS = [
  ["Game of Thrones", "got_title", 1], 
  ["Character & Book Information", "got_info", 1],
  ["How to Use", "how_to", 2],
  ["''charactes'' & ''houses'' take a character or house name as input, or no input. They return info for a given character or house", "expl_1_titleHeader", 4],
  ["''dead'' & ''bookstats''  take a book number as input, or no input. They return death information of general statistics about a book", "expl_2_titleHeader", 4]
]

function load_page(){
  LABEL = new Label();
  LABEL.createLabel("", "output_label")
  
  HEADERS = []
  for(var i = 0; i < CAPTIONS.length; i++){
    var tmpHeader = new Title();
    tmpHeader.createTitle(CAPTIONS[i][0], CAPTIONS[i][1], CAPTIONS[i][2]);
    tmpHeader.addToDocument();
    HEADERS.push(tmpInput)
  }


  // Create Submission Boxes
  INPUTS = []
  for(var i = 0; i < URLS.length; i++){
    var tmpInput = new InputBox()
    tmpInput.createInput(URLS[i])
    tmp_args = [BASE_URL + URLS[i], tmpInput, LABEL]
    tmpInput.addClickEventHandler(send_get,tmp_args)
    tmpInput.addToDocument();
    INPUTS.push(tmpInput)
  }

  LABEL.addToDocument();

};

function send_get(args) {
  // args[0] = url, args[1] = Input Box Object, args[2] = Output Label
  var url = args[0] + String(args[1].getValue())
  console.log(args[0])

  var rec_xhr = new XMLHttpRequest();
  rec_xhr.open("GET", url, true);

  rec_xhr.onload = function(e) {
    var dict = JSON.parse(rec_xhr.responseText);
    console.log(JSON.stringify(dict));
    
    to_print = "";
    first = true;
    for (var key in dict) {
      if (key == "result") {
        continue;
      }

      to_print += key + ': ';
      for (var val in dict[key]) {
        if (first) {
          first = false;
        } else {
          to_print += ', ';
        }
  
        to_print += dict[key][val];
      }

      to_print += '\n';
    }

    args[2].setText(to_print)
  }
  rec_xhr.onerror = function(e) {
    console.error(rec_xhr.statusText);
  }

  rec_xhr.send(null);
};
