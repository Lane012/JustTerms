var words = document.getElementsByClassName("word");
var definitions = document.getElementsByClassName("definition");


var iterator = { 
		 counter : 0, 
		 currentWord : words[0],
		 currentDef : definitions[0], 
		 
		 hideDef : function() {
		 	this.currentDef.style.display = "none";
		 },
		 
		 showDef : function() {
		 	this.currentDef.style.display = "";
		 },
		 
		 wordVisible : function() {
		 	if(this.currentWord.style.display != "none") {
		 		return true;
		 	}
		 	return false;
		 },
		 
		 hideWord : function() {
		 	this.currentWord.style.display = "none";
		 },
		 
		 showWord : function() {
		 	this.currentWord.style.display = "";
		 },
		 
		 next : function() {
				if(this.wordVisible()){
					this.hideWord()
					this.nextWord();
				}
				else {
					this.hideDef();
					this.nextDef();
				}
		 },
		 
		 nextWord : function() {
		 	 if(this.counter < words.length-1) {
		 		this.currentWord = words[++this.counter];
		 	}
		 	else {
		 		this.counter = 0;
		 		this.currentWord = words[this.counter];
		 	}
		 	this.showWord();
		 },
		 
		 nextDef : function() {
		 	 if(this.counter < words.length-1) {
		 		this.currentDef = definitions[++this.counter];
		 	}
		 	else {
		 		this.counter = 0;
		 		this.currentDef = definitions[this.counter];
		 	}
		 	this.showDef();
		 },
		 
		 prev : function() {
			if(this.wordVisible()) {
				this.hideWord();
				this.prevWord();
			}
			else{
				this.hideDef();
				this.prevDef();
			}
		 },
		 
		 prevWord : function() {
		 	if(this.counter > 0) {
		 		this.currentWord = words[--this.counter];
		 	}
		 	else{
		 		this.counter = words.length -1;
		 		this.currentWord = words[this.counter];
		 	}
		 	this.showWord();
		 },
		 	
		 
		 prevDef : function() {
		 	if(this.counter > 0) {
		 		this.currentDef = definitions[--this.counter];
		 	}
		 	else{
		 		this.counter = words.length -1;
		 		this.currentDef = definitions[this.counter];
		 	}
		 	this.showDef();
		 },
		 
		 flip : function() {
		 	if(this.wordVisible()) {
		 		this.currentWord.style.display = "none";
		 		this.currentDef = definitions[this.counter];
		 		this.currentDef.style.display = "";
		 	}
		 	else{
		 		this.currentDef.style.display = "none";
		 		this.currentWord = words[this.counter];
		 		this.currentWord.style.display = "";
		 	}
		 },
};


	
function Next() {
	iterator.next();
}

function Prev() {
	iterator.prev();
}

function Flip() {
	iterator.flip();
}


	
	
	