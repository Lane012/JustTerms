
var words = document.getElementsByClassName("word");
var definitions = document.getElementsByClassName("definition");
var lists = document.getElementsByTagName("ul");
var header = lists[0];
var navs = header.getElementsByTagName("li");
navs[0].className = "";
navs[1].className = "active";


for (i =1; i < words.length; i++) {
	currentWord = words[i];
	currentWord.style.display = "none";
}

for (i =0; i < definitions.length; i++) {
	currentDef = definitions[i];
	currentDef.style.display = "none";
}
