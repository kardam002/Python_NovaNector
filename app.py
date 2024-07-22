from flask import Flask, request, jsonify, render_template
from game import Game

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    game.start()
    return jsonify(message="Game started")

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    response = game.handle_command(command)
    return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)
