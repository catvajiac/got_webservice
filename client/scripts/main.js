PORT = '51062'
HOST = "localhost"
//HOST = "student04.cse.nd.edu"
BASE_URL = "http://" + HOST + ":" + PORT
URLS = ["/characters/","/houses/","/dead/","/bookstats/"]

//CAPTIONS creates headers with Text = Caption[0], id = Caption[1], and Size = Caption[2] (from 1 - Biggest, to 5 - Smallest)
CAPTIONS = [["Game of Thrones Client Information", "titleHeader", 1], 
	["\'/charactes/\' & \'/houses/\' take a character or house name as input, or no input. They return info for a given character or house", "expl_1_titleHeader", 5],
	["\'/dead/\' & \'/bookstats/\'  take a book number as input, or no input. They return death information of general statistics about a book", "expl_2_titleHeader", 5]
]

function load_page(){
	LABEL = new Label();
	LABEL.createLabel("", "output_label")
	
	HEADERS = []
	for(var i = 0; i < CAPTIONS.length; i++){
		var tmpHeader = new Title();
		tmpHeader.createTitle(CAPTIONS[i][0], CAPTIONS[i][2], CAPTIONS[i][2]);
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


function send_get(args) // args[0] = url, args[1] = Input Box Object, args[2] = Output Label
{
	var url = args[0] + String(args[1].getValue())

	var rec_xhr = new XMLHttpRequest();
	rec_xhr.open("GET", url, true);

	rec_xhr.onload = function(e) {
		var dict = JSON.parse(rec_xhr.responseText);
		console.log(JSON.stringify(dict))
		args[2].setText(JSON.stringify(dict))
	}
	rec_xhr.onerror = function(e) {
		console.error(rec_xhr.statusText);
	}

	rec_xhr.send(null);

};

