

const form = document.querySelector(".signup form"),
continueBtn = form.querySelector(".button input");

form.onsubmit = (e)=>{
    e.preventDefault(); //prevent submit

}
continueBtn.onclick = ()=> {

    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'php/signup.php', true);

    xhr.onload =()=> {
        if (xhr.readyState == XMLHttpRequest.DONE ) {
            if(xhr.status === 200 ) {
                let date = xhr.response;
                alert(data);
            }

    }
}
    let formData = new formData(form)
    xhr.send();
    
}


