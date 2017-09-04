var lastScore = document.getElementById("passScore");
var testScore = document.getElementById("currentTestScore");

function changeTestScores() {
	lastScore.innerText = testScore.innerText;
	testScore.innerText = "0";
}