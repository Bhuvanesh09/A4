	var Useranswers=[];
    var feedback = [];
    var correct_answers=[];
    
	var getUserAnswers = function(){
		score = 0;
    	for(let i=1;i<=4;i++){
			var checked = document.getElementsByName("question"+i);
    		checked.forEach(option=>{
    			if(option.checked) {
					let ans = document.getElementById("answer"+i).value;
					console.log("User Entered : " + option.value)
					console.log("Correct Answer : " + ans)
					if(option.value == ans) {
						score = score + 1 ;
					}
				}
    		});
		}
		alert("you have scored, "+score);
		
    }

    var checkAnswers = function(){
    	console.log("ran");
    	var score=0;
    	for(let i=0;i<4;i++)
    		if(correct_answers[i]==Useranswers[i])	score++;
    	alert("you have scored, "+score);
    }

    function gradeit(){
    	// alert("clicked!!");
    	getUserAnswers();
    	//checkAnswers();
    }