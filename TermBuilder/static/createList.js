
var xhttp = new XMLHttpRequest();
var table = document.getElementById("list");
var tableRows = table.getElementsByTagName('tr');

function createList() {
	if(tableRows.length > 0){
		for(i = tableRows.length -1; i>0; i--){
			table.removechild(tableRows[i]);
		}
	}
	xhttp.open("GET", "ajax/create_word_list/", true)
	xhttp.onreadystatechange = function() {
		if(xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 200){
			data = JSON.parse(xhttp.responseText);
			for (i =0; i < data.Words.length; i++) {
				var row = table.insertRow(i + 1);
				var wordCell = row.insertCell(0);
				var definitionCell = row.insertCell(1);
			
				currentWordDict = data.Words[i];
				key = Object.keys(currentWordDict);
				value = Object.values(currentWordDict);
				key = JSON.stringify(key[0]);
				wordDefinition = JSON.stringify(value[0]);
				
				word = key.replace(/"/g, "");
				wordDefinition = wordDefinition.replace(/"/g, "");
				
				wordCell.innerHTML = word.toUpperCase();
				definitionCell.innerHTML = wordDefinition.toUpperCase();
			}
		}
		header.style.textAlign = "center";
	};
	xhttp.send();
	
	
}

	
	