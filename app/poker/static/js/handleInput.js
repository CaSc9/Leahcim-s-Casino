
    const gameWindow =document.getElementsByClassName("game-container")[0];
    const raiseBtn = document.getElementById('raise-btn');
    const raiseSliderContainer = document.getElementById('raise-slider-container');
    const raiseSlider = document.getElementById('raise-slider');
    const raiseValue = document.getElementById('raise-value');
    const foldBtn = document.getElementById('fold-btn');
    const callBtn= document.getElementById('call-btn');
    let isConfirm = false;
    let isTurn = true;

    window.addEventListener('toggleTurn', ()=>{
        if(isTurn){
            gameWindow.querySelectorAll('button').forEach((button)=>{
                button.disabled = true;
                isTurn = false;
            })
        } else {
            gameWindow.querySelectorAll('button').forEach((button)=>{
                button.disabled = false;
                isTurn = true;
            })
        }
    })

    raiseSlider.addEventListener('blur', (event)=>{
        foldBtn.disabled = callBtn.disabled = !foldBtn.disabled
        raiseBtn.textContent = "Raise"
        isConfirm = event.relatedTarget === raiseBtn;
        raiseSliderContainer.style.display = 'none';
    });

    raiseBtn.addEventListener('click', handleRaise);

    raiseSlider.addEventListener('input', () => {
        raiseValue.textContent = raiseSlider.value;
    });

    foldBtn.addEventListener('click', ()=>{
        window.dispatchEvent(new Event('fold'))
        window.dispatchEvent(new Event('toggleTurn'));
    })
     callBtn.addEventListener('click', ()=>{
        window.dispatchEvent(new Event('call'))
        window.dispatchEvent(new Event('toggleTurn'));
    })

    function handleRaise(){
        //detach old raise event
        if (!isConfirm){
            raiseBtn.textContent = "Confirm";
            isConfirm = true;
            raiseSliderContainer.style.display = 'flex';
            foldBtn.disabled = callBtn.disabled = true;
        } else{
            raiseBtn.textContent = "Raise"
            window.dispatchEvent(new CustomEvent('raise', {value: raiseValue.value}));
            isConfirm = false;
            raiseSliderContainer.style.display = 'none';
            foldBtn.disabled = callBtn.disabled = false;
            window.dispatchEvent(new Event('toggleTurn'));
        }

    }
