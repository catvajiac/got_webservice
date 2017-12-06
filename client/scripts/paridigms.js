function Title() {
	this.createTitle = function(text, id, size){
		this.item = document.createElement("h"+size);
		this.item.setAttribute("id", id);
		var textLabel = document.createTextNode(text);
		this.item.appendChild(textLabel);
	},
	this.setText = function(text){
		this.item.innerHTML=text;
	},
	this.addToDocument = function(){
		document.body.appendChild(this.item);
	}
};


function InputBox() {
	this.createInput = function(name){
		this.item = document.createElement("form")

		// Add Text To Form Item
		//var t = document.createTextNode(name + " ")

    var thing = document.createElement("br")
    document.body.appendChild(thing)
    
    var t = document.createElement("p")
    t.innerHTML = name
    t.setAttribute("class", "url")
		this.item.appendChild(t)

		// Add Input Box to Form Item
		this.input = document.createElement("input")
		this.input.setAttribute("type", "text")
		this.item.appendChild(this.input)

		// Add Submit Button to Form Item
		this.submit = document.createElement("buton")
    this.submit.setAttribute("class", "submit")
		this.submit.innerHTML = "Submit"
		this.item.appendChild(this.submit)
	},

	this.addClickEventHandler = function(handler, args){ this.submit.onmouseup = function(){
      handler(args);
    };
	},

	this.getValue = function() {
		return this.input.value
	},


	this.addToDocument = function() {
		document.body.appendChild(this.item)
	}
};


function Label() {
	this.createLabel = function(text, id){
		this.item = document.createElement("p");
		this.item.setAttribute("id", id);
		this.item.setAttribute("class", "url");
		var textLabel = document.createTextNode(text);
		this.item.appendChild(textLabel);
	},
	this.setText = function(text){
		this.item.innerHTML=text;
	},
	this.addToDocument = function() {
		document.body.appendChild(this.item)
	}
};



