function controlMusic(action) {
  fetch(`/${action}`, { method: "POST" })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      alert(`${action} command sent!`);
    })
    .catch((error) => console.error("Error:", error));
}

function startVoice() {
  if (!("webkitSpeechRecognition" in window)) {
    alert("Your browser doesn't support speech recognition.");
    return;
  }

  const recognition = new webkitSpeechRecognition();
  recognition.lang = "en-US";
  recognition.start();

  document.getElementById("voice-status").innerText = "Listening... 🎙️";

  recognition.onresult = function (event) {
    const command = event.results[0][0].transcript.toLowerCase();
    document.getElementById(
      "voice-status"
    ).innerText = `You said: "${command}"`;

    if (command.includes("play")) {
      controlMusic("play");
    } else if (command.includes("pause")) {
      controlMusic("pause");
    } else if (command.includes("next")) {
      controlMusic("next");
    } else if (command.includes("previous")) {
      controlMusic("previous");
    } else {
      alert("Command not recognized.");
    }
  };

  recognition.onerror = function (event) {
    console.error(event.error);
    document.getElementById("voice-status").innerText =
      "Voice recognition error.";
  };
}
