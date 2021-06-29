function record(){

    var recognition = new webkitSpeechRecognition();
    recognition.lang = "en-GB";

    recognition.onresult = function(event) {
        var result = document.getElementById('speechToText').value = event.results[0][0].transcript;
       // console.log(result);
    }
    recognition.start();


    /*imgx = document.createElement("img");
    imgx.src = "microphone.gif";
    imgx.style.position = "absolute";
    imgx.style.top = "85px";
    imgx.style.left = "440px";
    imgx.id = "im";
    document.body.append(imgx);
     
    console.log("inside interact");
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recog = new SR();
   
    var xhr = new XMLHttpRequest();
   
   
    recog.onstart = () => console.log('speak');
   
    recog.onresult = function(event){
                    
                    document.getElementById("out").innerHTML = "";
                    document.getElementById("im").remove();
                   
                    
                    (async() => {
                      speak("Ok I will do that");
                      await sleep(3000);
                    
   
                    const current = event.resultIndex; 
                    const transcript = event.results[current][0].transcript;

                    console.log(transcript);
   
                    /*var queryString = "http://13.233.156.27/cgi-bin/interact.py?cmd=" + transcript;
                    xhr.open("GET", queryString, true);
                    xhr.send();
                    xhr.onload = function(){
                      var output = xhr.responseText;
                      document.getElementById("out").innerHTML = output;
                        
                    }
                   })()*/
      
                    
    }
   
    /*function speak(msg){
   
       const speech = new SpeechSynthesisUtterance();
       speech.text = msg;
       speech.volume = 1;
       speech.rate = 1;
       speech.pitch = 1;
       window.speechSynthesis.speak(speech);
    }
   
    const DEF_DELAY = 1000;
    function sleep(ms) {
       return new Promise(resolve => setTimeout(resolve, ms || DEF_DELAY));
    }
   
    //await sleep(100);
   
    (async()=>{
   
      speak("How can I help you");
      await sleep(3000);
      recog.start();
      await sleep(4000);
   
    })()
   }*/