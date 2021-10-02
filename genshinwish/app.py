# Author: Omgeta
# Description: Flask App
# Date: 2/10/2021

# Dependencies
from structures.node import PityNode
from structures.tree import PityTree
from flask import Flask
from flask import redirect, render_template, request

# Config
app = Flask(__name__)

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analysis", methods=["POST"])
def analysis():
    user_pity = int(request.form.get("user_pity", 0))
    user_cons = int(request.form.get("user_cons", 0))
    user_guarantee = False #TODO: change to string -> bool conversion
    
    start_node = PityNode(user_cons, 1, user_guarantee)
    tree = PityTree(start_node)
    tree.construct_tree(user_pity)

    layer = tree.get_layer(user_pity) #TODO: replace with a selection option
    layer_prob = tree.calc_total_probability(layer)
    print(layer_prob) #TODO: debug
    percentage_prob = tuple(map(lambda x: f"{x*100}%", layer_prob))

    return render_template("analysis.html", result=percentage_prob)

# Driver
app.run()
