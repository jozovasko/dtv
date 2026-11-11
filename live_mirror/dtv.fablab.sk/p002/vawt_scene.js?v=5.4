function initScene() {
    const container = document.getElementById('canvas-v40');
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xffffff);

    let aspect = container.clientWidth / container.clientHeight;
    perspCamera = new THREE.PerspectiveCamera(40, aspect, 0.1, 1000);
    perspCamera.position.set(8, 10, 12);
    
    let frustumSize = 7.0;
    orthoCamera = new THREE.OrthographicCamera(-frustumSize * aspect / 2, frustumSize * aspect / 2, frustumSize / 2, -frustumSize / 2, 0.1, 1000);
    orthoCamera.position.set(8, 10, 12);
    activeCamera = perspCamera;

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    controls = new THREE.OrbitControls(activeCamera, renderer.domElement);
    scene.add(new THREE.AmbientLight(0xffffff, 0.7));
    const sun = new THREE.DirectionalLight(0xffffff, 1); sun.position.set(10, 20, 10); scene.add(sun);

    const matStator = new THREE.MeshStandardMaterial({ color: 0x7f8c8d });
    const matRotor = new THREE.MeshStandardMaterial({ color: 0x2c3e50, metalness: 0.6, roughness: 0.2 });
    const matBlade = new THREE.MeshStandardMaterial({ color: 0x3498db, transparent: true, opacity: 0.55, side: THREE.DoubleSide });
    const matMech = new THREE.MeshStandardMaterial({ color: 0xd35400 });

    statorGroup = new THREE.Group(); scene.add(statorGroup);
    rotorGroup = new THREE.Group(); scene.add(rotorGroup);
    cfdGroup = new THREE.Group(); scene.add(cfdGroup);

    for(let i=0; i<300; i++) {
        let geo = new THREE.BufferGeometry();
        let positions = new Float32Array(TRAIL_LENGTH * 3);
        let startX = (Math.random() - 0.5) * 18, startY = (Math.random() - 0.5) * 5, startZ = (Math.random() - 0.5) * 12;
        for(let j=0; j<TRAIL_LENGTH; j++) { positions[j*3] = startX; positions[j*3+1] = startY; positions[j*3+2] = startZ; }
        geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        let mat = new THREE.LineBasicMaterial({ color: 0x3498db, linewidth: 2, transparent: true, opacity: 0.7 });
        let line = new THREE.Line(geo, mat);
        streamlines.push({ mesh: line, positions: positions, head: new THREE.Vector3(startX, startY, startZ), yOffset: startY, baseSpeed: Math.random() * 0.5 + 0.5 });
        cfdGroup.add(line);
    }

    topHub = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.18, 0.2, 16), matStator); statorGroup.add(topHub);
    bottomHub = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 0.2, 16), matStator); statorGroup.add(bottomHub);
    motorMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 0.3, 32), new THREE.MeshStandardMaterial({color: 0x34495e})); statorGroup.add(motorMesh);

    const strutGeo = new THREE.CylinderGeometry(0.04, 0.04, 1, 8);
    for(let i=0; i<3; i++) {
        statorPillars.push(new THREE.Mesh(strutGeo, matStator)); statorGroup.add(statorPillars[i]);
        topStruts.push(new THREE.Mesh(strutGeo, matStator)); statorGroup.add(topStruts[i]);
        botStruts.push(new THREE.Mesh(strutGeo, matStator)); statorGroup.add(botStruts[i]);
        mountLegs.push(new THREE.Mesh(strutGeo, matStator)); statorGroup.add(mountLegs[i]);
    }

    shaftMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 1, 16), matRotor); rotorGroup.add(shaftMesh);

    const shape = new THREE.Shape();
    const arcAngle = Math.PI / 6; 
    shape.absarc(-1, 0, 1, arcAngle, -arcAngle, true); 
    let headX = -1 + Math.cos(arcAngle); let headY = Math.sin(arcAngle);
    shape.quadraticCurveTo(-0.6, 0, headX, headY); 

    const bladeGeo = new THREE.ExtrudeGeometry(shape, { depth: 1, bevelEnabled: false, curveSegments: 32 });
    bladeGeo.translate(0, 0, -0.5); 
    bladeGeo.rotateX(Math.PI/2); 

    const linkGeo = new THREE.CylinderGeometry(0.015, 0.015, 1, 8);
    for(let i=0; i<6; i++) {
        let pObj = new THREE.Group(); pObj.rotation.y = -(i * Math.PI / 3);
        let pivot = new THREE.Group(); 
        let bMesh = new THREE.Mesh(bladeGeo, matBlade); pivot.add(bMesh);
        bladeMeshes.push(bMesh); pivotGroups.push(pivot); pObj.add(pivot);
        
        armsT.push(new THREE.Mesh(linkGeo, matRotor)); pObj.add(armsT[i]);
        armsB.push(new THREE.Mesh(linkGeo, matRotor)); pObj.add(armsB[i]);
        levers.push(new THREE.Mesh(linkGeo, matMech)); pObj.add(levers[i]);
        pushRods.push(new THREE.Mesh(linkGeo, matMech)); pObj.add(pushRods[i]);
        rotorGroup.add(pObj);
    }

    topCollar = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.1, 16), matRotor); rotorGroup.add(topCollar);
    slidingCollar = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.1, 16), matMech); rotorGroup.add(slidingCollar);

    for(let i=0; i<2; i++) {
        let gG = new THREE.Group(); gG.rotation.y = i * Math.PI;
        govWeights.push(new THREE.Mesh(new THREE.SphereGeometry(0.18, 16, 16), matMech)); gG.add(govWeights[i]);
        govArmsT.push(new THREE.Mesh(linkGeo, matRotor)); gG.add(govArmsT[i]);
        govArmsB.push(new THREE.Mesh(linkGeo, matRotor)); gG.add(govArmsB[i]);
        rotorGroup.add(gG);
    }

    window.addEventListener('resize', onWindowResize, false);
}

function onWindowResize() {
    const container = document.getElementById('canvas-v40');
    let aspect = container.clientWidth / container.clientHeight;
    perspCamera.aspect = aspect; perspCamera.updateProjectionMatrix();
    let fSize = 7.0;
    orthoCamera.left = -fSize * aspect / 2; orthoCamera.right = fSize * aspect / 2;
    orthoCamera.top = fSize / 2; orthoCamera.bottom = -fSize / 2;
    orthoCamera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
}