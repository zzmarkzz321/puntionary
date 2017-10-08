$(document).ready(function() {
	$("#submit").click(function() {
      var text = $("#input").val();
	  $.ajax({
			url: 'http://localhost:3000/test', 
			type : 'POST',
			contentType: 'application/json',
	    data: JSON.stringify({
	    	key: text
	    }),
	     success: function(res){
	       console.log("success!", res);
	      	
	       $("#test").text(res);
	     }
	      
		})
	})
})