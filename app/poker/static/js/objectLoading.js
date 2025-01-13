import * as THREE from 'three';
import {GLTFLoader} from "three/addons/loaders/GLTFLoader.js";

const manager = new THREE.LoadingManager();
const loadingContainer = document.getElementById('loading-container');
const loadingBar = document.getElementById('loading-bar');
const loadingText = document.getElementById('loading-text');

manager.onProgress = function (url, itemsLoaded, itemsTotal) {
  const progress = (itemsLoaded / itemsTotal) * 100;
  loadingBar.style.width = `${progress}%`;
  loadingText.innerText = `Loading... ${Math.round(progress)}%`;
};

function setupModel(gltf){
    const scene = gltf.scene;
    scene.animations = gltf.animations

    const mixer = new THREE.AnimationMixer(scene);
    gltf.animations.forEach(animation => {
        mixer.clipAction(animation)
    })

    return{
        scene,
        mixer
    }
}

export async function loadObjects() {
    loadingContainer.style.visibility = 'visible';

    //load generic models
    const gltfLoader = new GLTFLoader(manager);
    const urls = ['/poker/static/assets/Poker_Table_Export.glb', '/poker/static/assets/generic_cards.glb'];
    const prefixes = ['CLU', 'DIA', 'HEA', 'SPA']

    const[pokerTableData, genericCardsData] = await Promise.all([
        gltfLoader.loadAsync(urls[0]),
        gltfLoader.loadAsync(urls[1])
    ])

    //load real cards
    let realCardsData = [];
    for(const prefix of prefixes) {
        let loaders=[];
        for (let i = 1; i < 14; i++) {
            loaders.push(gltfLoader.loadAsync(`/poker/static/assets/poker_cards_export/${prefix}_${i<10?"0"+i: i}.glb`))
        }
        const cards = await Promise.all(loaders)
        realCardsData.push(cards)
    }

    //setting models up
    let realCardsAll = [];
    realCardsData.forEach(suit => {realCardsAll.push(suit.map(setupModel))});
    const pokerTableAll = setupModel(pokerTableData);
    const genericCardsAll = setupModel(genericCardsData);


    return {pokerTableAll, genericCardsAll}

}




