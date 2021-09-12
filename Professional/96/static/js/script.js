function notLoggedIn(){
    alert("You need to login to add to cart!")
}

function addedToCart(){
    alert("Product has been added to cart!");
    document.getElementById('cart_form').submit();
}