import * as THREE from 'three';

export function createScene() {
    const gameWindow = document.getElementById('render-target');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, gameWindow.innerWidth / gameWindow.innerHeight, 0.1, 1000);

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(gameWindow.offsetWidth, gameWindow.offsetHeight);
    gameWindow.appendChild(renderer.domElement);

    function draw(){
        renderer.render(scene, camera);
    }

    function start(){
        renderer.setAnimationLoop(draw)
    }

    return {
        start
    }

}