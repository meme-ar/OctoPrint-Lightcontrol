console.log('light control plugin js');
const lightBtn = document.querySelector('#light-toggle');
let lightStatus = 0
window.onload = async function () {
    const res = await fetch("/api/plugin/lightcontrol", {
        method: "GET"
    })
    const lightStatus = await res.json();

    if (lightStatus.status === 1) {
        console.log('lightStatus 1');
        lightBtn.innerHTML = '<i class="fa fa-solid fa-lightbulb"></i>'
    } else if (lightStatus.status === 0)  {

        console.log('lightStatus 0');
        lightBtn.innerHTML = '<i class="far fa-regular fa-lightbulb"></i>'
    }
};

lightBtn.addEventListener("click", async () => {
    const res = await fetch("/api/plugin/lightcontrol", {
        body: JSON.stringify({ "command": "toggle" }),
        credentials: 'omit',
        headers: {
            "Content-Type": "application/json"
        },
        method: "POST"
    })
    const postRes = await res.json();
    
    if (postRes.status === 1) {
        console.log('lightStatus 1');
        lightBtn.innerHTML = '<i class="fa fa-solid fa-lightbulb"></i>'
    } else if (postRes.status === 0) {

        console.log('lightStatus 0');
        lightBtn.innerHTML = '<i class="far fa-regular fa-lightbulb"></i>'
    }
});