function Login() {
    const test = () => {
        alert("로그인 완료!");
        window.location.href = '/';
        //<p>ID = ${model.id}</p>
    };
    this.init = () => {
        test();
    };
}


const temp = new Login();
temp.init();