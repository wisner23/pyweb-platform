# Import configurations
import config
import sys

# Run Server
from app import app

# Set profile
config.PROFILE = sys.argv[1]

app.run(host='0.0.0.0', port=8080, debug=True)

