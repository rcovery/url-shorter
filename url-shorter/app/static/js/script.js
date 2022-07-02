if (document.querySelector('.generated_url')) {
    navigator.clipboard.writeText(document.querySelector('.generated_url').innerHTML);
}