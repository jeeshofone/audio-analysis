# audio-analysis
A small set of tools for analyzing audio

## Setup

After cloning the repo, create a virtualenv in the cloned directory

`python3 -m venv .`

Enter the virtualenv
`source ./bin/activate`
(to leave the virtualenv)
`deactivate`

Consider upgrading pip
`python3 -m pip install --upgrade pip`

Install the requirements

`pip3 install -r requirements.txt`


Run the desired script to see the help output

```
% python3 frequency-plot-convert.py
usage: frequency-plot-convert.py [-h] --file FILE --output OUTPUT
frequency-plot-convert.py: error: the following arguments are required: --file/-f, --output/-o
```


This script expects a `--file` input of a CSV with columns for frequency and amplitude and an `--output` for the generated wav file

Sample files include 4k.csv and tenth-octave-unity-signal.csv

Try:
`python3 frequency-plot-convert.py --file 4k.csv --output 4k.wav`
