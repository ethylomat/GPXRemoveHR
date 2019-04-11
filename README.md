# GPXRemoveHeartrate
> Python tool for removing heartrate data from gpx files.

## Installation

```console
# Clone the project directory
foo@bar:~$ git clone git@github.com:ethylomat/GPXRemoveHR.git
foo@bar:~$ cd GPXRemoveHR
foo@bar:~$ pip3 install .
Successfully built GPXRemoveHeartrate
Installing collected packages: GPXRemoveHeartrate
Successfully installed GPXRemoveHeartrate-0.1
```

## Usage

To remove hr data from gpx file use the command `remove-hr`:

```console
foo@bar:~$ remove-hr 2019-04-07_09-15.gpx 2019-04-08_19-12.gpx
Processed: 2019-04-07_09-15.gpx
Processed: 2019-04-08_19-12.gpx
```

You will find the new files with prefix `removed_hr_` in your directory:

`removed_hr_2019-04-07_09-15.gpx` `removed_hr_2019-04-08_19-12.gpx`.
