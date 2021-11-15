const $userInfo = document.querySelector(".user_info");


function Index() {
    const mypage_check = () => {
        var userId = window.sessionStorage.getItem("userId");

        if(userId!=null){
            $userInfo.innerHTML = `${userId}`;
        }
    };
    this.init = () => {
        mypage_check();
    };
}


const temp = new Index();
temp.init();