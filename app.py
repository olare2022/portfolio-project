from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github_stats', methods=['POST'])
def github_stats():
    # Get the GitHub username from the form
    username = request.form['username']

    # Fetch GitHub statistics using the GitHub API
    stats_url = f'https://api.github.com/users/{username}'
    response = requests.get(stats_url)

    if response.status_code == 200:
        # Parse the JSON response
        github_stats = response.json()

        # Extract relevant information
        name = github_stats.get('name', '')
        followers = github_stats.get('followers', 0)
        public_repos = github_stats.get('public_repos', 0)
        avatar_url = github_stats.get('avatar_url', '')

        # Prepare the response data
        data = {
            'name': name,
            'followers': followers,
            'public_repos': public_repos,
            'avatar_url': avatar_url,
        }

        return jsonify(data)
    else:
        # Return an error message if the GitHub API request fails
        return jsonify({'error': 'Unable to fetch GitHub statistics.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
