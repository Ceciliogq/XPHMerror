1. Compile [this LAL](https://github.com/Ceciliogq/lalsuite/tree/fix-instability) in DEGUB mode under the igwn-py38 environment:
```bash
conda activate igwn-py38
configure --prefix=$CONDA_PREFIX --disables... CFLAGS'-g -D PHENOMXHMDEBUG'
```

2. Run `python xphm_test.py`. This will write .dat files for the Euler angles. In this script you can switch on/off multibanding.

3. Plot the result with PlotAngles.ipynb.
