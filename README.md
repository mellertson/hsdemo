Submission of Solution Engineering Exercise for Michael Ellertson
---

**Submission Date:** 01/26/2022<BR>
**Submitted By:** Michael Ellertson

This repo contains the code for ***Part 1: Technical Exercise*** for Michael 
Ellertson's submission to Hyperscience of the ***Solution Engineering Exercise***.


# Required Software

This Git repo includes a utility named `hsexport`.  Before using the `hsexport` 
utility the following software must be installed.

* Python version 3.7 or higher
* Pip
* Git (must be accessible from the command line)

# Installation

To install this software open a command line terminal (command prompt or 
Power Shell on Windows) and execute the following commands.

```shell script
git clone https://github.com/mellertson/hsdemo.git
cd hsdemo
pip3 install --user -r ./requirements.txt
```

# Usage

The `hsexport` utility, included in this Git repo, can output help text 
describing its supported command line options and syntax.  To do
so open a command line terminal and enter `./hsexport -h`, which will output the
following help text.

```shell script
usage: hsexport [-h] [-t TOKEN] [-s SERVER] submission_id filename

This utility will get a submission object from a HyperScience REST API server
and write it to a CSV file.

positional arguments:
  submission_id         A submission ID to get and write to the CSV file.
  filename              A filename where the CSV file will be saved.

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        (optional) An token to authenticate with the
                        HyperScience REST API. Default:
                        "46a2be39a2db8c79013f055bcb273093b587364a"
  -s SERVER, --server SERVER
                        (optional) A URI of the HyperScience server. Default:
                        "https://sales1.demo.hyperscience.com"
```

For example to get Submission ID 1 from the HyperScience REST API and write 
it to a CSV file named "output1.csv" open a command line terminal and enter the
following command.

```shell script
./hsexport 1 ./output1.csv
```