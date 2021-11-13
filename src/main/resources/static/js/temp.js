function Temp() {
    const test = () => {
        console.log("??");
        const $login = document.querySelector(".login");
        $login.innerHTML = `<h2 th:text="${userId}"></h2>`
    //<p>ID = ${model.id}</p>
    };
    this.init = () => {
        test();
    };
}


const temp = new Temp();
temp.init();