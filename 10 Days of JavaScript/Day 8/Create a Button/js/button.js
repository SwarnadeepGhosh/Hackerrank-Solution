function myFunction(a){
	var current=document.getElementById('btn');
	current.innerHTML=parseInt(current.innerHTML)+1;
}

/*  
var btn = document.getElementById("btn");
	btn.addEventListener("click",function() {
		var current_value = this.innerHTML;
		this.innerHTML = parseInt(current_value)+1;
	});