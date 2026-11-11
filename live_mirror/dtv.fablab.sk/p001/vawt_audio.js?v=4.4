function toggleAudio() {
    var btn = document.getElementById("btn-audio-v42");
    
    if (!audioInitialized) {
        var AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
        
        var bufferSize = audioCtx.sampleRate * 2; 
        var noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
        var output = noiseBuffer.getChannelData(0);
        for (var i = 0; i < bufferSize; i++) { output[i] = Math.random() * 2 - 1; }
        var noiseSource = audioCtx.createBufferSource();
        noiseSource.buffer = noiseBuffer;
        noiseSource.loop = true;
        
        windFilter = audioCtx.createBiquadFilter();
        windFilter.type = 'lowpass';
        windFilter.frequency.value = 400; 
        
        windGain = audioCtx.createGain();
        windGain.gain.value = 0; 
        
        noiseSource.connect(windFilter);
        windFilter.connect(windGain);
        windGain.connect(audioCtx.destination);
        noiseSource.start();

        bladeOsc = audioCtx.createOscillator();
        bladeOsc.type = 'sawtooth';
        bladeOsc.frequency.value = 50; 
        
        var bladeFilter = audioCtx.createBiquadFilter();
        bladeFilter.type = 'lowpass';
        bladeFilter.frequency.value = 600;
        
        bladeGain = audioCtx.createGain();
        bladeGain.gain.value = 0; 
        
        bladeOsc.connect(bladeFilter);
        bladeFilter.connect(bladeGain);
        bladeGain.connect(audioCtx.destination);
        bladeOsc.start();
        
        audioInitialized = true;
        isAudioPlaying = true;
        
        if(btn) {
            btn.innerText = "ZVUK ZAPNUT\u00DD";
            btn.style.backgroundColor = "#27ae60"; 
        }
    } else {
        if (isAudioPlaying) {
            audioCtx.suspend();
            isAudioPlaying = false;
            if(btn) {
                btn.innerText = "ZVUK VYPNUT\u00DD";
                btn.style.backgroundColor = "#e74c3c"; 
            }
        } else {
            audioCtx.resume();
            isAudioPlaying = true;
            if(btn) {
                btn.innerText = "ZVUK ZAPNUT\u00DD";
                btn.style.backgroundColor = "#27ae60"; 
            }
        }
    }
}

function updateAudio(windSpeed, rpm) {
    if (!audioInitialized || !audioCtx || !isAudioPlaying) return;
    var time = audioCtx.currentTime;
    
    var maxWind = 36.0;
    var windNorm = Math.min(windSpeed / maxWind, 1.0);
    windGain.gain.setTargetAtTime(windNorm * 0.4, time, 0.1);
    windFilter.frequency.setTargetAtTime(300 + (windNorm * 2000), time, 0.1);
    
    var maxRpm = 600.0;
    var rpmNorm = Math.min(rpm / maxRpm, 1.0);
    if (rpm > 1) {
        bladeGain.gain.setTargetAtTime(rpmNorm * 0.25, time, 0.1);
        bladeOsc.frequency.setTargetAtTime(20 + (rpmNorm * 180), time, 0.1);
    } else {
        bladeGain.gain.setTargetAtTime(0, time, 0.1);
    }
}