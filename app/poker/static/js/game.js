import * as THREE from 'three';
import {OrbitControls} from "three/addons/controls/OrbitControls.js";
import {AnimationM} from "./animation.js";
import {loadObjects} from "./objectLoading.js";


export class Scene {
    #importedObjects; #scene; #camera; #renderer; #AnimationManager
    constructor() {
        //Scene setup
        this.clock = new THREE.Clock();

        const aspectRatio = 16 / 9;
        const gameWindow = document.getElementById('render-target');
        this.#scene = new THREE.Scene();
        this.#camera = new THREE.PerspectiveCamera(75, aspectRatio, 0.1, 1000);
        this.#camera.position.set(-0.675, 2, 0);
        this.#camera.lookAt(new THREE.Vector3(0.6, -0.91, 0));

        this.#renderer = new THREE.WebGLRenderer({antialias: true, canvas: gameWindow});
        window.addEventListener('resize', ()=>{this.resizeCanvas();});

        //const controls = new OrbitControls(this.#camera, this.#renderer.domElement);

        const ambientLight = new THREE.AmbientLight(0xffffff, 1);
        this.#scene.add(ambientLight);

        const gridhelper = new THREE.GridHelper();
       //this.#scene.add(gridhelper);

        this.#AnimationManager = new AnimationM()
        window.addEventListener('keydown', async (event) => {
            if (event.key === 'Enter') {
                await this.#AnimationManager.startGameAnimation(2, this.#importedObjects.genericCardsAll.mixer, this.#importedObjects.genericCardsAll.scene)
            }
        });



    }
    resizeCanvas() {
        const canvas = this.#renderer.domElement;
        let width = canvas.clientWidth;
        let height = canvas.clientHeight;
        if (canvas.width !== width || canvas.height !== height) {
            this.#renderer.setSize(width, height, false);
            this.#camera.aspect = width / height;
            this.#camera.updateProjectionMatrix();

        }
    }

    draw(){
        const delta = this.clock.getDelta()
        this.#importedObjects.genericCardsAll.mixer.update(delta)
        this.#renderer.render(this.#scene, this.#camera)
    }
    async initialize(){
        //async Scene setup
        this.#importedObjects = await loadObjects(this.#scene);
        this.#importedObjects.genericCardsAll.scene.children.forEach(child => {child.visible = false});
        this.#scene.add(this.#importedObjects.pokerTableAll.scene, this.#importedObjects.genericCardsAll.scene)

    }

    start(){
        this.resizeCanvas()
        this.#renderer.setAnimationLoop(() => {this.draw()});
         document.getElementById('loading-container').style.visibility = 'hidden';
    }
    
}