function Code() {

    const makeCode = async () => {
        const $code = document.getElementById("code");
        await fetch("/getKey", {
            method: "GET",
            headers: {
                'content-type': 'application/json'
            }
        }).then(data => data.json())
            .then(data => {
            $code.innerHTML = `<strong>암호 : ${data.key}</strong>`;
        });
    };

    this.init = () => {
        makeCode();
    };
}

const code = new Code();
code.init()