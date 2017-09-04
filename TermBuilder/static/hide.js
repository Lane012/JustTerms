
var words = document.getElementsByClassName("word");
var definitions = document.getElementsByClassName("definition");
var title = document.getElementsByTagName("title")[0];



if(title.innerHTML == "Study") {
	for (i =1; i < words.length; i++) {
		currentWord = words[i];
		currentWord.style.display = "none";
	}
	
	for (i =0; i < definitions.length; i++) {
		currentDef = definitions[i];
		currentDef.style.display = "none";
	}
}

else if(title.innerHTML == "Test") {
	var frames = document.getElementsByClassName("main");
	
	for(i =1; i < frames.length; i++) {
		currentFrame = frames[i];
		currentFrame.style.display = "none";
	}
}
