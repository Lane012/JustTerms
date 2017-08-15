
function Next() {
	var words = document.getElementsByClassName("word");
	var definitions = document.getElementsByClassName("definition");
	var done = false;
	
	for (i=0; i < words.length; i++) {
		currentWord = words[i];
		currentDef = definitions[i];
		
		if(currentWord.style.display != "none") {
			currentWord.style.display = "none";
			done = true;
			if(i +1 < words.length) {
				next = words[i + 1];
				next.style.display = "";
			}
			else{
				next = words[0];
				next.style.display = "";
			}
		}
		
		else if(currentDef.style.display != "none") {
			currentDef.style.display = "none";
			done = true;
			if(i +1 < words.length) {
				nextDef = definitions[i + 1];
				nextDef.style.display = "";
			}
			else{
				nextDef = definitions[0];
				nextDef.style.display = "";
			}
				
		}
		
		if(done) {
			break;
		}
	}
}