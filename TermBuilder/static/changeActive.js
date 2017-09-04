
var title = document.getElementsByTagName("title")[0];
var lists = document.getElementsByTagName("ul");
var header = lists[0];
var navs = header.getElementsByTagName("li");

if(title.innerHTML == "Study") {
	navs[0].className = "";
	navs[1].className = "active";
}

else if(title.innerHTML == "Test") {
	navs[0].className = "";
	navs[1].className = "";
	navs[2].className = "active";
}