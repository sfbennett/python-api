# Python API Scripts

This repository contains three Python scripts that fetch data from different APIs:

1. `albums.py`
2. `cat-facts.py`
3. `useless-facts.py`

The `albums.py` script fetches data from my own album API hosted on Render and appends the details to a `.txt` file.

## Setup Instructions

1. **Clone the repository:**

```
git clone https://github.com/your-username/python-api.git
cd python-api
```

2. Create a `requirements.txt` file including:

```
requests==2.32.3
python-dotenv
```

3. Create a virtual environment:

```
python3 -m venv venv
```

4. Activate the virtual environment:

```
source venv/bin/activate
```

5. Install dependencies:

```
pip install -r requirements.txt

```

6. Verify packages with:

```
pip list

```

7. Run the Python script:

- `python3 py-scipts/albums.py`

- `python3 py-scipts/cat-facts.py`

- `python3 py-scipts/useless-facts.py`
