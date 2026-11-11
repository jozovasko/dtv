function initUI() {
    document.getElementById("ui-title-v40").innerText = "VAWT V5.2: Autonómny systém";
    document.getElementById("ui-wind-lbl-v40").innerText = "Rýchlosť vetra (m/s):";
    document.getElementById("ui-time-lbl-v40").innerText = "Spomalenie času:";
    document.getElementById("ui-offset-lbl-v40").innerText = "Výškový offset pák (m):";
    
    var loadLbl = document.getElementById("ui-load-lbl-v44");
    if(loadLbl) {
        loadLbl.innerText = "Elektrická záťaž (Odpor):";
        document.getElementById("ohm-sym-v44").innerText = "Ω";
        document.getElementById("ui-volts-lbl-v44").innerText = "Napätie (V)";
        document.getElementById("ui-amps-lbl-v44").innerText = "Prúd (A)";
        document.getElementById("ui-watts-lbl-v44").innerText = "Výkon (W)";
    }

    var btnAudio = document.getElementById("btn-audio-v42");
    if(btnAudio) { btnAudio.innerText = "ZAPNÚŤ ZVUK"; }

    document.getElementById("ui-mass-lbl-v40").innerText = "Hmota rotora:";
    document.getElementById("btn-cfd-v40").innerText = "CFD ZAPNUTÉ";
    document.getElementById("btn-proj-v40").innerText = "REŽIM: PERSPEKTÍVA";
    document.getElementById("btn-cam-top-v40").innerText = "Pohľad ZHORA";
    document.getElementById("btn-cam-side-v40").innerText = "Pohľad ZBOKU";
    document.getElementById("ui-dim-title-v40").innerText = "Konštrukčné parametre";
    document.getElementById("lbl-rad-v40").innerText = "Polomer r (m):";
    document.getElementById("lbl-h-v40").innerText = "Výška h (m):";
    document.getElementById("lbl-lev-v40").innerText = "Páka (cm):";
    document.getElementById("lbl-mass-v40").innerText = "Závažie (kg):";
    document.getElementById("lbl-damp-v40").innerText = "Tlmič (Hustota):";
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
    btn.innerText = isOrthographic ? "REŽIM: ORTOGRAFICKÝ (CAD)" : "REŽIM: PERSPEKTÍVA";
    btn.style.background = isOrthographic ? "#8e44ad" : "#2c3e50";
}

window.toggleCFD = function() {
    isCfd = !isCfd; cfdGroup.visible = isCfd;
    let btn = document.getElementById("btn-cfd-v40");
    btn.innerText = isCfd ? "CFD ZAPNUTÉ" : "CFD VYPNUTÉ";
    btn.style.backgroundColor = isCfd ? "#3498db" : "#95a5a6";
}

window.setCameraView = function(type) {
    if(type==='top') { activeCamera.position.set(0, 16, 0.1); } 
    else { activeCamera.position.set(0, 0, 16); }
    controls.target.set(0,0,0);
    if(isOrthographic) { toggleProjection(); toggleProjection(); }
    controls.update();
}

window.openDocs = function() {
    document.getElementById('docs-modal').style.display = 'flex';
}

window.closeDocs = function() {
    document.getElementById('docs-modal').style.display = 'none';
}