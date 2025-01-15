
window.addEventListener('ready', NetworkHandler)
function NetworkHandler() {
    const socketio = io();

    socketio.on('start', (data) => {

    })

    socketio.on("game_update", (data) => {

    })


    socketio.on("allow_turn", async () => {
        window.dispatchEvent(new Event('toggleTurn'))

        await new Promise(resolve => {
            window.addEventListener('fold', fold)
            window.addEventListener('raise', raise)
            window.addEventListener('call', call)
        })
    });


    function raise(event) {
        window.removeEventListener("fold", fold)
        window.removeEventListener("raise", raise)
        window.removeEventListener("call", call)
        socketio.emit("game_action", "raise", event.value);
        resolve();
    }

    function call() {
        window.removeEventListener("fold", fold)
        window.removeEventListener("raise", raise)
        window.removeEventListener("call", call)
        socketio.emit("call");
        resolve();
    }

    function fold() {
        window.removeEventListener("fold", fold)
        window.removeEventListener("raise", raise)
        window.removeEventListener("call", call)
        socketio.emit("fold");
        resolve();
    }
}