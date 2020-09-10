var updateBtns = document.getElementsByClassName('update-cart')

for (i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product            //trả về {{product.id}} quy định bên store.html
        var action = this.dataset.action                //trả về "add"
        console.log('productId:', productId,'Action:', action)

        //biến 'user' đã được đặt bên script
        console.log('User:',user)
        if (user == 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}
//Trường hợp chưa đăng kí
function addCookieItem(productId,action){
    console.log('Not logged in')
    if (action == 'add'){
        if (cart[productId] == undefined){
            //Đưa giá trị vào OBj 'cart'
            cart[productId] = {'quanity':1}
        }else{
            cart[productId]['quanity'] +=1
        }
    }
    if (action == 'remove'){
        cart[productId]['quanity'] -=1
        if (cart[productId]['quanity'] <=0){
            console.log('Remove Item')
            delete cart[productId]
        }
    }
    console.log('cart',cart)
    //Update cart trong file JSON
    location.reload()
    document.cookie = 'cart='+ JSON.stringify(cart)+ ";domain=;path=/"
}
//Khi đã đăng kí
function updateUserOrder(productId, action){
    console.log('User is logging, sending data...')
    //Địa chỉ để gửi dữ liệu tới
    var url = '/update_item/'
    //Tại sao không tăn giá trị ở đây luôn mà lại sang Views.py
    //Để  cập nhập trên Models luôn? => cập nhập trên database
    //Trên kia không đăng nhập mà cập nhật qua cookie

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,                   //Lấy dữ liệu từ cookie đưa vào file json
        },
        body: JSON.stringify({'productId':productId,'action':action})   //Chuyển thành chuỗi JSON
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
        //tự động tăng số sản phẩm
        location.reload()
    })
}