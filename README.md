# SportneVadbe app with flask and ndb (Datastore wrapper library)

This is an example of a structured app with the **new ndb** library (Datastore wrapper) and tests (using pytest).

## Links

- [The new repository on GitHub](https://github.com/Vrcelj1979/SportneVadbe)

## Preview

![](static/img/.......)

## Requirements

> Note that requirements will install the new ndb library: google-cloud-ndb

Install the necessary libraries using this command:

    pip install -r requirements.txt

Using a virtual environment is strongly encouraged!

## Running the emulator and the web app via run.py (RECOMMENDED)

> This has only been tested on Mac so far. Not sure if it's working on Linux or Windows.

The easiest way to run the web app is via the `run.py` script. Right click it in PyCharm and select `Run 'run'`.

Alternatively, you can run it via the Terminal:

    python run.py

In this case you'll have to shut it down using CTRL+C combo.

This script also allows you to run tests (it asks you at the beginning).

## Running the emulator and web app manually (without run.py)

If the `run.py` script does not work on your computer, you'll have to run the Emulator and the web app manually.

### Run the Datastore emulator

First run the datastore emulator:

    gcloud beta emulators datastore start --no-legacy --data-dir=. --project test --host-port "localhost:8001"

Notice that the `8001` port has been used. This is for running the web app. To run tests, use port `8002`.

### Run the web app.

Next, run the web app. Right-click on `main.py` and select `Run 'main'`. Your web app will now be accessible via `localhost:8080`. Whenever
you'll make any change in your code, make sure to **reload** the web app via this button:

![](static/img/reload-web-app.png)

To **shut down** the web app click the **red square icon** below the reload button.

Alternatively, you can run the web app via the Terminal with this command:

    python main.py

In this case you'll have to shut it down using CTRL+C combo.

If you'd like to use Flask's auto-reloading features, run the web app with these two commands:

    export FLASK_APP=main.py
    flask run --host localhost --port 8080 --reload

This will automatically reload your app whenever you make any changes in your Python files.

