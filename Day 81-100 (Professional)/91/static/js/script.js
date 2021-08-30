function hex_copied(color){
    const new_element = document.createElement('textarea');
    new_element.value = color;
    document.body.appendChild(new_element);
    new_element.select();
    document.execCommand('copy');
    document.body.removeChild(new_element);
    alert('Hex code copied to clipboard!')
}