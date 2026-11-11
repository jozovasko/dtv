function initUI() {
    document.getElementById("ui-title-v40").innerText = "VAWT G4.4: Gener\u00E1tor a Watty";
    document.getElementById("ui-wind-lbl-v40").innerText = "R\u00FDchlos\u0165 vetra (m/s):";
    document.getElementById("ui-time-lbl-v40").innerText = "Spomalenie \u010Dasu:";
    document.getElementById("ui-offset-lbl-v40").innerText = "V\u00FD\u0161kov\u00FD offset p\u00E1k (m):";
    
    var loadLbl = document.getElementById("ui-load-lbl-v44");
    if(loadLbl) {
        loadLbl.innerText = "Elektrick\u00E1 z\u00E1\u0165a\u017E (Odpor):";
        document.getElementById("ohm-sym-v44").innerText = "\u03A9";
        document.getElementById("ui-volts-lbl-v44").innerText = "Nap\u00E4tie(V)";
        document.getElementById("ui-amps-lbl-v44").innerText = "Pr\u00FAd(A)";
        document.getElementById("ui-watts-lbl-v44").innerText = "V\u00FDkon(W)";
    }

    var btnAudio = document.getElementById("btn-audio-v42");
    if(btnAudio) { btnAudio.innerText = "ZAPN\u00DA\u0164 ZVUK"; }

    document.getElementById("ui-mass-lbl-v40").innerText = "Hmota rotora:";
    document.getElementById("btn-cfd-v40").innerText = "CFD ZAPNUT\u00C9";
    document.getElementById("btn-proj-v40").innerText = "RE\u017EIM: PERSPEKT\u00CDVA";
    document.getElementById("btn-cam-top-v40").innerText = "Poh\u013Ead ZHORA";
    document.getElementById("btn-cam-side-v40").innerText = "Poh\u013Ead ZBOKU";
    document.getElementById("ui-dim-title-v40").innerText = "Kon\u0161truk\u010Dn\u00E9 parametre";
    document.getElementById("lbl-rad-v40").innerText = "Polomer r (m):";
    document.getElementById("lbl-h-v40").innerText = "V\u00FD\u0161ka h (m):";
    document.getElementById("lbl-lev-v40").innerText = "P\u00E1ka (cm):";
    document.getElementById("lbl-mass-v40").innerText = "Z\u00E1va\u017Eie (kg):";
    document.getElementById("lbl-damp-v40").innerText = "Tlmi\u010D (Hustota):";
}

window.toggleProjection = function() {
    isOrthographic = !isOrthographic;
    let oldCam = isOrthographic ? perspCamera : orthoCamera;
    let newCam = isOrthographic ? orthoCamera : perspCamera;
    newCam.position.copy(oldCam.position); newCam.quaternion.copy(oldCam.quaternion);

    if(isOrthographic) {
        const container = document.getElementById('canvas-v40');
        let aspect = container.clientWidth / container.clientHeight;
        let dist = oldCam.position.distanceTo(controls.target);
        let fov = perspCamera.fov * (Math.PI / 180);
        let h = 2 * Math.tan(fov / 2) * dist;
        orthoCamera.left = -h * aspect / 2; orthoCamera.right = h * aspect / 2;
        orthoCamera.top = h / 2; orthoCamera.bottom = -h / 2;
        orthoCamera.updateProjectionMatrix();
    }
    activeCamera = newCam; controls.object = activeCamera; controls.update();
    let btn = document.getElementById("btn-proj-v40");
    btn.innerText = isOrthographic ? "RE\u017EIM: ORTOGRAFICK\u00DD (CAD)" : "RE\u017EIM: PERSPEKT\u00CDVA";
    btn.style.background = isOrthographic ? "#8e44ad" : "#2c3e50";
}

window.toggleCFD = function() {
    isCfd = !isCfd; cfdGroup.visible = isCfd;
    let btn = document.getElementById("btn-cfd-v40");
    btn.innerText = isCfd ? "CFD ZAPNUT\u00C9" : "CFD VYPNUT\u00C9";
    btn.style.backgroundColor = isCfd ? "#3498db" : "#95a5a6";
}

window.setCameraView = function(type) {
    if(type==='top') { activeCamera.position.set(0, 16, 0.1); } 
    else { activeCamera.position.set(0, 0, 16); }
    controls.target.set(0,0,0);
    if(isOrthographic) { toggleProjection(); toggleProjection(); }
    controls.update();
}