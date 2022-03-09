# file-bundler
A small Python script that takes a list of files and organizes them to your liking and then creates a zip-archive.

## Running the script
To run the script, use the following:
- `py file-bundler.py <SOURCE> <TARGET> <NAME>`
  - `<SOURCE>` Full path to directory of unorganized files.
  - `<TARGET>` Full path to where the archive should be placed once the script is done.
  - `<NAME>` Name of outputted archive.

## Example
We have a directory  of files that look something like this:
```
unorganized-files/
├─ some-abc-generic-file
├─ some-ble-file
├─ some-bluetoothrelated-file1
├─ some-bluetoothrelated-file2
├─ some-tcp-file1
├─ some-tcp-file2
├─ some-tcp-file3
├─ some-udp-file
└─ some-websocket-file
```
And we would like to have a structure of two directories, one for web-related files and another one for bluetooth-related files. We also want all files that have the word "generic" in their name to be placed in the root directory.

To let the script know what file structure we want, we edit the dictionary into the wanted file structure:
```python
DIRECTORY_FILE_DICTIONARY = {
    "bluetooth": ["bluetooth", "ble"],  # All bluetooth related files go into "bluetooth"
    "web": ["websocket", "tcp", "udp"], # All web-related files go into "web"
    "root": ["generic"]                 # All files that have "generic" in their name stay in root directory
}
```

We can now run the script with appropriate arguments and output name. Which will give us a zip-archive with the following structure:

`py file-bundler.py /path/to/unorganized-files /path/to/output organized`

```
organized.zip
├─ bluetooth/
│  ├─ some-ble-file
│  ├─ some-bluetoothrelated-file1
│  └─ some-bluetoothrelated-file2
├─ web/
│  ├─ some-tcp-file1
│  ├─ some-tcp-file2
│  ├─ some-tcp-file3
│  ├─ some-udp-file1
│  └─ some-websocket-file
└─ some-abc-generic-file
```
