
var TestResults = {};
var frames = document.getElementsByClassName("main");

function parse_cookies() {
    var cookies = {};
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function (c) {
            var m = c.trim().match(/(\w+)=(.*)/);
            if(m !== undefined) {
                cookies[m[1]] = decodeURIComponent(m[2]);
            }
        });
    }
    return cookies;
}
var cookies = parse_cookies();

var TestData =  { 
	counter : 1,
	countUp : function() {
		return this.counter++;
	},
	testScore : 0,
	addToTestScore : function() {
		this.testScore = this.testScore + 1;
	},
	getTestScore : function() {
		return this.testScore;
	},
};

var num = document.getElementsByClassName("questionNum")[0];
num.innerHTML = TestData.counter;


function answerChecker(guess) {
	evaluateGuess(guess);
}


function countUp() {
	num = document.getElementsByClassName("questionNum");
	currentNum = num[TestData.counter];
	currentNum.innerHTML = TestData.countUp();
}

function nextQuestion() {
	var currentQuestion = document.getElementsByClassName("definition")[TestData.counter -1];
	currentQuestion  = formatQuestion(currentQuestion);
	return currentQuestion;
}

function formatQuestion(question){
	currentQuestion = question.innerText.replace(/[0-9]/g, '');
	currentQuestion = currentQuestion.trim();
	
	return currentQuestion;
}
	
	
	

function evaluateGuess(guessButton) {
	var question = nextQuestion();
	guess = guessButton.innerText;
	for(i = 0; i < answers.length; i++) {
		if(guess === answers[i]) {
			if(question === questions[i]) {
				TestData[question] = "correct";
				TestData.addToTestScore();
				disableButtons();
				guessButton.style.backgroundColor = "green";
				
				break;
			}
			else{
				TestData[question] = "incorrect";
				guessButton.style.backgroundColor = "red";
				highlightCorrectAnswer(question);
				disableButtons();
				break;
			}
		}
	}
	setTimeout(function() { changeFrame()}, 1000);
}


function addToTestScore() {
	TestData.testScore = TestData.testScore + 1;
}

	

function changeFrame() {
	currentFrame = getCurrentFrame();
	currentFrame.style.display = "none";
	
	nextFrame();
}

function getCurrentFrame() {
	currentFrame = frames[TestData.counter -1];
	return currentFrame;
}
	

function highlightCorrectAnswer(question) {
	currentFrame = getCurrentFrame();
	options = currentFrame.getElementsByClassName("col-12 options");
	
	for(i = 0; i < options.length; i++) {
		currentButton = options[i];
		currentOption = currentButton.innerHTML;
		for(answerIndex = 0; answerIndex < answers.length; answerIndex++){
			currentAnswer = answers[answerIndex];
			
			if(currentOption === currentAnswer) {
				answerDefinition = questions[answerIndex];
				
				if(answerDefinition === question) {
					currentButton.style.backgroundColor = "green";
				}
			}
		}			
	}
	
	
}


function nextFrame() {
	if(TestData.counter === 20) {
		displayTestScore();
		sendTestData();
		disableButtons();
		showResults();
		return;
	}
	next = frames[TestData.counter];
	next.style.display = '';
	var num = document.getElementsByClassName("questionNum")[TestData.counter];
	TestData.countUp();
	
	num.innerHTML = TestData.counter;
}

function displayTestScore() {
	alert("you scored a" + " " + (TestData.getTestScore() / 20)* 100 + "!");
}

function showResults() {
	var frames = document.getElementsByClassName("main");
	for(i =0; i < frames.length; i++) {
		currentFrame = frames[i];
		currentFrame.style.display = "";
	}
}

function disableButtons() {
	currentFrame = getCurrentFrame();
	options = currentFrame.getElementsByClassName("col-12 options");
	
	for(i = 0; i < options.length; i++) {
		option = options[i];
		
		option.removeAttribute("onclick");
	}
}


function sendTestData() {
	var testScore = TestData.getTestScore().toString();
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "ajax/test_score_update/", true);
	xhttp.setRequestHeader('X-CSRFToken', cookies['csrftoken']);
	xhttp.send(testScore);

}
	
	
	
	
	
	
	
	
	




	


	


	