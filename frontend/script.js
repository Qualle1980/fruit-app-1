fetch("http://127.0.0.1:8000/fruits/")
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const fruitList = document.getElementById("fruit-list");

        data.forEach(function(fruit) {
            const li = document.createElement("li");

            li.innerText = fruit.icon + " " + fruit.name + " - " + fruit.gewicht + "g - " + fruit.farbe;

            fruitList.appendChild(li);
        });
    });