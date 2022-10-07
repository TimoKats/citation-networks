# packages
from flask import Flask, render_template, request
import networkx as nx
from pyvis.network import Network
# classes
from get_data import data
app = Flask(__name__)

def make_subarticle_graph(catagory, country, language, amount):
    news = data(catagory, country, language, amount)
    edge_list = news.sub_articles()
    edge_list = edge_list.drop_duplicates(keep=False).reset_index(drop=True)
    G = nx.from_pandas_edgelist(edge_list, source='source',target='target', create_using=nx.DiGraph())
    net = Network(notebook=True, width="100%", height="100%", directed=True)
    net.from_nx(G)
    net.show('static/graphs/network.html')

@app.route('/', methods=['POST'])
def form_network():
    if request.method == 'POST':
        form_data = request.form
        make_subarticle_graph(form_data['topic'], form_data['country'], 'en', int(form_data['amount']))
    return render_template('index.html', category=form_data['topic'], country= form_data['country'], amount=form_data['amount'])

@app.route("/")
def home():
    make_subarticle_graph('business', 'US', 'en', 20)
    return render_template('index.html', category= 'business', country= 'US', amount='20')

if __name__ == '__main__':
    app.run(debug=True)