function animate() {
    requestAnimationFrame(animate);
    let wind = parseFloat(document.getElementById('wind-v40').value);
    timeScale = parseFloat(document.getElementById('time-v40').value);
    document.getElementById('val-time-v40').innerText = timeScale.toFixed(2);
    let rad = parseFloat(document.getElementById('rad-v40').value);
    let h = parseFloat(document.getElementById('h-v40').value);
    let l_cm = parseFloat(document.getElementById('lev-v40').value)/100;
    let damp = parseFloat(document.getElementById('damp-v40').value);

    let estimatedRotorMass = (rad * h) * 30; 
    let momentOfInertia = estimatedRotorMass * rad * rad; 
    let aeroEfficiency = currentAngle / 50.0; 
    let aeroTorque = (wind * wind) * aeroEfficiency * (rad * h) * 1.5; 
    let frictionTorque = (currentRPM * 0.8) + (currentRPM > 0 ? 5.0 : 0); 
    
    // V5.0: Fyzika Generátora
    let Kv = 15.0; 
    let Kt = 60.0 / (2.0 * Math.PI * Kv); 
    let R_ph = 0.2; 
    
    let R_load = 5.0;
    let loadEl = document.getElementById('load-v44');
    if(loadEl) {
        R_load = parseFloat(loadEl.value);
        document.getElementById('val-load-v44').innerText = R_load.toFixed(1);
    }
    
    let E_emf = currentRPM / Kv;
    let I_gen = E_emf / (R_ph + R_load);
    let P_elec = I_gen * I_gen * R_load;
    let genTorque = Kt * I_gen;

    let voltsEl = document.getElementById('val-volts-v44');
    if(voltsEl) {
        voltsEl.innerText = E_emf.toFixed(1);
        document.getElementById('val-amps-v44').innerText = I_gen.toFixed(2);
        document.getElementById('val-watts-v44').innerText = Math.round(P_elec);
    }

    let netTorque = aeroTorque - frictionTorque - genTorque;
    let angularAcc = netTorque / momentOfInertia; 
    
    currentRPM += angularAcc * timeScale * 20; 
    if (currentRPM < 0) currentRPM = 0;

    let angularVel = (currentRPM * 2 * Math.PI) / 60;
    rotorGroup.rotation.y -= angularVel * 0.016 * timeScale;
    
    let govExt = Math.min(1.0, currentRPM / 450);
    currentAngle += (50 * (1 - govExt) - currentAngle) * (0.2 / damp) * timeScale;

    let isClosed = currentAngle < 5;
    let flowStateEl = document.getElementById("ui-flow-state-v40");
    if(flowStateEl) {
        if(isClosed) {
            flowStateEl.innerHTML = "<span style='color:#e74c3c;'>Analytické potenciálne obtekanie uzamknutého valca</span>";
        } else {
            flowStateEl.innerHTML = "<span style='color:#27ae60;'>Kolízne krídlové vírenie s odrazmi prúdnic</span>";
        }
    }

    let sR = rad + 0.6, hTS = h/2 + 0.5, hBS = -h/2 - 0.5, offset = parseFloat(document.getElementById('offset-v40').value);
    topHub.position.y = hTS; bottomHub.position.y = hBS; motorMesh.position.y = hBS - 0.25;
    for(let i=0; i<3; i++) {
        let a = (i * 120) * Math.PI / 180;
        let pT = new THREE.Vector3(Math.cos(a)*sR, hTS, -Math.sin(a)*sR);
        let pB = new THREE.Vector3(Math.cos(a)*sR, hBS, -Math.sin(a)*sR);
        alignCylinder(statorPillars[i], pB, pT);
        alignCylinder(topStruts[i], topHub.position, pT);
        alignCylinder(botStruts[i], bottomHub.position, pB);
        alignCylinder(mountLegs[i], pB, new THREE.Vector3(Math.cos(a)*(sR+0.5), hBS-1.5, -Math.sin(a)*(sR+0.5)));
    }

    shaftMesh.scale.set(1, h + 1.0, 1);
    topCollar.position.y = offset + 0.6; slidingCollar.position.y = offset - 0.3 + (govExt * 0.6);

    for(let i=0; i<6; i++) {
        let pRad = (currentAngle * Math.PI) / 180;
        pivotGroups[i].rotation.y = -pRad;
        pivotGroups[i].position.set(rad, 0, 0); 
        bladeMeshes[i].scale.set(rad, h, rad);

        alignCylinder(armsT[i], new THREE.Vector3(0, h/2, 0), new THREE.Vector3(rad, h/2, 0));
        alignCylinder(armsB[i], new THREE.Vector3(0, -h/2, 0), new THREE.Vector3(rad, -h/2, 0));
        
        let pPivot = new THREE.Vector3(rad, offset, 0);
        let lA = -pRad + Math.PI - 0.2;
        let pE = new THREE.Vector3(rad + Math.cos(lA)*l_cm, offset, -Math.sin(lA)*l_cm);
        alignCylinder(levers[i], pPivot, pE);
        alignCylinder(pushRods[i], new THREE.Vector3(0, slidingCollar.position.y, 0), pE);
    }

    for(let i=0; i<2; i++) {
        let gR = 0.3 + (govExt * 0.6); let midY = (topCollar.position.y + slidingCollar.position.y) / 2;
        govWeights[i].position.set(gR, midY, 0);
        alignCylinder(govArmsT[i], new THREE.Vector3(0, topCollar.position.y, 0), govWeights[i].position);
        alignCylinder(govArmsB[i], new THREE.Vector3(0, slidingCollar.position.y, 0), govWeights[i].position);
    }

    if(isCfd) {
        let U = wind === 0 ? 0.05 : wind * 0.1;
        let closedR = rad + 0.15, closedR2 = closedR * closedR;
        
        rotorGroup.updateMatrixWorld(true);
        let bladeSegments = [];
        let arcAngle = Math.PI / 6;
        let hX = -1 + Math.cos(arcAngle); let hZ = -Math.sin(arcAngle); 
        let tX = -1 + Math.cos(-arcAngle); let tZ = -Math.sin(-arcAngle); 

        for(let i=0; i<6; i++) {
            let mesh = bladeMeshes[i];
            let headPos = new THREE.Vector3(hX, 0, hZ).applyMatrix4(mesh.matrixWorld);
            let tailPos = new THREE.Vector3(tX, 0, tZ).applyMatrix4(mesh.matrixWorld);
            bladeSegments.push({x1: headPos.x, z1: headPos.z, x2: tailPos.x, z2: tailPos.z});
        }
        
        for(let s of streamlines) {
            let vx = U * s.baseSpeed; let vz = 0;
            let px = s.head.x; let pz = s.head.z;
            let r2 = px*px + pz*pz; let distToCenter = Math.sqrt(r2);
            let hitColor = 0x3498db;

            if (Math.abs(s.head.y) <= h/2) {
                if (isClosed) {
                    if (r2 < closedR2) { px = (px/distToCenter) * closedR; pz = (pz/distToCenter) * closedR; r2 = closedR2; }
                    vx = U * (1 - closedR2 * (px*px - pz*pz) / (r2*r2));
                    vz = U * (- closedR2 * (2*px*pz) / (r2*r2));
                    hitColor = 0xe74c3c;
                } else {
                    for(let b of bladeSegments) {
                        let distToBlade = distToSegment(px, pz, b.x1, b.z1, b.x2, b.z2);
                        if(distToBlade < 0.25) { 
                            let dx = b.x2 - b.x1; let dz = b.z2 - b.z1;
                            let len = Math.sqrt(dx*dx + dz*dz);
                            let nx = -dz/len; let nz = dx/len; 
                            if (nx*(px - b.x1) + nz*(pz - b.z1) < 0) { nx = -nx; nz = -nz; }
                            px += nx * (0.25 - distToBlade); pz += nz * (0.25 - distToBlade);
                            vx += nx * U * 2.5; vz += nz * U * 2.5;
                            hitColor = 0xf1c40f; 
                            break;
                        }
                    }
                    if (distToCenter <= rad && hitColor === 0x3498db) {
                        let angle = Math.atan2(pz, px);
                        let swirl = angularVel * distToCenter * 0.05;
                        vx += Math.sin(angle) * swirl; vz -= Math.cos(angle) * swirl;
                        hitColor = 0xe67e22;
                    }
                }
            }

            s.head.x = px + vx * timeScale; s.head.z = pz + vz * timeScale;
            s.head.y = s.yOffset + Math.sin(s.head.x * 2) * 0.1;

            if (timeScale > 0.001) {
                for(let j = TRAIL_LENGTH - 1; j > 0; j--) {
                    s.positions[j*3] = s.positions[(j-1)*3];
                    s.positions[j*3+1] = s.positions[(j-1)*3+1];
                    s.positions[j*3+2] = s.positions[(j-1)*3+2];
                }
                s.positions[0] = s.head.x; s.positions[1] = s.head.y; s.positions[2] = s.head.z;
                s.mesh.geometry.attributes.position.needsUpdate = true;
                s.mesh.material.color.setHex(hitColor);
            }

            if (s.head.x > 12 || Math.abs(s.head.z) > 10) { resetStreamline(s, -8, s.yOffset, (Math.random()-0.5)*12); }
        }
    }

    document.getElementById('val-wind-v40').innerText = wind.toFixed(1);
    document.getElementById('val-rotor-mass-v40').innerText = Math.round(estimatedRotorMass);
    document.getElementById('val-rpm-v40').innerText = Math.round(currentRPM);

    if (typeof initCharts === "function" && chartUpdateCounter === 0) { initCharts(); }
    if (typeof updateCharts === "function") {
        updateCharts(currentRPM, netTorque, wind, P_elec, rad, h, l_cm, parseFloat(document.getElementById('mass-v40').value), damp);
    }
    if (typeof updateAudio === "function") { updateAudio(wind, currentRPM); }

    renderer.render(scene, activeCamera);
}

initUI();
initScene();
animate();