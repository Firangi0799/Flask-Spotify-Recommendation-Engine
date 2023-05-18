# Spotify Recommendation Engine

This is a Python code for a simple Spotify recommendation engine. It uses the Spotify API to search for a track and get recommendations based on that track.

## Setup

Before running the code, make sure you have the following:

- Python installed on your system
- Spotify API credentials (client ID and client secret)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/spotify-recommendation-engine.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Open the code file `app.py` in a text editor.
2. Replace the `client_id` and `client_secret` variables with your own Spotify API credentials.

## Usage

1. Run the code:

   ```bash
   python recommendation_engine.py
   ```

2. Open your web browser and navigate to [https://spotify-recommendation-engine.onrender.com/](https://spotify-recommendation-engine.onrender.com/).
3. Enter the name of a track in the input field and click the "Submit" button.
4. The application will search for the track and display up to 5 recommended tracks based on the input track.

## Deployment

This application is deployed on Render and can be accessed at [https://spotify-recommendation-engine.onrender.com/](https://spotify-recommendation-engine.onrender.com/).

Please note that you need to deploy this application on your own Render account if you want to access it with your specific credentials.

To deploy the application on Render, follow these steps:

1. Sign up for a Render account at [https://render.com/](https://render.com/).
2. Create a new web service on Render.
3. Set the GitHub repository as the source for the web service.
4. Configure the environment variables `client_id` and `client_secret` with your Spotify API credentials.
5. Deploy the web service.
6. Once the deployment is complete, you can access the application at the provided URL.

## License

This code is released under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.
