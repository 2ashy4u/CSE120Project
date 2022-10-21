from website import create_app

app = create_app()
# makes sure server doesnt continually run
if __name__ == '__main__':
    app.run(debug = True)