# Test of BE position
This is the test result that applying for the backend engineer position.

## Test Result
The scripts of answer are located in directories `part1` and `part2`. For `part2`, I choose to do the question `b`. Please follow the instructions below to check the result.

## Create python virtualenv for this project
If you have installed `virtualenv` in your environment, you can use the shell script `mkvenv.sh` to set up the virtual environment for this project.

```
$ ./mkvenv.sh
```

## Run python scripts
1. Source the python virtual env before running python scripts

  ```
  $ . venv/bin/activate
  ```

2. Run python scripts

  * Once you have done the step 1, you can run python scripts under `part1` or `part2` for the result. For example:

      ```
      $ ./part1/Counting.py
      $ ./part1/Integration.py
      $ ./part1/MultiplesOf3and5.py
      ```
  
  * For part2,
  
      To run the simple web server:

      ```
      $ ./part2/b.py
      ```
      
      An example to check the web server:

      ```
      $ curl -X GET http://localhost:1234/
      "Sparse is better than dense."
      ```
