//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;

var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input; 							//MediaStreamAudioSourceNode we'll be recording

// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record

var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");
//var pauseButton = document.getElementById("pauseButton");
var submitButton = document.getElementById("submitButton");
//add events to those 2 buttons
recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
//pauseButton.addEventListener("click", pauseRecording);
submitButton.addEventListener("click", submitRecording);
function startRecording() {
	console.log("recordButton clicked");

	/*
		Simple constraints object, for more advanced audio features see
		https://addpipe.com/blog/audio-constraints-getusermedia/
	*/
    
    var constraints = { audio: true, video:false }

 	/*
    	Disable the record button until we get a success or fail from getUserMedia() 
	*/

	recordButton.disabled = true;
	stopButton.disabled = false;
	//pauseButton.disabled = false

	/*
    	We're using the standard promise based getUserMedia() 
    	https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
	*/

	navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
		console.log("getUserMedia() success, stream created, initializing Recorder.js ...");

		/*
			create an audio context after getUserMedia is called
			sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
			the sampleRate defaults to the one set in your OS for your playback device

		*/
		audioContext = new AudioContext();

		//update the format 
		document.getElementById("formats").innerHTML="Format: 1 channel pcm @ "+audioContext.sampleRate/1000+"kHz"

		/*  assign to gumStream for later use  */
		gumStream = stream;
		
		/* use the stream */
		input = audioContext.createMediaStreamSource(stream);

		/* 
			Create the Recorder object and configure to record mono sound (1 channel)
			Recording 2 channels  will double the file size
		*/
		rec = new Recorder(input,{numChannels:1})

		//start the recording process
		rec.record()

		console.log("Recording started");

	}).catch(function(err) {
	  	//enable the record button if getUserMedia() fails
    	recordButton.disabled = false;
    	stopButton.disabled = true;
    	//pauseButton.disabled = true
	});
}
/*
function pauseRecording(){
	console.log("pauseButton clicked rec.recording=",rec.recording );
	if (rec.recording){
		//pause
		rec.stop();
		//pauseButton.innerHTML="Resume";
	}else{
		//resume
		rec.record()
		//pauseButton.innerHTML="Pause";

	}
}
*/
function stopRecording() {
	console.log("stopButton clicked");

	//disable the stop button, enable the record too allow for new recordings
	stopButton.disabled = true;
	recordButton.disabled = false;
	//pauseButton.disabled = true;

	//reset button just in case the recording is stopped while paused
	//pauseButton.innerHTML="Pause";
	
	//tell the recorder to stop the recording
	rec.stop();

	//stop microphone access
	gumStream.getAudioTracks()[0].stop();

	//create the wav blob and pass it on to createDownloadLink
	rec.exportWAV(createDownloadLink);
}

function createDownloadLink(blob) {		//ol li 태그에서 div태그안에 바로 입력하는 방식으로 변경
	console.log("blob : ", blob);
	var url = URL.createObjectURL(blob);
	console.log("url : ", url);
	recordingsList = document.getElementById("recordingsList");
	recordingsList.innerHTML="";
	var au = document.createElement('audio');
	//var li = document.createElement('span');
	//var link = document.createElement('a');
	//var p = document.createElement('p');

	// var path = "D:\\코딩\\자바\\soundCode\\data\\";
	//name of .wav file to use during upload and download (without extendion)
	var filename = "User";

	//add controls to the <audio> element
	au.controls = true;
	au.src = url;

	//save to disk link
	//link.href = url;
	//link.download = filename + ".wav"; //download forces the browser to donwload the file using the  filename
	//link.innerHTML = "Save to disk";

	//add the new audio element to li
	recordingsList.appendChild(au);
	//li.appendChild(p);

	//add the filename to the li
	//li.appendChild(document.createTextNode(filename + ".wav "))

	//add the save to disk link to li
	//li.appendChild(link);

	//upload link
	var upload = document.createElement('button');
	// upload.href="test";
	upload.innerHTML = "Upload";
	upload.className = "control_btn"

	const formData = new FormData();
	formData.append("wav", blob, filename);

	// user 가져와야함


	upload.addEventListener("click", async function (event) {
		const response = await fetch("security/record", {
			method: 'POST',
			headers: {
				// 'content-type': 'multipart/form-data'
			},
			body: formData
		});

		console.log(response.json());
		alert("upload 완료!");

		// var xhr=new XMLHttpRequest();
		// xhr.onload=function(e) {
		//     if(this.readyState === 4) {
		//         console.log("Server returned: ",e.target.responseText);
		//     }
		// };
		// var fd = new FormData();
		// fd.append("audio_data", blob, filename);
		// xhr.open("POST","upload.php",true);
		// xhr.send(fd);
	});
	recordingsList.appendChild(document.createTextNode(" "))//add a space in between
	recordingsList.appendChild(upload)//add the upload link to li

}

async function submitRecording() {
	var userId = "security";
	const $pass = document.getElementById("pass");
	const $recognize = document.getElementById("recognize");
	const $stt = document.getElementById("stt");
	$pass.className = "result_item";
	$recognize.className = "result_item";
	$stt.className = "result_item";


	// submitButton.addEventListener("click", async function (event) {
		await fetch(`authenticate?name=${userId}`, {
			method: 'GET',
			headers: {
				'content-type': 'application/json'
			}
		}).then(data => data.json())
			.then(data => {
				console.log(data);

				if (`${data.pass}` == 'true') {
					$pass.innerHTML = `결과 : 2차 인증 성공!!`;
				} else {
					$pass.innerHTML = `결과 : 2차 인증 실패...`;
				}
				$recognize.innerHTML = `성문 유사성 : ${data.recognize}%`;
				$stt.innerHTML = `텍스트 유사성 : ${data.stt}%`;
		});
	// });


	// window.location.href = '/';
}