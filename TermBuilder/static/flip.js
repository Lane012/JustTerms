
function Flip() {
	var words = document.getElementsByClassName("word");
	var definitions = document.getElementsByClassName("definition");
	
	
	for (i=0; i < words.length; i++) {
		currentWord = words[i];
		currentDef = definitions[i];
		
		if(currentWord.style.display != "none") {
			currentWord.style.display = "none";
			currentDef.style.display = "";
		}
		
		else {
			if(currentDef.style.display != "none") {
				
				currentDef.style.display = "none";
				currentWord.style.display = "";

			}
		}
		
	}
					
}