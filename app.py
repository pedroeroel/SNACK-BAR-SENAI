from flask import Flask, session, redirect, render_template

app = Flask("__name__")

sandwiches = [
    {"name": "X-Bacon", "description": "Bacon, queijo, hambúrguer e salada", "price": 15.00},
    {"name": "X-Salada", "description": "Queijo, hambúrguer e salada", "price": 12.00},
    {"name": "X-Egg", "description": "Ovo, queijo, hambúrguer e salada", "price": 13.50},
    {"name": "X-Tudo", "description": "Bacon, ovo, queijo, presunto, hambúrguer e salada", "price": 18.00},
    {"name": "X-Frango", "description": "Frango, queijo, milho, salada", "price": 14.00},
    {"name": "X-Calabresa", "description": "Calabresa, queijo, cebola, salada", "price": 15.50},
    {"name": "X-Picanha", "description": "Picanha, queijo, cebola caramelizada, salada", "price": 20.00},
    {"name": "X-Veggie", "description": "Hambúrguer vegetariano, queijo, salada", "price": 16.00},
    {"name": "X-BBQ", "description": "Molho barbecue, bacon, queijo, hambúrguer", "price": 17.00},
    {"name": "X-Fish", "description": "Peixe empanado, queijo, alface, molho tártaro", "price": 14.50}
]


@app.route("/")
def menu():
    return render_template("menu.html", sandwiches=sandwiches)

if __name__ == "__main__":
    app.run(debug=True)