function Register() {
    const test = () => {
        alert("회원가입 완료!");
        window.location.href = '/';
    //<p>ID = ${model.id}</p>
    };
    this.init = () => {
        test();
    };
}


const temp = new Register();
temp.init();