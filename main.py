'''import web_app
import config

app = web_app.create_app(config)

if __name__ == "__main__":
    app.run(debug=True)'''


from web_app import app


if __name__ == "__main__":
    app.run(debug=True)