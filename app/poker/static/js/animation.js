import * as THREE from 'three';

export class AnimationM {
    async startGameAnimation(numPlayers, animationMixer, cardsParent) {

        const cards = cardsParent.children
        animationMixer.stopAllAction();
        const fillUp = numPlayers < 4
        const playerDiff = 4-numPlayers
        numPlayers = fillUp?numPlayers+playerDiff:numPlayers

        //personal cards
        for (let i = 0; i < numPlayers*2; i++) {
            if(fillUp && playerDiff>1){
                if(i% numPlayers+1===2 || i% numPlayers+1===3){ continue}
            } else if (fillUp){
                if(i% numPlayers+1===3){continue}
            }
            let animation = animationMixer.existingAction(`card_${i% numPlayers+1}.${Math.ceil((i+1) / numPlayers)}`);
            animation.clampWhenFinished = true;
            animation.loop = THREE.LoopOnce
            animation.enabled = true;
            cards[Math.ceil((i+1) / numPlayers)===1? i: i+7-numPlayers].visible = true;

            animation.play();
            await new Promise(resolve => {
                animationMixer.addEventListener("finished", async function(event){
                    animationMixer.removeEventListener('finished', this);
                    resolve();
                })
            });
        }
        //community cards
        const comCards = cards.slice(14, 19)
        let i = 0;
        cardsParent.animations.slice(14,19).forEach(clip => {
            const animation = animationMixer.existingAction(clip)
            animation.clampWhenFinished = true;
            animation.loop = THREE.LoopOnce
            comCards[i].visible = true;

            animation.play();
            i++;
        })

    }

    distributeRealCards(realCardsAll, cardsInfo, stage){
        switch (stage) {
            case "pre-f":
                //cardsInfo: [playerCard1, PlayerCard2, 3* communityCard]
                break
            case "f":
                break
            case "turn":
                break
            case "river":
                break
        }
    }
}