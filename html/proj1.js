function clearCookies(){
	var cookies = document.cookie.split(";");
	for (var i = 0; i < cookies.length; i++){
		i = 0;
		var cookies = document.cookie.split(";");
		var onecook = cookies[i].split("=");
		console.log(onecook);
		deleteCookie(onecook[0]);
	}
}

function deleteCookie(cookiename){
	var max_age = ";max-age=0";
	var name = cookiename;
	var value = "";
	document.cookie = name + "=" + value + max_age + "; path =/";

}


function loadDataFunction(){
	// Instantiate an new XHR Object 
    const xhr = new XMLHttpRequest(); 

    // Open an object (GET/POST, PATH, ASYN-TRUE/FALSE) 
    // 2nd parameter is URL of API
    xhr.open("GET", "cgi-bin/readMessageTable.py", true); 

    // When response is ready 
    xhr.onload = function () { 

      //If the response is returned successfully
      if (this.status === 200) { 

        // Retrieve responseText and convert to JSON Object 
        console.log(this.responseText);
        obj = JSON.parse(this.responseText);
        console.log(obj);// Save a cookie with API info

        // Get table element - DOM node that will be used to put the whole data table on the page.
        var tableNode = document.getElementById("messageboard"); 
        var i = 1;
        //loop through JSON object
        for (key in obj) { 
          //create nodes
          var rowNode = document.createElement("tr");
          var user=document.createElement("td");
          var message=document.createElement("td");
          var timestamp=document.createElement("td");
          var center = document.createElement("center");

          //add data to nodes
          user.innerHTML=obj[key].User;
          message.innerHTML=obj[key].Message;
          timestamp.innerHTML=obj[key].Time;

          //link nodes together
          user.appendChild(center);
          rowNode.appendChild(user);
          rowNode.appendChild(message);
          rowNode.appendChild(timestamp);
          //load to the actual page
          tableNode.appendChild(rowNode);
		  
		  i += 1;        
        } 
      } 
      else { 
        console.log("Invalid data"); 
      } 
    } 
    xhr.send(); 
  } 

  function setCookie(cname, cvalue, exdays) {
      var d = new Date();
      d.setTime(d.getTime() + (exdays*24*60*60*1000));
      var expires = "expires="+ d.toUTCString();
      document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }