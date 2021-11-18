function Register() {
    const test = () => {
        alert("회원가입 완료!");
        window.location.href = '/';
    //<p>ID = ${model.id}</p>
    };


    const trainModel = async () => {
        await fetch("/trainModel",{
            method: "GET",
            headers:{
                'content-type': 'application/json'
            }
        })

    };
    this.init = () => {
        test();
        trainModel();
    };
}


const temp = new Register();
temp.init();