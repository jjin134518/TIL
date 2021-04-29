```html
document.querySelector('h1')
<h1 id=​"header">​DOM Manipulation​</h1>​
document.querySelector('#header')
<h1 id=​"header">​DOM Manipulation​</h1>​
document.querySelector('h1') === document.querySelector('#header')
true
mainHeader = document.querySelector('h1')
<h1 id=​"header">​DOM Manipulation​</h1>​
mainHeader.innerText
"DOM Manipulation"
mainHeader.innerText = 'CHANGE'
"CHANGE"
```

