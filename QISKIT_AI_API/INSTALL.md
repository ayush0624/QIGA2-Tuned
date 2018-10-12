# QISKit ACQUA Tutorials


## Guide for Installation and Setup

### 1. Download the QISKit ACQUA Tutorials and Samples

The easiest way is to [download](https://github.com/QISKit/qiskit-acqua-tutorials/archive/master.zip) the tutorials. 
Unzip the archive in the directory of your choice.

More advanced users may choose to use `git`. If you have `git` installed, run

```
git clone https://github.com/QISKit/qiskit-acqua-tutorials.git
```

If you need to install `git` follow the instructions [here](https://help.github.com/articles/set-up-git/).


### 2. Refer to QISKit installation

QISKit ACQUA depends on QISKit Core. While installation of QISKit ACQUA will automatically install QISKit
we encourage you to read the
[QISKit tutorial installation](https://github.com/QISKit/qiskit-tutorial/blob/master/INSTALL.md#2-install-qiskit)
and follow the recommendation there for setting up a virtual environment.


### 3. Install QISKit ACQUA

_**Note**: If you plan to run the QISKit ACQUA Chemistry you may like to skip
to step 4 below, since that will automatically install QISKit ACQUA as its dependency._

The latest release version of QISKit ACQUA should be the one installed.

The latest release can be installed using

```
pip install qiskit-acqua
```

If you have an older version pre-installed then it can be updated using

```
pip install -U qiskit-acqua
```

### 4. Install QISKit ACQUA Chemistry

If you plan to run the QISKit ACQUA Chemistry notebooks or samples then this needs to
be installed as well. This will automatically install QISKit ACQUA as a 
dependency, so in this case manually carrying out step 3 above is not necessary. 

The latest release version of QISKit ACQUA Chemistry should be the one installed.

The latest release can be installed using

```
pip install qiskit-acqua-chemistry
```

If you have an older version pre-installed then it can be updated using

```
pip install -U qiskit-acqua-chemistry
```

## 5. Explore the tutorials

In step 2 above, if you followed the QISKit recommendation of a virtual environment then please refer to
[QISKit explore the tutorials](https://github.com/QISKit/qiskit-tutorial/blob/master/INSTALL.md#4-explore-the-tutorials)
for information on how to activate the environment.

You can now **start Jupyter with the index notebook**

```
jupyter notebook index.ipynb
```
