
var xhttp = new XMLHttpRequest();
var table = document.getElementById("list");
var tableRows = table.getElementsByTagName('tr');
var body = document.getElementsByTagName("body")[0];
var button = document.getElementsByTagName("button")[0];
var lastScore = document.getElementById("passScore");
var currentTestScore = document.getElementById("currentTestScore");

function changeTestScores() {
	lastScore.innerText = currentTestScore.innerText;
	currentTestScore.innerText = "0";
}





function createList() {
	
	xhttp.open("GET", "ajax/create_word_list/", true)
	
	
	body.style.cursor = "wait";
	button.style.cursor = "wait";
	
	xhttp.onreadystatechange = function() {
		if(xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 200){

		
			data = JSON.parse(xhttp.responseText);
			for (i =1; i < data.Words.length; i++) {
				
				var div = document.createElement("div");
				div.id = "status";
				var wordCell = tableRows[i].cells[0];
			
				currentWordDict = data.Words[i];
				key = Object.keys(currentWordDict);
				value = Object.values(currentWordDict);
				key = JSON.stringify(key[0]);
				wordDefinition = JSON.stringify(value[0]);
				
				word = key.replace(/"/g, "");
				
				wordCell.innerHTML = word.toUpperCase();
				wordCell.appendChild(div);
			}
		}
		body.style.cursor = "default";
		button.style.cursor = "pointer";
	};
	changeTestScores();
	lockEvaluator();
	xhttp.send();
	
	
}

	
	