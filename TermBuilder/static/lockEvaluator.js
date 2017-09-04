

function lockEvaluator() {
	
	
	
	var testData = document.getElementById("testScore");
	var listCreator = document.getElementById("createNewList");
	var lock = document.getElementById("lock");
	
	var buttonText = listCreator.childNodes[0];
	
	
	
	testData = testData.innerHTML;
	testScore = testData.match(/\d+/);
	
	if(testScore < 70) {
		listCreator.disabled = true;
		listCreator.style.cursor = "default";
		listCreator.onmouseover = function() {
			this.fontSize = "10px";
			buttonText.nodeValue = "This button locked until test passed with 70 or higher";
		}
		listCreator.onmouseout = function() {
			buttonText.nodeValue = "Create New Word List";
		}
		
		lock.style.display = "";
	}
	else {
		lock.style.display = "none";
	}
}
	
	

