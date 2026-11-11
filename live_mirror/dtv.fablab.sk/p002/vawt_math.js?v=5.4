function distToSegment(px, pz, ax, az, bx, bz) {
    let l2 = (bx - ax)*(bx - ax) + (bz - az)*(bz - az);
    if (l2 === 0) return Math.sqrt((px-ax)*(px-ax) + (pz-az)*(pz-az));
    let t = ((px - ax) * (bx - ax) + (pz - az) * (bz - az)) / l2;
    t = Math.max(0, Math.min(1, t));
    let projX = ax + t * (bx - ax);
    let projZ = az + t * (bz - az);
    return Math.sqrt((px - projX)*(px - projX) + (pz - projZ)*(pz - projZ));
}

function alignCylinder(mesh, p1, p2) {
    let d = p1.distanceTo(p2);
    mesh.scale.set(1, Math.max(d, 0.01), 1);
    mesh.position.copy(p1.clone().lerp(p2, 0.5));
    if(d > 0.001) mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), p2.clone().sub(p1).normalize());
}

function resetStreamline(s, x, y, z) {
    s.head.set(x, y, z);
    for(let j=0; j<TRAIL_LENGTH; j++) {
        s.positions[j*3] = x; s.positions[j*3+1] = y; s.positions[j*3+2] = z;
    }
}