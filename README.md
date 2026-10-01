#URL SHORTNER 

##WHAT IT IS
 It is a url shortner i built using flask , HTML , and CSS . you paste a long link in this and it gives you shorter link that redirects to the original.

## Features
- Turns a long URL into a random 6 character code
- Lets you pick your own alias, and shows an error if it's already taken
- It Counts how many times each short link is generrated
- Saves everything in `data.json`, so links are still there after a restart
- Shows an error for an empty URL and adds `http://` if you forget it

## How to run
Install Flask:

```
pip install -r requirements.txt
```

Start the app:

```
python main.py
```

Then open http://127.0.0.1:5000 in your browser.

## Files
- `main.py`: the backend using flask
- `templates/index.html`: the home page
- `static/url.css`: the styling for buttons, text and also for layouts
- `requirements.txt`: just Flask

## What I learned
Flask was picky about folders. my page shows errors until i put html and css in seprate template ans staic folder. I also got stuck in `startswith` bug,

I used a JSON file instead of a database because it was simpler. It works fine for one person, but it would break if lots of people used it at once.

## Future ideas
- A delete button for old links
- Links that expire
- A real database instead of JSON

Made by [your name]
